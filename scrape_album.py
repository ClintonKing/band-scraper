#!/usr/bin/env python

import sys
import requests
import unicodecsv as csv

from models.band import bandPage
from models.album import albumPage


def scrape_album(album_ext):
    url = BASE_URL + album_ext
    response = requests.get(url)
    if response:
        album = albumPage(response.content)
        print(album.artist)



def scrape_index():
    url = BASE_URL + '/music'
    response = requests.get(url)
    if response:
        page = bandPage(response.content)

        for album_ext in page.albums:
            scrape_album(album_ext)


    else:
        print('Could not find that band, sorry.')





if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('band name required')
        sys.exit()

    band = str(sys.argv[1])
    global BASE_URL
    BASE_URL = 'https://' + band + '.bandcamp.com'
    scrape_index()
