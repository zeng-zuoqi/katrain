@echo off
cd /d "%~dp0"
if exist "..\katrain-env\Scripts\pythonw.exe" (
    start "" "..\katrain-env\Scripts\pythonw.exe" -m katrain "katrain\white60.sgf"
) else (
    python -m katrain "katrain\white60.sgf"
)
