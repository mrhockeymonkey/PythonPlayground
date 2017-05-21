import os
import shutil
import send2trash # Third party module - pip install send2trash
import zipfile

# Create a path that will work on any OS, i.e. \\ for windows / for linux
files = ['file1.txt','file2.txt','file3.txt']
for filename in files :
	print(os.path.join('C:\\temp',filename)) # important to use this join to work on any os

# Current working directory
os.getcwd() 
os.chdir('C:\\Temp') # equiv: cd or sl
os.makedirs('.\\folder1') # Create a new directory (will also create intermediary)
os.listdir() # List contents of directory

# Paths
os.path.abspath('.') # Convert relative path into an absolute one
os.path.dirname('.\\stuff.txt') # Returns folder path
os.path.basename('.\\stuff.txt') # Returns filename
os.path.getsize('.\\stuff.txt') # Get size of item
os.path.exists('.\\stuff.txt') # Equiv of Test-Path
os.path.isfile('.\\stuff.txt') # check its a file, can also use isdir() to check its a directory
base, ext = os.path.splitext() #split the base and extention from a file and save

# Reading and Writing plaintext 
file = open('C:\\Temp\\stuff.txt') # Open a file to get the file object, this also create a new file if not present
file.read() # Read entire contents
file.reasdlines() # Returns a list of each line
file.close() # close the handle you have on the file
# Note: You can only read the file once?

# Writing to files
f = open('C:\\temp\stuff.txt', 'w') # Open the file in 'w' Write Mode (Overwrites existing or creates if missing)
f.write('I have been overwritten!') 
f.close()

f = open('C:\\temp\\stuff.txt', 'a') # Open the file in 'a' Append Mode
f.write('I have been appended!')
f.close()

# Moving files
shutil.copy('C:\\Temp\\stuff.txt', 'C:\\temp\\stuff.txt.copy') # Copy a file (source, dest)
shutil.copytree('C:\\temp\\folder1', 'C:\\temp\\folder1_bu') # Create a copy of an entire folder
shutil.move('C:\\temp\\stuff.txt','C:\\temp\\folder1\\stuff.txt') # Move a file, note that of you specify only a folder in dest it will keep the same filename

# Deleting files Permanently
os.unlink('C:\\temp\\stuff.txt') # Delete single file
os.rmdir('C:\\temp\\folder2') # Delete a single empty folder
shutil.rmtree('C:\\temp\\folder1_bu') # Remove a folder and al contents (recursive)

# Deleting file Safely (RecycleBin)
send2trash.send2trash('C:\\temp\\recoverme.txt') # Send item to recycle bin. 

# Walk a directory
for walk in os.walk('C:\\temp'): # os.walk returns a tuple (foldername, subfolders, files) and recurses through each subfolder
	print(walk)

#Note if you want to explore what is in walk without looping usng list(walk)

# Creating Zip files
new_zip = zipfile.ZipFile('C:\\temp\\new.zip', 'w') # Similar to open(file, mode), 'w' is write mode
new_zip.write('C:\\temp\\zipme.txt', compress_type = zipfile.ZIP_DEFLATED)
new_zip.close()

# Reading Zip files
zip = zipfile.ZipFile('C:\\temp\\new.zip') # default to mode='r'
zip.namelist() # get list of files in zip
zip.getinfo(zip.namelist()[0]) # Getinfo on a particular file, in this case the first file from namelist()
zip.extractall('C:\\temp\\') # extract all files, can also use extract() to pick particular files
zip.close()


