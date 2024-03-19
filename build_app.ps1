python -m pip install virtualenv
python -m virtualenv .\venv
.\venv\Scripts\activate.ps1
python -m pip install -r requirements.txt
python -m nuitka --onefile --follow-imports --enable-plugin=pyqt5 --include-data-dir=Icons=Icons --include-data-dir=lib=lib --include-data-dir=logo_urls=logo_urls --windows-disable-console --windows-icon-from-ico=icons/app.ico __main__.py
