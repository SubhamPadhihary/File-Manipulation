import os
import subprocess
import collections


def movies():
    path = "D:\\Movies"
    vlc_path = "D:\\Program files\\VLC\\vlc.exe"

    # input the name of the movie
    movie_name = input('Enter the name of the movie').split()
    movie_name = ' '.join(movie_name)

    # Get the path of the movies and names of movies
    movie_path_list, movie_names = get_movie_path_and_names(path)  # print(movie_path_list, movie_names, sep='\n')

    # create a movie_launch dictionary containing movie_name as key and
    # index of that movie in movies_name_only as value.
    movie_to_launch = collections.defaultdict(int)  # print(movie_to_launch) to see what it looks like
    movie_names_to_access_the_dict = []
    for index, a_movie in enumerate(movie_names):
        if movie_name in a_movie:
            movie_to_launch[a_movie] += index

    # If there is only one movie run it using VLC
    if len(movie_to_launch) == 1:
        subprocess.Popen([vlc_path, movie_path_list[movie_to_launch[list(movie_to_launch.keys())[0]]]])

    # If there are more than one movies found, list the movies.
    elif len(movie_to_launch) > 1:
        for index, key in enumerate(movie_to_launch.keys()):
            print(index + 1, '. ', key, sep='')
        # And Prompt for a choice
        choice = int(input('Enter choice: '))
        # Select the movie from dict.keys() and run it.
        movie_name = list(movie_to_launch.keys())[choice - 1]
        subprocess.Popen([vlc_path, movie_path_list[movie_to_launch[movie_name]]])
    else:
        print('Not Found')


def get_movie_path_and_names(path):
    """ (str) -> list, list

    Accepts the path of a directory and returns the a list containing the path of all the movies
    and another with the names of all movies.
    """
    movie_path_list = []
    movie_names = []
    # dir_path has the
    for dir_path, dir_names, file_names in os.walk(path):
        for file in file_names:
            if file.endswith(".mp4") or file.endswith(".mkv"):
                movie_path_list.append(os.path.join(dir_path, file))  # a list containing movies' path
                movie_names.append(file)  # a list containing the original movies name with extensions
    # Rename the movie_names_only to remove all the "."
    movie_names = rename_movie_names(movie_names)
    return movie_path_list, movie_names


def rename_movie_names(movie_names):
    """(list) -> list

    Takes movie_names list and removes all the "." from the names
    """
    renamed_movie_names = []
    for movie in movie_names:
        renamed_movie_names.append(movie.replace('.', ' '))
    return renamed_movie_names


if __name__ == "__main__":
    movies()
