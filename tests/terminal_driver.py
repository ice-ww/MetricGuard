"""Real terminal driver: hidden Windows console or POSIX PTY, no input mocking."""
import ctypes
from ctypes import wintypes
import json
import os
import subprocess
import sys
import time
from pathlib import Path
import signal


def windows(command, operations):
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    class Coord(ctypes.Structure):
        _fields_ = [('X',ctypes.c_short),('Y',ctypes.c_short)]
    class Rect(ctypes.Structure):
        _fields_ = [(name,ctypes.c_short) for name in ('Left','Top','Right','Bottom')]
    class Info(ctypes.Structure):
        _fields_ = [('size',Coord),('cursor',Coord),('attributes',wintypes.WORD),
                    ('window',Rect),('maximum',Coord)]
    class Char(ctypes.Union):
        _fields_ = [('unicode',wintypes.WCHAR),('ascii',ctypes.c_char)]
    class Key(ctypes.Structure):
        _fields_ = [('down',wintypes.BOOL),('repeat',wintypes.WORD),
                    ('virtual',wintypes.WORD),('scan',wintypes.WORD),
                    ('char',Char),('control',wintypes.DWORD)]
    class Event(ctypes.Union):
        _fields_ = [('key',Key),('padding',ctypes.c_byte*16)]
    class Record(ctypes.Structure):
        _fields_ = [('kind',wintypes.WORD),('event',Event)]
    kernel.CreateFileW.argtypes = [wintypes.LPCWSTR,wintypes.DWORD,wintypes.DWORD,
                                  ctypes.c_void_p,wintypes.DWORD,wintypes.DWORD,wintypes.HANDLE]
    kernel.CreateFileW.restype = wintypes.HANDLE
    kernel.GetConsoleScreenBufferInfo.argtypes = [wintypes.HANDLE,ctypes.POINTER(Info)]
    kernel.ReadConsoleOutputCharacterW.argtypes = [wintypes.HANDLE,wintypes.LPWSTR,wintypes.DWORD,Coord,ctypes.POINTER(wintypes.DWORD)]
    kernel.WriteConsoleInputW.argtypes = [wintypes.HANDLE,ctypes.POINTER(Record),wintypes.DWORD,ctypes.POINTER(wintypes.DWORD)]
    startup = subprocess.STARTUPINFO()
    startup.dwFlags = subprocess.STARTF_USESHOWWINDOW
    startup.wShowWindow = 0
    child = subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE, startupinfo=startup)
    kernel.FreeConsole()
    deadline = time.monotonic()+10
    while not kernel.AttachConsole(child.pid):
        if time.monotonic() > deadline:
            child.kill()
            raise RuntimeError('cannot attach to test console')
        time.sleep(.05)
    output = kernel.CreateFileW('CONOUT$',0xC0000000,3,None,3,0,None)
    input_handle = kernel.CreateFileW('CONIN$',0xC0000000,3,None,3,0,None)
    def read():
        info = Info()
        if not kernel.GetConsoleScreenBufferInfo(output, ctypes.byref(info)):
            raise ctypes.WinError(ctypes.get_last_error())
        count = min(30000, info.size.X*(info.cursor.Y+1))
        buffer = ctypes.create_unicode_buffer(count+1)
        read_count = wintypes.DWORD()
        if not kernel.ReadConsoleOutputCharacterW(output,buffer,count,Coord(0,0),ctypes.byref(read_count)):
            raise ctypes.WinError(ctypes.get_last_error())
        return buffer.value
    def write(value):
        for char in value.replace('\n','\r'):
            record = Record()
            record.kind = 1
            record.event.key.down = True
            record.event.key.repeat = 1
            record.event.key.char.unicode = char
            record.event.key.virtual = 13 if char == '\r' else 0
            written = wintypes.DWORD()
            if not kernel.WriteConsoleInputW(input_handle,ctypes.byref(record),1,ctypes.byref(written)):
                raise ctypes.WinError(ctypes.get_last_error())
    def interrupt():
        kernel.SetConsoleCtrlHandler(None,True)
        if not kernel.GenerateConsoleCtrlEvent(0,0):
            raise ctypes.WinError(ctypes.get_last_error())
    try:
        screen = perform(child, operations, read, write, interrupt)
        return {'code':child.wait(timeout=20),'screen':screen}
    finally:
        if child.poll() is None:
            child.kill()
        child.wait(timeout=10)
        kernel.CloseHandle.argtypes = [wintypes.HANDLE]
        kernel.CloseHandle(output)
        kernel.CloseHandle(input_handle)
        kernel.FreeConsole()


def posix(command, operations):
    import fcntl
    import pty
    import select
    import termios
    master, slave = pty.openpty()
    def control():
        os.setsid()
        fcntl.ioctl(slave, termios.TIOCSCTTY, 0)
    child = subprocess.Popen(command, stdin=slave, stdout=slave, stderr=slave, preexec_fn=control)
    os.close(slave)
    data = bytearray()
    def read():
        while select.select([master],[],[],0)[0]:
            try:
                chunk = os.read(master,65536)
            except OSError:
                break
            if not chunk:
                break
            data.extend(chunk)
        return data.decode('utf-8',errors='replace')
    try:
        screen = perform(child,operations,read,lambda value:os.write(master,value.encode()),
                         lambda:os.killpg(child.pid,signal.SIGINT))
        return {'code':child.wait(timeout=20),'screen':screen}
    finally:
        if child.poll() is None:
            child.kill()
        child.wait(timeout=10)
        os.close(master)


def perform(child, operations, read, write, interrupt):
    for operation in operations:
        deadline = time.monotonic()+90
        def ready():
            return Path(operation['wait_file']).exists() if 'wait_file' in operation else operation['wait'] in read()
        while not ready():
            if child.poll() is not None or time.monotonic()>deadline:
                raise RuntimeError('terminal condition not met:\n'+read())
            time.sleep(.05)
        if operation.get('hold'):
            time.sleep(operation['hold'])
            if child.poll() is not None:
                raise RuntimeError('terminal closed before dismissal')
        if operation.get('interrupt'):
            interrupt()
        else:
            write(operation.get('write',''))
        if 'touch' in operation:
            Path(operation['touch']).touch()
    deadline = time.monotonic()+30
    while child.poll() is None and time.monotonic()<deadline:
        time.sleep(.05)
    if child.poll() is None:
        raise RuntimeError('terminal did not exit:\n'+read())
    return read()


if __name__ == '__main__':
    payload = json.load(sys.stdin)
    result = (windows if os.name == 'nt' else posix)(payload['command'],payload['operations'])
    print(json.dumps(result, ensure_ascii=False), flush=True)
