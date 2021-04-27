from pytube import YouTube

# Enter YouTube URL
url = input('YouTube URL')
yt = YouTube(url)

# Show details
print('Title: ',yt.title)
print('Number of views: ',yt.views)
print('Length of video: ',yt.length)
print('Rating of video: ',yt.rating)

# Get the highest resolution possible
ys = yt.streams.get_highest_resolution()

# Start download
print('Downloading...')
ys.download()
print('Download completed!!')


