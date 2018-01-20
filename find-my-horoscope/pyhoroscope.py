#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ashokramcse
"""
from pyhoroscopicdp import ServerResponse as _sr
from pyhoroscopicdp import HoroscopeStaticDataProvider as _hsdp
from pyhoroscopicdp import DataProviderCleanup as _dpc


class Horoscope:

    @staticmethod
    def get_todays_horoscope(sunsign):
        url = _hsdp.TODAY_ENDPOINT + sunsign
        tree = _sr.get_server_response(url)
        date = str(tree.xpath(_hsdp.RANGE_X_PATH))
        date = _dpc.noice_cleanup(date)
        horoscope = str(tree.xpath(_hsdp.HOROSCOPE_X_PATH))
        horoscope = _dpc.noice_cleanup(horoscope)

        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_weekly_horoscope(sunsign):
        url = _hsdp.WEEKLY_ENDPOINT + sunsign
        tree = _sr.get_server_response(url)
        week = str(tree.xpath(_hsdp.RANGE_X_PATH))
        week = _dpc.noice_cleanup(week)
        horoscope = str(tree.xpath(_hsdp.HOROSCOPE_X_PATH))
        horoscope = _dpc.noice_cleanup(horoscope)

        dict = {
            'week': week,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_monthly_horoscope(sunsign):
        url = _hsdp.MONTHLY_ENDPOINT + sunsign
        tree = _sr.get_server_response(url)
        month = str(tree.xpath(_hsdp.RANGE_X_PATH))
        month = _dpc.noice_cleanup(month)
        horoscope = str(tree.xpath(_hsdp.HOROSCOPE_X_PATH + "[1]"))
        horoscope = _dpc.noice_cleanup(horoscope)

        dict = {
            'month': month,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_yearly_horoscope(sunsign):
        url = _hsdp.YEARLY_ENDPOINT + sunsign
        tree = _sr.get_server_response(url)
        year = str(tree.xpath(_hsdp.RANGE_X_PATH))
        year = _dpc.noice_cleanup(year)
        horoscope = str(tree.xpath(_hsdp.HOROSCOPE_X_PATH))
        horoscope = _dpc.noice_cleanup(horoscope)

        dict = {
            'year': year,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict
