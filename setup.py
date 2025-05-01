
from sys import executable
from cx_Freeze import setup, Executable

setup(
    name="LearnSync",
    version="1.0",
    
executables=[Executable("final.py")]
)
