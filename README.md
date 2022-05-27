# Instrukcja obsługi aplikacji API


## Uruchamianie serwera API 🚀

0. Jeśli używasz venva, aktywuj venva wpisując w terminalu komendę:
`[ścieżka do folderu venv]\Scripts\activate`

1. Zainstaluj potrzebne biblioteki zawarte w pliku ***python_server_backend\app\requirements.txt*** za pomocą polecenia:
`pip install -r [ścieżka do pliku requirements.txt]`

2. W terminalu przejdź do folderu głównego aplikacji ***Rasberek***

3. Uruchom serwer API, za pomocą polecenia:
`uvicorn python_server_backend.app.api:app`.
Jeśli chcesz, żeby serwer automatycznie się odświeżał po wprowadzeniu zmian w kodzie, dodaj flagę `--reload`:
`uvicorn python_server_backend.app.api:app --reload`

4. Żeby przejść do webowego GUI serwisu API, wpisz w przeglądarce:
http://localhost:8000/docs


## Struktura folderów 📁

### API: `python_server_backend\app`:

- `routers\` - folder z "ruterami" endpointów dla poszczególnych czujników (ruter, czyli grupa endpointów wykorzystujących np. ten sam url, dzieląca ustawienia itp). Tutaj są zdefiniowane funkcje wykonywane po wpisaniu konkretnego URLa w przeglądarce np.
- `sql_app\schemas\` - zbiór modelów biblioteki pydantic wykorzystywane w    fastapi do wysyłania i odbierania danych w konkretnym formacie (np. sposród danych użytkownika, chcemy odczytać tylko imię i email, ale nie hasło)
- `sql_app\database.py` - skrypt tworzący lub otwierający bazę danych (jeśli już istnieje + przechowuje zmienną silnika SQLAlchemy, instancję sesji i bazową instancję obiektu
- `sql_app\models.py` - modele mapujące tablice bazy danych na "obiekty", które wykorzystuje sqlalchemy
- `api.py` - główny skrypt uruchamiający aplikację
- `constants.py` - stałe globalne (scieżka __ROOT__ - " \python_server_backend\")
- `dependencies.py` - powtarzające się funkcje zależności wykorzystywane przez fastapi
- `hashing.py` - funkcje związane z haszowaniem w fastapi
- `login.py` - funkcje i endpointy związane z logowaniem? (ale nie wiem czy wgl je teraz wykorzystuję... chyba jeszcze nie)
- `requirements.txt` - lista bilbiotek wymaganych do uruchomienia aplikacji
- `authentication.py` - wszelkie funkcje na potrzeby logowania/autoryzacji/haszowania i dekodowania haseł

### Baza danych: `python_server_backend\sqlite_db`:
- `database.db` - plik bazy danych sqlite3
- `database_setup.py` - skrypt tworzący bazę i tabele
- `sqlite_operations.py` - listy z poleceniami sql wykorzystywanymi do tworzenia bazy (np. **CREATE TABLE**)

### Skrypty do obsługi czujników: `python_server_backend\???`:
- TODO :)

## A działa to tak:

Uruchamiamy serwer poleceniem `uvicorn`, które wywołuje skrypt z pliku `api.py`, który robi kilka rzeczy:
   - importuje, a więc wykonuje skrypty z folderu `routers`, które definiują funkcje przypisane do konkretnych adresów 
   URL - takie zbiory metod nazywa się tu *ruterami*
   - importuje plik `models.py` z `sql_app`, który tworzy instancje klas mapujących tabele bazy danych SQL do bardziej 
   pythonowego formatu
   - wykonuje plik `sql_app.database` i importuje tworzoną tam instancję `engine` - tj. silnika SQLAlchemy wykorzystywanego
    do operowania na bazie
   - wywoływany jest skrypt z pliku `sqlite_db\database_setup.py`, który tworzy bazę jeśli baza nie istnieje
   - zaimportowane wcześniej modele są *bindowane* do instancji silnika
   - tworzona jest instancja aplikacji FastAPI: `app = FastAPI()`
   - do `app` dowiązywane są rutery z zdefiniowanymi funkcjami dla konkretnych adresów URL
