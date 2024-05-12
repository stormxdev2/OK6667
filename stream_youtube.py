import streamlink
import subprocess

# Video ID of the YouTube video to stream
video_id = "-p5NXiuZydw"

# RTMP URLs provided by YouTube
stream_url = "rtmp://x.rtmp.youtube.com/live2"
backup_url = "rtmp://y.rtmp.youtube.com/live2?backup=1"

def get_best_stream_url(video_url):
    # Fetch available streams for the given YouTube video URL
    streams = streamlink.streams(video_url)
    if 'best' in streams:
        return streams['best'].url
    return None

def stream_youtube(video_id, primary_url, backup_url):
    # Construct the YouTube video URL
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    # Get the best available stream URL using streamlink
    stream_url = get_best_stream_url(video_url)
    if not stream_url:
        print("Failed to get the stream URL.")
        return

    print(f"Streaming from: {stream_url}")

    # Use ffmpeg to stream to the primary RTMP server URL with a backup option
    ffmpeg_cmd = [
        "ffmpeg", "-i", stream_url, "-c", "copy", "-f", "flv",
        f"{primary_url}/{video_id}",
        f"{backup_url}/{video_id}"
    ]

    # Start streaming using ffmpeg
    subprocess.run(ffmpeg_cmd)

if __name__ == "__main__":
    stream_youtube(video_id, stream_url, backup_url)
