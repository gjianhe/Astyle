@echo off
::del *.exe
pyinstaller -F --icon=123.ico astyle.py
copy .\dist\*.exe .\
del /Q *.spec
rd /S /Q dist
rd /S /Q build
rd /S /Q __pycache__
pause
