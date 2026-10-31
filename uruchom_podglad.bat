@echo off
title Tajlandia 2027 - Podglad Aplikacji
echo ============================================================
echo   🌴 TAJLANDIA 2027 - INTERAKTYWNA APLIKACJA PWA
echo ============================================================
echo.
echo Uruchamianie lokalnego serwera na porcie 8080...
echo Otwieranie aplikacji w Twojej domyslnej przegladarce...
echo.
start http://localhost:8080/index.html
echo.
echo ------------------------------------------------------------
echo Aby miec aplikacje na telefonie:
echo 1. Polacz telefon z tym samym Wi-Fi.
echo 2. Wpisz w Safari na iPhone adres swojego komputera:
echo    http://[IP_KOMPUTERA]:8080
echo 3. Kliknij Udostepnij (⬆️) -> "Do ekranu poczatkowego".
echo ------------------------------------------------------------
echo.
echo Aby zatrzymac serwer, zamknij to okno konsoli.
echo.
python -m http.server 8080 --directory "%~dp0"
pause
