#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ashokramcse
"""

from pyhoroscope import Horoscope as _hor

your_todays_horoscope = _hor.get_todays_horoscope('stagittarius')

print(your_todays_horoscope)

print("\n")
print (your_todays_horoscope['date'])
print (your_todays_horoscope['sunsign'])
print (your_todays_horoscope['horoscope'])

print("\n")
print(_hor.get_weekly_horoscope('stagittarius'))

print("\n")
print(_hor.get_monthly_horoscope('stagittarius'))

print("\n")
print(_hor.get_yearly_horoscope('stagittarius'))
