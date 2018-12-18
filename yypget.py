import requests
from bs4 import BeautifulSoup

def main():
    video_url = 'https://sv.baidu.com/videoui/page/videoland?pd=bjh&context=\
    {%22nid%22:%224949783038993399443%22,%22sourceFrom%22:%22bjh%22}&fr=bjha\
    uthor&type=video'

    r = requests.get(video_url)
    print('status_code:', r.status_code)

    soup = BeautifulSoup(r.text, features = "html.parser")
    video_real_url = soup.find(id = "main-player")
    print(video_real_url.video.source.attrs['src'])

    # download video
    video_real_url_str = video_real_url.video.source.attrs['src']
    video_r = requests.get(video_real_url_str, stream = True)

    with open("video.mp4", "wb") as mp4:
        for chunk in video_r.iter_content(chunk_size = 1024 * 1024):
            if chunk:
                mp4.write(chunk)

    print('download done')

if __name__ == '__main__':
    main()
