import datetime
import log
import time

from zadanie08_funkcje import policz_linie, policz_wyrazy, policz_bajty

start = datetime.datetime.now()

format = '%(levelname)s [%(asctime)s] - %(message)s'


log.basicConfig(level=log.DEBUG, format=format)
nazwa_pliku = 'zen.txt'

try:
    with open(nazwa_pliku) as f:
        zawartosc = f.read()
        log.info(f'otwarto plik {nazwa_pliku}')
except FileNotFoundError:
    log.error(f'przerwanie pracy programu')
    exit()

szablony = {'pelny': '{linie} {wyrazy} {bajty} {nazwa_pliku}',
            'linie': '{linie} {nazwa_pliku}'}

rodzaj_szablonu = 'pelny'
szablon = szablony[rodzaj_szablonu]


log.info(f'wybrany rodzaj komunikatu: {rodzaj_szablonu}')

wynik_pelny = szablon.format(linie=policz_linie(zawartosc),
                             wyrazy=policz_wyrazy(zawartosc),
                             bajty=policz_bajty(zawartosc),
                             nazwa_pliku=nazwa_pliku)
time.sleep(2)
czas_od_startu = datetime.datetime.now() - start
log.debug(f'czas wykonania skryptu: {czas_od_startu}')
print(wynik_pelny)
