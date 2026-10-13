"""Small static SVG renderer for already resolved evidence points only."""
from html import escape


def render_svg(chart: dict) -> str:
    points=chart['points']
    low=min(0,min(float(y) for _,y in points))
    high=max(0,max(float(y) for _,y in points))
    extent=high-low or 1
    def y_at(value):
        return 210-(float(value)-low)/extent*170
    width=540/len(points)
    parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 280" role="img">',
           '<title>'+escape(chart['chart_id'])+'</title>',
           '<rect width="640" height="280" fill="white"/>',
           f'<path d="M50 {y_at(0)}H600" stroke="#777"/>']
    xy=[]
    for index,(label,value) in enumerate(points):
        x=50+(index+.5)*width; y=y_at(value); xy.append(f'{x},{y}')
        title=escape(str(label)+': '+str(value))
        if chart['kind']=='bar':
            parts.append(f'<rect x="{x-width*.35}" y="{min(y,y_at(0))}" width="{width*.7}" height="{abs(y-y_at(0))}" fill="#167d9a"><title>{title}</title></rect>')
        else:
            parts.append(f'<circle cx="{x}" cy="{y}" r="3" fill="#167d9a"><title>{title}</title></circle>')
        if len(points)<=12:
            parts.append(f'<text x="{x}" y="230" text-anchor="middle" font-size="11">{escape(str(label))}</text>')
    if chart['kind']=='line':
        parts.append('<polyline points="'+' '.join(xy)+'" fill="none" stroke="#167d9a"/>')
    parts.extend([f'<text x="5" y="42" font-size="11">{high:g}</text>',
                  f'<text x="5" y="210" font-size="11">{low:g}</text>',
                  '<text x="50" y="265" font-size="11">'+('Partial result; not a complete population' if 'partial_result_not_complete_population_or_ranking' in chart['limitations'] else 'Values resolved from cited evidence')+'</text>','</svg>'])
    return ''.join(parts)
