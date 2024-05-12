import subprocess

def stream_youtube(video_id, stream_url, backup_url):
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    subprocess.run(['youtube-dl', '-f', 'best', video_url])

if __name__ == '__main__':
    video_id = '-p5NXiuZydw'
    stream_url = 'rtmp://x.rtmp.youtube.com/live2'
    backup_url = 'rtmp://y.rtmp.youtube.com/live2?backup=1'
    stream_youtube(video_id, stream_url, backup_url)
