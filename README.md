# Tenders in Russia Micro-Service

A Python app for scraping tenders, storing them and sharing them via REST API

## Technologies used

1. Python 3.13.5
2. Docker
3. Linux (Ubuntu 22)
4. Sqlite3
5. FastAPI
6. Selenium
7. Swagger

## Instruction

1. one
2. How To
   1. Run Server
      1. `python3 main.py`
   2. Scrape Tenders
      1. `python3 main.py scrape`
   3. Print 100 tenders
      1. `python3 main.py --max 100`
   4. Export 100 tenders to CSV
      1. `python3 main.py --max 100 --output tenders.csv`
