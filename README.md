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
   1. Work in docker
      1. `cd ru_tenders_microservice`
      2. `docker compose -f 'docker-compose.yml' up -d --build`
   2. Setup environment
      1. Use Python 3.13.5 preferebly on Ubuntu
      2. `cd ru_tenders_microservice`
      3. `python3 -m venv env`
      4. `source env/bin/activate`
      5. `pip install -r requirements.txt`
      6. `cd src`
      7. Maybe setup environment variables in a _.env_ file
   3. Run Server
      - `python3 main.py`
   4. Scrape Tenders
      - `python3 main.py scrape`
   5. Print 100 tenders
      - `python3 main.py --max 100`
   6. Export 100 tenders to CSV
      - `python3 main.py --max 100 --output tenders.csv`

## Future Work

1. Add Security
2. Add logging
3. Add Tests
4. Use Chromeserver
