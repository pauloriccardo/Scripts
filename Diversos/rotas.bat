@echo off
REM Script Para Adicionar e Remover Rotas
REM Criado Por: Paulo Celestino
REM Data: 24/07/2019
REM Versão: 1.0
REM Script: Rotas.bat

REM 0 = Black       8 = Gray
REM 1 = Blue        9 = Light Blue
REM 2 = Green       A = Light Green
REM 3 = Aqua        B = Light Aqua
REM 4 = Red         C = Light Red
REM 5 = Purple      D = Light Purple
REM 6 = Yellow      E = Light Yellow
REM 7 = White       F = Bright White

:MENU

color 1f

echo     =========================================================================
echo.
echo                   SCRIPT PARA ADICIONAR E REMOVER ROTAS
echo.
echo                               OUTLOOK/SKYPE
echo.
echo     =========================================================================
echo.
echo.

echo         1 - Adicionar Rotas
echo         2 - Remover Rotas
echo         3 - Verificar Rotas
echo         4 - Sair
echo.
echo.

CHOICE /C:1234 /M "Selecione uma opcao:"
IF ERRORLEVEL 1 SET M=1
IF ERRORLEVEL 2 SET M=2
IF ERRORLEVEL 3 SET M=3
IF ERRORLEVEL 4 SET M=4


IF %M%==1 GOTO ADD
IF %M%==2 GOTO RMV
IF %M%==3 GOTO PRT
IF %M%==4 GOTO SAIR



:ADD
cls
echo     ==============================================================
echo				Adicionando Rotas
echo     ==============================================================
echo.

route add 148.80.254.190 mask 255.255.255.255 192.168.1.1
route add 52.0.0.0 mask 255.0.0.0 192.168.1.1
route add 40.0.0.0 mask 255.0.0.0 192.168.1.1
route add 13.0.0.0 mask 255.0.0.0 192.168.1.1
route add 31.13.0.0 mask 255.255.0.0 192.168.1.1
echo.

pause

cls
GOTO MENU

:RMV
cls
echo     ==============================================================
echo				Removendo Rotas
echo     ==============================================================
echo.

route delete 148.80.254.190 mask 255.255.255.255 192.168.1.1
route delete 52.0.0.0 mask 255.0.0.0 192.168.1.1
route delete 40.0.0.0 mask 255.0.0.0 192.168.1.1
route delete 13.0.0.0 mask 255.0.0.0 192.168.1.1
route delete 31.13.0.0 mask 255.255.0.0 192.168.1.1
echo.

pause

cls
GOTO MENU

:PRT
cls
echo     ==============================================================
echo				Verificando Rotas
echo     ==============================================================
echo.
route print
echo.

pause

cls
GOTO MENU

:SAIR
echo.
pause

exit

