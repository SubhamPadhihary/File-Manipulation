import os
import subprocess

ABSOLUTE_PATH = os.getcwd()
entertainment = 'movies'  # input('Enter the type of entertainment(Eg. Movies TV Shows Games etc) ')

if entertainment == 'Movies' or 'movies':
    os.chdir('D:\\Movies')
    movies_with_original_names = os.listdir('.')
    movies_formatted = []
    for movie in movies_with_original_names:
        movies_formatted.append(movie.replace('.', ' '))
    movie = input('Enter Movie Name ').split()
    movie = ' '.join(movie)
    # creating a path list
    movies_path_list = []
    d = 'D:\\Movies'
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if

    for i in movies_formatted:
        if movie in i:
            movie_path_index = movies_formatted.index(i)
            movie_path = movies_path_list[movie_path_index]
            subprocess.Popen(["D:\\Program files\\VLC\\vlc.exe", movie_path + "\\"
                              + movies_with_original_names[movie_path_index] + '.mp4'])
            print('yay')

    # To see how things are working

    print(os.getcwd())
    print(movies_formatted)
    print(movies_with_original_names)
    print(movie_path, type(movie_path))
    print(movies_with_original_names[movie_path_index] + ".mp4")
    print(movies_path_list)
    for i in movies_path_list:
        print(i)