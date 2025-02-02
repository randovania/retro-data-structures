@ECHO OFF
IF EXIST requirements.txt python -m pip install -U -r requirements.txt
python -m pip install .
