from bs4 import BeautifulSoup

class bandPage:
    def __init__(self, html):
        self._html = html
        self._soup = BeautifulSoup(self._html, 'html.parser')
        self.albums = []
        self._parse()

    def _parse(self):
        album_grid = self._soup.find_all('li', class_='music-grid-item')
        for album in album_grid:
            album_ext = album.find('a')
            if album_ext:
                href = album_ext.get('href')
                self.albums.append(href)
