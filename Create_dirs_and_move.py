import shutil
import os


movies = "D:\\Movies"

# get the file names without their extensions for the dir names.
def get_file_names():
    file_names = []
    for everything in os.listdir(movies):
        if everything.endswith('.mkv') or everything.endswith('.mp4'):
            file_names.append(everything)
    return file_names

file_names = get_file_names()
# Create dirs with the corresponding file names
def create_dirs():
    dir_path = ''
    choice = ask_for_confirmation_before_creating_dirs()
    if choice == 'y':
        for files in file_names:
            dir_path = os.path.join(movies, os.path.splitext(files)[0])
            if not os.path.exists(dir_path) :
                os.mkdir(dir_path)
            else:
                print('Folder {0} already created'. format(os.path.splitext(files)[0]))
    else:
        print('Ok. Aborted.')
        exit(1)

def ask_for_confirmation_before_creating_dirs():
    dir_path = ''
    for files in file_names:
        dir_path = os.path.join(movies, os.path.splitext(files)[0])
        if not os.path.exists(dir_path):
            print('Creating {0}'.format(dir_path))
        else:
            print('{0} already created'. format(dir_path))
    choice = input('Do you confirm?(y/n): ')
    return choice
        
    

# Move the files to the appropriate dirs.
def ask_for_confirmation_before_moving():
    dir_name = ''
    dir_path = ''
    for everything in os.listdir(movies):
        # Get the dir_path to move the file to corresponding dir.
        if os.path.isdir(os.path.join(movies, everything)):
            dir_name = everything  # For the console message.
            dir_path = os.path.join(movies, everything)  # To move.
        # if it's a file of any kind and the name of it matches the dir_path, then move the file.
        if os.path.isfile(os.path.join(movies, everything)):
            if dir_name in everything:       
                # before moving it's a good idea to display some messages in console and maybe ask for confirmation.
                print('moving {0} to the folder {1}'.format(everything, dir_path))
    
    choice = input('Do you confirm?(y/n): ')
    return choice


def move_files():
    # ask for confirmation and move files code is very similar.
    dir_name = ''
    dir_path = ''
    choice = ask_for_confirmation_before_moving()
    if choice == 'y':
        for everything in os.listdir(movies):
            # Get the dir_path to move the file to corresponding dir.
            if os.path.isdir(os.path.join(movies, everything)):
                dir_name = everything  # For the console message.
                dir_path = os.path.join(movies, everything)  # To move.
            # if it's a file of any kind and the name of it matches the dir_path, then move the file.
            if os.path.isfile(os.path.join(movies, everything)):
                if dir_name in everything:       
                    shutil.move(os.path.join(movies, everything), dir_path)
        print('This was pretty cool...')
    else:
        print('Ok. Aborted.')       

if __name__ == "__main__":
    create_dirs()
    move_files()
