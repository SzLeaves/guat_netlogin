@echo off

cd %cd%
echo. >> run.log
echo %date% %time% >> run.log
python netlogin.py up >> run.log