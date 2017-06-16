#!/usr/bin/env python

import sys
import requests
import unicodecsv as csv
import json
from flask import flash, redirect

#import models
from models.band import bandPage
from models.album import albumPage

#use generated urls for album pages to scrape album and song info
def scrape_albums(page, band_url):
    with open('static/json/albums.json', 'wb') as albumJSON:
        all_albums = []
        for album_ext in page.albums:
            url = band_url + album_ext
            response = requests.get(url)
            if response:
                album = albumPage(response.content)
                songs = []
                for song in album.songs:
                    song_dict = {'songTitle': song.title, 'songLength': song.length}
                    songs.append(song_dict)
                album_dict = {'albumTitle': album.title, 'release': album.release, 'artistName': album.artist, 'songs': songs}
                all_albums.append(album_dict)
        try:
            json.dump(all_albums, albumJSON, indent=4, sort_keys=True)

        except:
            flash('Something went wrong...')
            return redirect('/')



#scrape band's page for urls to individual album pages
def scrape_index(band_url):
    if band_url.endswith('/'):
        url = band_url + 'music'
    else:
        url = band_url + '/music'
    try:
        response = requests.get(url)
        if response:
            page = bandPage(response.content)
            if page.albums == []:
                page.albums = ['/releases']
            scrape_albums(page, band_url)
        else:
            flash('Sorry, that url does not seem to exist.')
            return redirect('/')
    except requests.exceptions.MissingSchema:
        flash('Sorry, that url does not seem to exist.')
        return redirect('/')





# # runs app when provided bandcamp url
# if __name__ == '__main__':
#     if len(sys.argv) == 1:
#         print('bandcamp url required')
#         sys.exit()
#
#     band_url = str(sys.argv[1])
#     scrape_index(band_url)
