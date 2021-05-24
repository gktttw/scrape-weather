# scrape-weather

install virtualenv
cd into the directory
`virtualenv env`

`pip3 install -r requirements.txt`

`source env/bin/activate`

first time init db:
`cd cwb`
`python3 init_db.py`

then do the scrape:
make sure you are in the first cwb directory
`cd cwb`
`scrapy crawl cwb`
