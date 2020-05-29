import os

os.chdir('D:\\Movies')
d = 'D:\\Movies'
full_path = []
for path in os.listdir(d):
    full_path.append(os.path.join(d, path))
print(full_path)
s = input().split()
print(s)
print(''.join(s))
print(' '.join(s))