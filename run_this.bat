@ECHO OFF
SET /p network_id= Network ID: 
SET /p date= Date(yyyy-mm-dd): 
python main.py %network_id% %date%
PAUSE