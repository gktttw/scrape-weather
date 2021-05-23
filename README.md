# scrape-weather

install virtualenv

`source env/bin/activate`

first time init db:
`cd cwb`
`python3 init_db.py`

then do the scrape:
make sure you are in the first cwb directory
`cd cwb`
`scrapy crawl cwb`
