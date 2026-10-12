"""Small, fail-closed DuckDB SQL subset for the T02 experiment snapshot.

This is a policy layer, not the sandbox. Its canonical output must still execute
inside the restricted worker. Adding syntax requires an explicit policy review.
"""

from sqlglot import exp, parse
from sqlglot.errors import SqlglotError
from sqlglot.optimizer.qualify import qualify
from sqlglot.optimizer.scope import traverse_scope

POLICY_VERSION = "t02-v1"
SCHEMA: dict[str, object] = {
    "sales": {"id": "INTEGER", "region_id": "INTEGER", "amount": "INTEGER"},
    "regions": {"id": "INTEGER", "name": "VARCHAR"},
}
MAX_SQL_BYTES = 8192
MAX_NODES = 512
MAX_DEPTH = 32

# Exact classes deliberately exclude Anonymous, Command, table functions, casts,
# recursive queries, extension functions, and future SQLGlot subclasses.
ALLOWED_NODES = frozenset({
    exp.Select, exp.From, exp.Table, exp.Identifier, exp.Column, exp.Alias,
    exp.TableAlias, exp.CTE, exp.With, exp.Join, exp.Subquery,
    exp.Group, exp.Order, exp.Ordered, exp.Where, exp.Having, exp.Limit,
    exp.Distinct, exp.Star, exp.Literal, exp.Null, exp.Boolean, exp.Paren,
    exp.EQ, exp.NEQ, exp.GT, exp.GTE, exp.LT, exp.LTE, exp.And, exp.Or,
    exp.Not, exp.Is, exp.In, exp.Between, exp.Exists,
    exp.Add, exp.Sub, exp.Mul, exp.Div, exp.Neg,
    exp.Sum, exp.Count, exp.Min, exp.Max, exp.Avg, exp.Coalesce, exp.Nullif,
    exp.Case, exp.If,
})


class PolicyError(ValueError):
    """Input is outside the explicitly reviewed SQL subset."""


def _inspect(tree: exp.Expr) -> None:
    if type(tree) is not exp.Select:
        raise PolicyError("Only a SELECT is allowed")
    count = 0
    stack = [(tree, 1)]
    while stack:
        node, depth = stack.pop()
        count += 1
        if count > MAX_NODES or depth > MAX_DEPTH:
            raise PolicyError("SQL AST complexity limit exceeded")
        if type(node) not in ALLOWED_NODES:
            raise PolicyError(f"Unapproved AST node: {type(node).__name__}")
        if isinstance(node, exp.With) and node.args.get("recursive"):
            raise PolicyError("Recursive CTE is forbidden")
        if isinstance(node, exp.Table):
            if type(node.this) is not exp.Identifier or node.db or node.catalog:
                raise PolicyError("Only unqualified physical table or CTE names are allowed")
        if isinstance(node, exp.Column) and (node.db or node.catalog):
            raise PolicyError("Qualified catalog/schema columns are forbidden")
        stack.extend((child, depth + 1) for child in node.iter_expressions())

    # Scope resolution is necessary: a CTE name does not authorize a physical
    # table with that name inside an earlier or nested scope.
    for scope in traverse_scope(tree):
        for _, source in scope.selected_sources.values():
            if isinstance(source, exp.Table) and source.name.lower() not in SCHEMA:
                raise PolicyError(f"Unapproved physical table: {source.name}")


def _parse_one(sql: str) -> exp.Expr:
    if len(sql.encode("utf-8")) > MAX_SQL_BYTES:
        raise PolicyError("SQL byte limit exceeded")
    # Bound parser recursion before constructing its AST. Conservative rejection
    # of parentheses in strings/comments is acceptable for this narrow subset.
    depth = 0
    for char in sql:
        if char == "(":
            depth += 1
            if depth > MAX_DEPTH:
                raise PolicyError("SQL nesting limit exceeded")
        elif char == ")":
            depth = max(0, depth - 1)
    statements = parse(sql, read="duckdb")
    if len(statements) != 1 or statements[0] is None:
        raise PolicyError("Exactly one nonempty statement is required")
    return statements[0]


def validate_sql(sql: str) -> str:
    """Return checked canonical SQL, or reject before any database execution."""
    try:
        tree = _parse_one(sql)
        _inspect(tree)
        # Validate column names and ambiguity through scopes; star expansion is
        # based solely on this static, reviewed physical schema.
        qualified = qualify(tree, dialect="duckdb", schema=SCHEMA)
        _inspect(qualified)
        canonical = qualified.sql(dialect="duckdb", comments=False)
        regenerated = _parse_one(canonical)
        _inspect(regenerated)
        qualify(regenerated, dialect="duckdb", schema=SCHEMA)
        return canonical
    except PolicyError:
        raise
    except (SqlglotError, RecursionError, ValueError, KeyError) as exc:
        raise PolicyError(f"SQL validation failed: {type(exc).__name__}") from exc
