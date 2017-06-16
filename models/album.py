from bs4 import BeautifulSoup

#structure for album object
class albumPage:
    def __init__(self, html):
        self._html = html
        self._soup = BeautifulSoup(self._html, 'html.parser')
        self.songs = []
        self._parse()

    def _parse(self):
        song_list = self._soup.find_all('tr', class_='track_row_view')
        for row in song_list:
            song = songItem(row)
            if song.length:
                self.songs.append(song)

    @property
    def title(self):
        title_section = self._soup.find(id='name-section')
        return title_section.find('h2').string.strip()

    @property
    def artist(self):
        title_section = self._soup.find(id='name-section')
        h3 = title_section.find('h3')
        span = h3.find('span')
        return span.find('a').string.strip()

    @property
    def release(self):
        release_date = self._soup.find(attrs={"itemprop": "datePublished"})
        return release_date['content']

    # RETURNS SPAN WITH NO INNER HTML, DESPIT CONTENT BEING VISIBLE ON PAGE????
    # @property
    # def titleTrackLength(self):
    #     time_span = self._soup.find(attrs={'class':'time_total'})
    #     print time_span
    #     return time_span


#structure for song object in album
class songItem:
    def __init__(self, row):
        self._row = row

    @property
    def title(self):
        title_col = self._row.find('td', class_='title-col')
        title_div = title_col.find('div')
        return title_div.find('span', attrs={"itemprop": "name"}).string.strip()

    @property
    def length(self):
        title_col = self._row.find('td', class_='title-col')
        title_div = title_col.find('div')
        time_span = title_div.find('span', attrs={"class": "time"})
        if time_span:
            return time_span.string.strip()
