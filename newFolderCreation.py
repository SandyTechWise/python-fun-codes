import os

# define the name of the directory to be created
path = "C:/NewFolder/Music"


for x in range(99):
  os.mkdir(path+format(x))
  print("newfolder created as"+path+format(x)+" successfully")