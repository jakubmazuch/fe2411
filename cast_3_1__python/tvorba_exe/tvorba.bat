@echo off
echo === Cistim stare soubory ===
rmdir /s /q build
rmdir /s /q dist
del /q neco.spec

echo === Tvorim novou .exe verzi (soubor neco.py) ===
py -m PyInstaller --onefile --console neco.py

echo.
echo === Hotovo! Vystupni soubor najdes ve složce "dist". ===
pause