from pytube import YouTube, Playlist
import sys, os
import pathlib


# youtube vid down function
def vid_dwon():
    url = input("please enter the video link: ")
    vid_url = YouTube(url)
    print("*****************")
    print(vid_url.title)
    print("*****************")
    print("Downloading the highest quality")
    print("*****************")
    # downloading path
    if not os.path.exists('videos'):
        os.makedirs('videos')
    try:
        vid_url.streams.filter(res="720p").first().download(f'{path}/videos/')
        print("finish!")
        loop()
    except:
        print("download failed!")


# playlist down function
def play_dwon():
    play_url = input("please enter the playlist link: ")
    playlist = Playlist(play_url)
    print("*****************")
    print(f"{playlist.title}:")
    for tit in playlist.video_urls:
        print(tit)
    print("*****************")
    print("Downloading the playlist with the highest quality")
    print("*****************")
    # downloading path
    if not os.path.exists('playlist'):
        os.makedirs('playlist')
    try:
        # extract the playlist to videos and then download the videos
        for url in playlist.video_urls:
            url = YouTube(url)
            url.streams.filter(res="720p").first().download(f'{path}/playlist/')
            print("finish!")
        loop()
    except:
        print("download failed!")


# playlist_audio down function
def Mplay_dwon():
    Mplay_url = input("please enter the playlist link: ")
    Mplaylist = Playlist(Mplay_url)
    print("*****************")
    print(f"{Mplaylist.title}:")
    for tit in Mplaylist.video_urls:
        print(tit)
    print("*****************")
    print("Downloading the playlist with the highest quality")
    print("*****************")
    # downloading path
    if not os.path.exists('playlist(audio)'):
        os.makedirs('playlist(audio)')
    try:
        # extract the playlist to videos and then download the videos
        for url in Mplaylist.video_urls:
            url = YouTube(url)
            url.streams.filter(res="720p").first().download(f'{path}/playlist(audio)/')
            for filename in os.listdir(f"{path}/playlist(audio)/"):
                infilename = os.path.join(f"{path}/playlist(audio)/", filename)
                oldbase = os.path.splitext(filename)
                newname = infilename.replace('.mp4', '.mp3')
                output = os.rename(infilename, newname)
            print("finish!")
        loop()
    except:
        print("download failed!")


# audio down function
def audio_down():
    aud_url = input("please enter the video link: ")
    audio = YouTube(aud_url)
    print("*****************")
    print(audio.title)
    name = audio.title
    print("*****************")
    print("Downloading the audio with highest quality")
    print("*****************")
    # downloading path
    try:
        os.makedirs(f"{path}\music")
    except FileExistsError:
        # directory already exists
        pass
    try:
        audio.streams.filter(only_audio=True).first().download(f"{path}/audio/")
        # searching for the file and then changing her extension
        for filename in os.listdir(f"{path}/audio/"):
            infilename = os.path.join(f"{path}/audio/", filename)
            oldbase = os.path.splitext(filename)
            newname = infilename.replace('.mp4', '.mp3')
            output = os.rename(infilename, newname)
        print("finish!")
        loop()
    except:
        print("download failed!")


def subtitle():
    sub_url = input("please enter the video link: ")
    cap_option = input("choose the subtitle language please(e.g: ar/en/de...): ")
    sub = YouTube(sub_url)
    try:
        caption = sub.captions[cap_option]
        print("*****************")
        print(sub.title)
        print("*****************")
        print(caption.generate_srt_captions())
        loop()
    except:
        print("error, please try again!")


def loop():
    choice = ""

    while choice != "y" and choice != "n":
        choice = input("Do you want do continue ? (y/n): ")

    if choice == "y":
        # here the user will choose video or playlist or audio
        choice2 = ""
        while choice2 != "1" and choice2 != "2" and choice2 != "3" and choice2 != "4" and choice2 != "5":
            choice2 = input(
                "do you want to download a video or audio or playlist or audio_playlist or subtitle tracker ("
                "1/2/3/4/5): ")
        if choice2 == "1":
            # download path
            path = input("enter please your path: ")
            vid_dwon()
        elif choice2 == "2":
            path = input("enter please your path: ")
            audio_down()
        elif choice2 == "3":
            path = input("enter please your path: ")
            play_dwon()
        elif choice2 == "4":
            path = input("enter please your path: ")
            Mplay_dwon()
        elif choice2 == "5":
            subtitle()

# let's display our program intro
print(
    "Welcome to DownTube, where you can download Youtube videos as mp4 or mp3 or a playlist(videos or audio) and you "
    "can track the caption/subtitle.\n"
    "It's the beta version, we will try our best to make it better in the future ^^.")

# this var is the choice of the user if he want's to continue or not
choice = ""

while choice != "y" and choice != "n":
    choice = input("Do you want do continue ? (y/n): ")

if choice == "y":
    # here the user will choose video or playlist or audio
    choice2 = ""
    while choice2 != "1" and choice2 != "2" and choice2 != "3" and choice2 != "4" and choice2 != "5":
        choice2 = input("do you want to download a video or audio or playlist or audio_playlist or subtitle tracker ("
                        "1/2/3/4/5): ")
    if choice2 == "1":
        # download path
        path = input("enter please your path: ")
        vid_dwon()
    elif choice2 == "2":
        path = input("enter please your path: ")
        audio_down()
    elif choice2 == "3":
        path = input("enter please your path: ")
        play_dwon()
    elif choice2 == "4":
        path = input("enter please your path: ")
        Mplay_dwon()
    elif choice2 == "5":
        subtitle()

elif choice == "n":
    sys.exit()

input("press any button to exit")