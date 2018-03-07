@setlocal
py -3 -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
python setup.py bdist_launcher
call venv\Scripts\deactivate.bat
cd dist\launcher3-64 && hello.exe
@endlocal