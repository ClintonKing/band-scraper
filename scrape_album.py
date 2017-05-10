#!/usr/bin/env python

import sys
import requests
import unicodecsv as csv

#import models
from models.band import bandPage
from models.album import albumPage

#use generated urls for album pages to scrape album and song info
def scrape_albums(page):
    all_albums = []
    for album_ext in page.albums:
        url = BAND_URL + album_ext
        response = requests.get(url)
        if response:
            album = albumPage(response.content)
            all_albums.append(album)
    for album in all_albums:
        print(album.title)



#scrape band's page for urls to individual album pages
def scrape_index():
    url = BAND_URL
    try:
        response = requests.get(url)
        page = bandPage(response.content)
        scrape_albums(page)
    except requests.exceptions.MissingSchema:
        print('Sorry, that url does not seem to exist.')





#runs app when provided bandcamp url
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('bandcamp url required')
        sys.exit()

    global BAND_URL
    BAND_URL = str(sys.argv[1])
    scrape_index()
