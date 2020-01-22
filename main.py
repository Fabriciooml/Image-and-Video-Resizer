import PIL
from PIL import Image
import moviepy.editor as mp

def UserInteract():
    while True:
        typeOfArchive = input("It's a video or an image? (video/image)")
        location = input("Please, insert the name of it with extension. (example.jpeg)")
        size = input("Please, insert the size you want. (1920 X 1080)")
        if(typeOfArchive == "image"):
            ResizeImage(location, size)
            break
        elif(typeOfArchive == "video"):
            ResizeVideo(location, size)
            break
        else:
            print("Please, image or video.")

def ResizeImage(location, size):
    img = Image.open(location)
    width, height = GetHeightWidth(size)
    imgResized = img.resize((width, height), Image.ANTIALIAS)
    imgResized.save('resizedImage.jpg')

def ResizeVideo(location, size):
    video = mp.VideoFileClip(location)
    width, height = GetHeightWidth(size)
    videoResized = video.resize(height = height, width = width)
    videoResized.write_videofile("video_resized.mp4")

def GetHeightWidth(size):
    sizeVector = size.split("X")
    sizeVector[0] = int(sizeVector[0])
    sizeVector[1] = int(sizeVector[1])
    return sizeVector

UserInteract()