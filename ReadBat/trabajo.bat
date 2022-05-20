@echo off
cls
:menu
cls
color 80

date /t

echo Computador: %computername%        Usuario: %username%
                   
echo            MENU 
echo  ==================================
echo * 1. Parte 1                       * 
echo * 2. Parte 2                       *
echo * 3. Parte 3                       *
echo * 4. Parte 4                       *
echo * 5. Salir                         * 
echo  ==================================

set /p opcion= Numero: 
echo ------------------------------
if %opcion% equ 1 goto opcion1
if %opcion% equ 2 goto opcion2
if %opcion% equ 3 goto opcion3
if %opcion% equ 4 goto opcion4
if %opcion% equ 5 goto opcion5


:opcion1
cls
FOR /F "tokens=* delims=" %%x in (part1.txt) DO echo %%x
pause
goto menu

:opcion2
cls
FOR /F "tokens=* delims=" %%x in (part2.txt) DO echo %%x
pause
goto menu

:opcion3
cls
FOR /F "tokens=* delims=" %%x in (part3.txt) DO echo %%x
pause
goto menu

:opcion4
cls
FOR /F "tokens=* delims=" %%x in (part4.txt) DO echo %%x
pause
goto menu

:opcion5
cls
exit

