from bs4 import BeautifulSoup

class bandPage:
    def __init__(self, html):
        self._html = html
        self._soup = BeautifulSoup(self._html, 'html.parser')
        self.items = []
        self._parse()

    def _parse(self):
        albums = self._soup.find_all('li', class_='music-grid-item')
        for album in albums:
            link = album.find('a')
            if link:
                href = link.get('href')
                self.items.append(href)
