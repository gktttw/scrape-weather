import scrapy
import sqlite3 as sl

class CWBSpider(scrapy.Spider):
    name = 'cwb'

    # it's the ajax call within "https://www.cwb.gov.tw/V8/C/W/week.html"
    start_urls = [
        'https://www.cwb.gov.tw/V8/C/W/County/MOD/wf7dayNC_NCSEI/ALL_Week.html'
    ]

    def parse(self, response):
        con = sl.connect('cwb.db')

        sql = "INSERT INTO WEATHER (city_name, date, time, temperature, status) VALUES(?, ?, ?, ?, ?)"
        insert_to_db = []

        for city in response.css('div.panel'):
            city_name = city.css('a::text').get()

            for date_time in city.css('div.panel-collapse')[0].css('ul'):
                date = date_time.css('li.date span::text')[0].get()
                # day
                time = 'Day'
                temp = date_time.css('li.Day')[0].css('span.tem-C::text').get().replace('\u2002', '')
                status = date_time.css('li.Day')[0].css('img').xpath('@alt').get()
                insert_to_db.append([city_name, date, time, temp, status])

                # night
                time = 'Night'
                temp = date_time.css('li.Night')[0].css('span.tem-C::text').get().replace('\u2002', '')
                status = date_time.css('li.Night')[0].css('img').xpath('@alt').get()
                insert_to_db.append((city_name, date, time, temp, status))

        with con:
            con.executemany(sql, insert_to_db)
