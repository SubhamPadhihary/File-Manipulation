import os

# Changing directory
os.chdir("D:\\Movies")
print(os.listdir())
# Get the file names
file_names = []
for dirpath, dirname, filename in os.walk("D:\\Movies"):
    #for file in filename:
        #if file.endswith(".mp4"):
            #file_names.append(os.path.join(dirpath, file))
    print(dirpath, dirname, filename, sep= '\n')
#print(file_names)