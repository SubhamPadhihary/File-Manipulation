import os
import shutil
import re
src = "D:\\Downloads\\Mega"
movies = "D:\\Movies"
tv = "D:\\TV Series"
comics = "D:\\Comics"

def get_file_names():
    """
    Returns the paths and names of all the videos and comics in src...
    """
    # The names are needed to display messages in consoles
    video_names = []
    comics_names = []
    for dirPath, dirNames, fileNames in os.walk(src):
        for file in fileNames:
            if file.endswith(".mkv") or file.endswith(".mp4"):
                video_names.append(file)
            if file.endswith(".cbr") or file.endswith(".cbz"):
                comics_names.append(file)
    return video_names, comics_names

# get all the paths of the filenames
video_names, comics_names  = get_file_names()


def ask_for_confirmation_before_moving(names):
    for name in names:
        if name in video_names:
            if re.search(r'(S|s)\d{2}(E|e)\d{2}', name) or re.search(r'\s-\s\d{2}', name) or re.search(r'(Episode|episode)\s\d{2}', name):
                print('moving {0} from {1} to {2}'.format(name, src, tv))
            else:
                print('moving {0} from {1} to {2}'.format(name, src, movies))               
        elif name in comics_names:
            print('moving {0} from {1} to {2}'.format(name, src, comics))
    choice = input('confirm y or n: ')
    return choice


def move_videos():
    if len(video_names) == 0:
        print(' There are no videos here... ')
    else:
        choice = ask_for_confirmation_before_moving(video_names)
        if choice == 'y' or choice == 'Y':
            for video in video_names:
                if re.search(r'(S|s)\d{2}(E|e)\d{2}', video) or re.search(r'\s-\s\d{2}', video) or re.search(r'(Episode|episode)\s\d{2}', video):
                    shutil.move(os.path.join(src, video), os.path.join(tv, video))
                    print('moved {0} from {1} to {2}'.format(video, src, tv))
                else:
                    shutil.move(os.path.join(src, video), os.path.join(movies, video))
                    print('moved {0} from {1} to {2}'.format(video, src, movies))
        else:
            print('OK. Aborted.')

def move_comics():
    if len(comics_names) == 0:
        print(' There are no comics here... ')
    else:
        choice = ask_for_confirmation_before_moving(comics_names)
        if choice == 'y' or choice == 'Y':
            for comic in comics_names:
                shutil.move(os.path.join(src, comic), os.path.join(comics, comic))
                print('moved {0} from {1} to {2}'.format(comic, src, comics))
        else:
            print('OK. Aborted.')

if __name__ == "__main__":
    move_videos()
    move_comics()