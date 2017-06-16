from bs4 import BeautifulSoup

#structure for bandpage object
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

class searchPage:
    def __init__(self, html):
        self._html = html
        self._soup = BeautifulSoup(self._html, 'html.parser')
        self._parse()

    def _parse(self):
        band_result = self._soup.find('li', class_='searchresult band')
        result_info = band_result.find('div', class_='result-info')
        item_url = result_info.find('div', class_='itemurl')
        self.url = item_url.find('a').get_text()
