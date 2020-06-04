import os
import subprocess

ABSOLUTE_PATH = os.getcwd()
entertainment = 'movies'  # input('Enter the type of entertainment(Eg. Movies TV Shows Games etc) ')

if entertainment == 'Movies' or 'movies':
    # Changing Directory to Movies
    os.chdir('D:\\Movies')
    # Got to rename the movies' names because they are named with . separators
    movies_with_original_names = os.listdir('.')
    movies_renamed = []
    for a_movie in movies_with_original_names:
        movies_renamed.append(a_movie.replace('.', ' '))
    movie = input('Enter Movie Name ').split()
    movie = ' '.join(movie)
    # creating a path list
    movies_path_list = []
    d = 'D:\\Movies'
    for dir_path, dir_names, file_names in os.walk(d):
        for file in file_names:
            if file.endswith(".mp4"):



    for i in movies_renamed:
        if movie in i:
            movie_path_index = movies_renamed.index(i)
            movie_path = movies_path_list[movie_path_index]
            subprocess.Popen(["D:\\Program files\\VLC\\vlc.exe", )
            print('yay')

    # To see how things are working

    print(os.getcwd())
    print(movies_renamed)
    print(movies_with_original_names)
    print(movie_path, type(movie_path))
    print(movies_with_original_names[movie_path_index] + ".mp4")
    print(movies_path_list)
    for i in movies_path_list:
        print(i)