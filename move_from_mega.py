import re
import os
import shutil
mega = "D:\\Downloads\\Mega"
# get the all the files in the dir.
source_list = []
filenames2 = []
for dirpath, dirnames, filenames in os.walk(mega):
    for file in filenames:
        if file.endswith('.mkv') or file.endswith('.mp4') and ():
            # This list contains the filenames with type.
            filenames2.append(file)   
            filepath = os.path.join(mega, file)
            # This list contains the source paths
            source_list.append(filepath)
movies = 'D:\\Movies'
tv = 'D:\\TV Series'
dest = ''
for i in filenames2:
    if re.search(r'(S|s)\d{2}(E|e)\d{2}', i) or re.search(r'\s-\s\d{2}', i) or re.search(r'(Episode|episode)\s\d{2}', i):
        print('Moving {0} from {1} to {2}'.format(i, mega, tv))
    else:
        print('Moving {0} from {1} to {2}'.format(i, mega, movies))
print('CONFIRM:')
x = input('y or n? ')
if x == 'y':
    for i in range(len(filenames2)):
        if re.search(r'(S|s)\d{2}(E|e)\d{2}', filenames2[i]) or re.search(r'\s-\s\d{2}', filenames2[i]) or re.search(r'(Episode|episode)\s\d{2}', filenames2[i]):
            dest = os.path.join(tv, filenames2[i])
            if os.path.exists(dest):
                print('{0} already exists in TV Series.'.format(filenames2))
                file_exists_choice = input('Do you want to overwrite or skip (Type o to overwrite or s to skip)')
                if file_exists_choice == 'o':
                    shutil.move(source_list[i], dest)
                    print('Moved {0} from {1} to {2}'.format(filenames2[i], mega, tv))
                elif file_exists_choice == 's':
                    continue
            else:
                shutil.move(source_list[i], dest)
                print('Moved {0} from {1} to {2}'.format(filenames2[i], mega, tv))
        else:
            dest = os.path.join(movies, filenames2[i])
            if os.path.exists(dest):
                print('{0} already exists in Movies.'.format(filenames2))
                file_exists_choice = input('Do you want to overwrite or skip (Type o to overwrite or s to skip)')
                if file_exists_choice == 'o':
                    shutil.move(source_list[i], dest)
                    print('Moved {0} from {1} to {2}'.format(filenames2[i], mega, movies))
                elif file_exists_choice == 's':
                    continue
            else:
                shutil.move(source_list[i], dest)
                print('Moved {0} from {1} to {2}'.format(filenames2[i], mega, tv))
            
else:
    print('ok.')
