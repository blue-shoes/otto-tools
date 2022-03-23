import os
import shutil
import sys
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\adam.scharf\AppData\Local\Continuum\anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\adam.scharf\AppData\Local\Continuum\anaconda3\tcl\tk8.6'

__version__ = '0.8.0'
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

includes = ['tkinter']
excludes = ['matplotlib', 'sqlite3', 'PyQt5', 'scipy', 'numpy-mkl' 'babel', 'jedi', 'jupyter_client', 'sphinx']
packages = ['numpy', 'pandas', 'xlsxwriter']

setup(
    name='Ottoneu Draft Tool',
    description='A tool for Ottoneu drafts',
    version=__version__,
    executables=[Executable('otto_draft_tool.py', base=base)],
    options = {'build_exe': {
        'packages': packages,
        'includes': includes,
        'include_msvcr': True,
        'excludes': excludes
    }},
)

path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))
build_path = os.path.join(path, 'build', 'exe.win32-3.7')
shutil.copy(r'C:\Users\adam.scharf\AppData\Local\Continuum\anaconda3\DLLs\tcl86t.dll', build_path)
shutil.copy(r'C:\Users\adam.scharf\AppData\Local\Continuum\anaconda3\DLLs\tk86t.dll', build_path)