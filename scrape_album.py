#!/usr/bin/env python

import sys
import requests
import unicodecsv as csv
import json

#import models
from models.band import bandPage
from models.album import albumPage

#use generated urls for album pages to scrape album and song info
def scrape_albums(page, band_url):
    with open('cache/albums.json', 'wb') as albumJSON:
        all_albums = []
        for album_ext in page.albums:
            url = band_url + album_ext
            response = requests.get(url)
            if response:
                album = albumPage(response.content)
                songs = []
                for song in album.songs:
                    song_dict = {'songTitle': song.title, 'length': song.length}
                    songs.append(song_dict)
                album_dict = {'albumTitle': album.title, 'release': album.release, 'artistName': album.artist, 'songs': songs}
                all_albums.append(album_dict)
        try:
            json.dump(all_albums, albumJSON, indent=4, sort_keys=True)
            print('Done!')
        except:
            print('Something went wrong...')



#scrape band's page for urls to individual album pages
def scrape_index(band_url):
    url = band_url + '/music'
    try:
        response = requests.get(url)
        page = bandPage(response.content)
        scrape_albums(page, band_url)
    except requests.exceptions.MissingSchema:
        print('Sorry, that url does not seem to exist.')





#runs app when provided bandcamp url
# if __name__ == '__main__':
#     if len(sys.argv) == 1:
#         print('bandcamp url required')
#         sys.exit()
#
#     band_url = str(sys.argv[1])
#     scrape_index(band_url)
