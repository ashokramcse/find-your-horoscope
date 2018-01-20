#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ashokramcse
"""
import urllib.request
from lxml import etree

class HoroscopeStaticDataProvider(object) :

    TODAY_ENDPOINT="http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/"
    WEEKLY_ENDPOINT="http://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/"
    MONTHLY_ENDPOINT="http://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/"
    YEARLY_ENDPOINT="http://www.ganeshaspeaks.com/horoscopes/yearly-horoscope/"

    RANGE_X_PATH="//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"

    HOROSCOPE_X_PATH="//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"

class DataProviderCleanup (object) :
    
    def noice_cleanup (data) :
        data = data.replace("['(", "").replace(")']", "").replace("['\\n", "").replace("']", "").replace("\\u2013", "-").replace("[u'", "").replace("\\xe2\\x80\\x99s", "").replace("\\n", "").strip()
        return data
    
class ServerResponse (object) :

    @staticmethod
    def get_server_response(url):
        response = urllib.request.urlopen(url)
        htmlparser = etree.HTMLParser()
        return etree.parse(response, htmlparser)