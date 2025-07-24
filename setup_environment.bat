
@echo on

REM 1 Erstelle eine virtuelle Umgebung
python -m venv .\venv

REM 2) Aktiviere die virtuelle Umgebung
call .\venv\Scripts\activate

REM 3) Liste die installierten Pakete auf
pip list

PAUSE

REM 4) Installiere netmiko
pip install netmiko

REM 5) Installiere PySide6
pip install PySide6

REM 6) Liste die installierten Pakete auf
pip list

REM 7) Deaktiviere die virtuelle Umgebung
deactivate

REM Warte auf Eingabe bevor das Fenster geschlossen wird
PAUSE
