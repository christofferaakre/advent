from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

import requests
from credentials import cookies

ap = ArgumentParser(description=__doc__,
                    formatter_class=RawDescriptionHelpFormatter)

ap.add_argument('days', type=str, help="Days to get data for")

args = ap.parse_args()

days = args.days.split(',')

for day in days:
    url = f'https://adventofcode.com/2018/day/{day}/input'
    data = requests.get(url, cookies=cookies).text
    f = open(f'inputs/input{day}', 'w')
    f.write(data)
    f.close()
