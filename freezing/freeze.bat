
pyinstaller -c --clean -y ^
--additional-hooks-dir=freezing\hooks ^
speechtools\command_line\sct.py
