import os
import re

tv_series_path = "D:\\TV Series"
def get_folder_names():
    '''
    Takes no arguments.
    Returns a list of folder names(folder_names), using which folders will be created.
    '''
    folder_names = []
    # listdrir lists all the files and folders in the given path.
    for everything in os.listdir(tv_series_path):
        # get the names of mkv files you want to create folders for.
        if everything.endswith(".mkv"):
            # if the the tv shows are episodic i.e Something containing like S01E19.
            if re.search(r'(S|s)\d\d(E|e)\d\d', everything):
                # for folder names, remove everything right of Season and episode num
                # for example: The.Stand.2020.S01E01.The.End.720p.10bit.WEBRip.2CH.x265.HEVC-PSA.mkv
                # will become The.Stand.2020
                folder_name = re.sub(r'\.(S|s)\d\d(E|e)\d\d\.(\d|\w|\.|-)+', '', everything)
            else:
                # If it's not an episode: George.Carlin.Life.Is.Worth.losing.2005.720p.BrRip.2CH.x265.HEVC-PSA.mkv
                # Just remove everything from(incl.) 720p or 1080p.
                # ex - George.Carlin.Life.Is.Worth.losing.2005
                folder_name = re.sub(r'\.(\d{3}|\d{4})p\.(\d|\w|\.|-)+', '', everything)
            folder_names.append(folder_name)
    return folder_names
def prompt_create_folders(folder_names: list):
    '''
    Takes a list of folder_names and prompts user to confirm the creation of folders.
    If they confirm create_folders() is called.
    '''
    print('Creating folders: ')
    for index, folder_name in enumerate(folder_names):
        print(f'{index + 1}. {os.path.join(tv_series_path, folder_name)}' )
    choice = input('Confirm(Y/N): ')
    if choice == 'Y' or choice == 'y':
        print('Okay.')
        create_folders(folder_names)
    elif choice == 'N' or choice == 'n':
        print('You refused to create Folders')
        input('Press Enter to Exit')
        exit(1)
    else:
        input('Invalid Choice. Press Enter to exit.')
        exit(1)

def create_folders(folder_names):
    '''
    Takes a list of folder_names as argument and creates folders from the strings in that list.
    '''
    for folder_name in folder_names:
        try:
            os.mkdir(os.path.join(tv_series_path, folder_name))
        except:
            print(f'folder {folder_name} already exists.')
    input('Folders created. Press Enter to continue.')

def prompt_move(folder_names):
    """
    Takes a list folder_names as argumenr.
    Prompts users whether they want to move the files as per the given path or nor.
    """
    files_to_move = []
    # get files to move.
    for everything in os.listdir(tv_series_path):
        # get all the files in the folder and not just mkv's.
        if os.path.isfile(os.path.join(tv_series_path, everything)) and not everything.endswith('.parts'):
            files_to_move.append(everything)
    files2folders = {}
    for folder_name in folder_names:
        for file_to_move in files_to_move:
            if folder_name in file_to_move:
                files2folders[file_to_move] = folder_name
    for file, folder in files2folders.items():
        print(f'Moving {file} to {folder}')
    choice = input('Confirm(Y/N): ')
    if choice == 'Y' or choice == 'y':
        print('Okay.')
        move(files2folders)
    elif choice == 'N' or choice == 'n':
        input('You refused to move files. Press Enter to Exit.')
        exit(1)
    else:
        input('Invalid Choice. Press Enter to exit.')


def move(files2folders: dict):
    '''
    Arguments: a dictionary containing corresponding file and folder names(created in prompt_move()).
    Moves files to their corresponding folders.
    '''
    for file, folder in files2folders.items():
        # create folder/destination from folder name in files2folders.
        folder_path = os.path.join(tv_series_path, folder)
        folder_dest_path = os.path.join(folder_path, file)
        # Create file origin path from file name in files2folders.
        file_src_path = os.path.join(tv_series_path, file)
        # move files.
        os.replace(src=file_src_path, dst=folder_dest_path)



if __name__ == "__main__":
    folder_names = get_folder_names()
    if len(folder_names) > 0:
        prompt_create_folders(folder_names)
        prompt_move(folder_names)
    else:
        input('Nothing to move. Press Enter to exit.')