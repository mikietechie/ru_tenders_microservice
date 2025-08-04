# Tenders in Russia Micro-Service

A Python app for scraping tenders, storing them and sharing them via REST API.

## Technologies used

1. Python 3.13.5
2. Docker
3. Linux (Ubuntu 22)
4. Sqlite3
5. FastAPI
6. Selenium
7. Swagger

## Instruction

1. `git clone https://github.com/mikietechie/ru_tenders_microservice`
2. How Tos
   1. Setup environment
      1. Use Python 3.13.5 preferebly on Ubuntu
      2. `cd ru_tenders_microservice`
      3. `python3 -m venv env`
      4. `source env/bin/activate`
      5. `pip install -r requirements.txt`
      6. `cd src`
      7. Maybe setup environment variables in a *.env* file
   2. Run Server
      - `python3 main.py`
   3. Scrape Tenders
      - `python3 main.py scrape`
   4. Print 100 tenders
      - `python3 main.py --max 100`
   5. Export 100 tenders to CSV
      - `python3 main.py --max 100 --output tenders.csv`

## Future Work

1. Add Security
2. Add logging
3. Use Docker
4. Add Tests
5. Use Chromeserver
