#!/usr/bin/env python

import sys
import requests
import unicodecsv as csv

from models.album import bandPage

BANDCAMP_URL_END = '.bandcamp.com/music'

def scrape_album(band):
    with open('cache/albums.csv', 'wb') as f:
        writer = csv.writer(f)
        url = 'https://' + band + BANDCAMP_URL_END
        response = requests.get(url)
        if response:
            page = bandPage(response.content)

            for item in page.items:
                writer.writerow([item])

        else:
            print('Could not find that band, sorry.')





if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('band name required')
        sys.exit()

    band = str(sys.argv[1])
    scrape_album(band=band)
