# find-your-horoscope

A Python module to fetch and parse data from GaneshaSpeaks.

## Installation
* You will need [Python 2](https://www.python.org/download/) or [Python 3](https://www.python.org/download/).

## Usage

```python

from pyhoroscope import Horoscope as _hor

your_todays_horoscope = _hor.get_todays_horoscope('stagittarius')
    
print(your_todays_horoscope)

print (your_todays_horoscope['date'])
print (your_todays_horoscope['sunsign'])
print (your_todays_horoscope['horoscope'])

```
