import sys
from cx_Freeze import setup, Executable

base = None 
if sys.platform == "win32":
    base = "Win32GUI"
   
exe = Executable(script="spellpop.py", base=base)
 
include_files = ["resources/sound", "resources/fonts", "resources/words"]
includes=[]
excludes=[]
packages=[]

setup(version="0.1",
         description="Boring Spelling Game",
         author="iminurnamez",
         name="Boring Spelling Game",
         options={"build_exe": {"includes": includes, "include_files": include_files, "packages": packages, "excludes": excludes}},
         executables=[exe])

