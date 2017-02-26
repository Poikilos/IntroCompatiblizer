@echo off
SET FOUND_KIVY=FALSE

SET KIVY_BAT=D:\programs\Kivy-1.8.0-py3.3-win32\kivy.bat
IF EXIST "%KIVY_BAT%" GOTO FOUNDKIVY
SET KIVY_BAT=D:\programs\Kivy-1.8.0-python3-win32\kivy.bat
IF EXIST "%KIVY_BAT%" GOTO FOUNDKIVY
SET KIVY_BAT=C:\Kivy-1.8.0-py3.3-win32\kivy.bat
IF EXIST "%KIVY_BAT%" GOTO FOUNDKIVY
SET KIVY_BAT=C:\Kivy-1.8.0-python3-win32\kivy.bat
IF EXIST "%KIVY_BAT%" GOTO FOUNDKIVY
SET KIVY_BAT=%APPDATA%\Kivy-1.8.0-python3-win32\kivy.bat
IF EXIST "%KIVY_BAT%" GOTO FOUNDKIVY
SET KIVY_BAT=C:\Kivy\kivy.bat
IF EXIST "%KIVY_BAT%" GOTO FOUNDKIVY

GOTO NOKIVY

:FOUNDKIVY
SET FOUND_KIVY=TRUE
SET PROGRAMFOLDERNAME=IntroCompatiblizer
SET PROGRAM_PY_NAME=introcompatiblizer.py

SET PROGRAM_PY_FULLNAME=C:\Users\Owner\OneDrive\Projects-kivy\%PROGRAMFOLDERNAME%\%PROGRAM_PY_NAME%
IF EXIST "%PROGRAM_PY_FULLNAME%" GOTO FOUNDPROGRAM
SET PROGRAM_PY_FULLNAME=C:\Users\Owner\SkyDrive\Projects-kivy\%PROGRAMFOLDERNAME%\%PROGRAM_PY_NAME%
IF EXIST "%PROGRAM_PY_FULLNAME%" GOTO FOUNDPROGRAM
SET PROGRAM_PY_FULLNAME=D:\Projects-kivy\%PROGRAMFOLDERNAME%\%PROGRAM_PY_NAME%
IF EXIST "%PROGRAM_PY_FULLNAME%" GOTO FOUNDPROGRAM

GOTO NOPROGRAM
 
:FOUNDPROGRAM
"%KIVY_BAT%" "%PROGRAM_PY_FULLNAME%"

GOTO ENDSILENTLY

:NOKIVY
echo.
echo Could not find Kivy! Try installing it such that kivy.bat is in C:\Kivy or:          C:\Kivy-1.8.0-py3.3-win32\
echo.
pause

GOTO ENDSILENTLY

:NOPROGRAM
echo.
echo Could not find program! Try installing it such that program exists:                   %PROGRAM_PY_FULLNAME%
echo.
pause

:ENDSILENTLY