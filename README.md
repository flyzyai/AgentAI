
# Flyzy - AI Wyszukiwarka Lotów

Aplikacja webowa do wyszukiwania tanich lotów za pomocą AI (ChatGPT) i FastAPI.

## Instalacja lokalna

1. Zainstaluj wymagane biblioteki:
```
pip install -r requirements.txt
```

2. Stwórz plik `.env` i wstaw swój klucz API:
```
OPENAI_API_KEY=YOUR_API_KEY_HERE
```

3. Uruchom aplikację lokalnie:
```
uvicorn app.main:app --reload
```

Otwórz w przeglądarce: [http://localhost:8000](http://localhost:8000)

## Hosting na Render

1. Stwórz nowe repozytorium na GitHub i wrzuć pliki.
2. Przejdź do [Render](https://render.com) i stwórz nową usługę **Web Service**.
3. Wskaż repozytorium GitHub.
4. Wybierz build command: `pip install -r requirements.txt`
5. Wybierz start command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
6. Ustaw zmienną środowiskową: `OPENAI_API_KEY`

Gotowe!

---
Autor: ChatGPT & Flyzy Team
