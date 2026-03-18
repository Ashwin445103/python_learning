import os

# Specify the directory path
path = '/'

# Check if the directory exists
if os.path.exists(path) and os.path.isdir(path):
    print("\nContents of the directory:\n")
    
    # List all files and folders
    for item in os.listdir(path):
        print(item)
else:
    print("Invalid directory path")
