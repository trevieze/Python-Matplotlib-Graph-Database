@echo off&SETLOCAL

@echo off
for /F "usebackq tokens=1,2 delims==" %%i in (`wmic os get LocalDateTime /VALUE 2^>NUL`) do if '.%%i.'=='.LocalDateTime.' set ldt=%%j
set ldt=%ldt:~0,4%-%ldt:~4,2%-%ldt:~6,2%_%ldt:~8,2%h%ldt:~10,2%m%ldt:~12,2%s
REM echo Local date is [%ldt%]

IF EXIST G:\NUL GOTO :USE_G
goto :eof

:USE_G
sqlcmd -S DULRICH-XPV -i "D:\MultiAxesGraph\GetDataLog.sql" -o "G:\GraphData_%ldt%.csv" -s, -W