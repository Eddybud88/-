from bs4 import BeautifulSoup


def extract_songs(html):
    soup = BeautifulSoup(html, 'html.parser')

    song_list = soup.find('ul', {'id': 'list'}).find_all('li')

    songs_dict = {}

    for song in song_list:
        link = song.find('a')
        if link:
            singer = link.get('singer', '')
            title = link.string
        else:
            title = song.get_text()
            singer = ''

        songs_dict[title] = singer

    return songs_dict


html = '''
<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>
'''

songs = extract_songs(html)
for title, singer in songs.items():
    print(f'{title} - {singer or "未知"}')