from pytube import Channel, YouTube
import re
import os

def download_youtube_shorts(channel_url, download_path='downloads'):
    # Create download directory if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    # Fetch the channel object
    channel = Channel(channel_url)
    
    # Regular expression to match YouTube Shorts URLs
    shorts_pattern = re.compile(r'/shorts/')

    for video_url in channel.video_urls:
        if shorts_pattern.search(video_url):
            try:
                # Create YouTube object
                yt = YouTube(video_url)
                
                # Select the highest resolution stream available
                video_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                
                # Download the video
                print(f"Downloading: {yt.title}")
                video_stream.download(output_path=download_path)
                print(f"Downloaded: {yt.title}")
            except Exception as e:
                print(f"Failed to download {video_url}: {e}")

if __name__ == "__main__":
    channel_url = input("Enter the YouTube channel URL: ")
    download_youtube_shorts(channel_url)
