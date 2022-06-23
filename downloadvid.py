from pytube import YouTube

video = input("Enter the video link: ")

yt = YouTube(video)

print("Title", yt.title)
print("Number Of Views", yt.views)
print("Length Of Video", yt.length)
print("Rating Of Video", yt.rating)

ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download()
print("Download Complete")