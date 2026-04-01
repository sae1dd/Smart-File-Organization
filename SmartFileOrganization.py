import os
import shutil

videos = [".mp4",".avi"]
photos = [".jpg",".jpeg",".png"]
documents = [".pdf",".doc",".docx"]
texts = [".txt",".py"]

fileWay = input("Enter file way: \n")

allFiles = os.listdir(fileWay)

for file in allFiles:
    name, fileType = os.path.splitext(file)
    print("File`s name -->", name, "|", "Files`s type -->", fileType)

    if fileType in photos:
        newFolder = os.path.join(fileWay, "Pictures")

        if not os.path.exists(newFolder):
            os.mkdir(newFolder)
        oldFolder = os.path.join(fileWay, file)
        newFolder = os.path.join(newFolder, file)
        shutil.move(oldFolder, newFolder)
        print(file, "--> Pictures moved to new folder")

    elif fileType in videos:
        newFolder = os.path.join(fileWay, "Videos")
        if not os.path.exists(newFolder):
            os.mkdir(newFolder)
        oldFolder = os.path.join(fileWay, file)
        newFolder = os.path.join(newFolder, file)
        shutil.move(oldFolder, newFolder)
        print(file, "--> Videos moved to new folder")

    elif fileType in documents:
        newFolder = os.path.join(fileWay, "Documents")
        if not os.path.exists(newFolder):
            os.mkdir(newFolder)
        oldFolder = os.path.join(fileWay, file)
        newFolder = os.path.join(newFolder, file)
        shutil.move(oldFolder, newFolder)
        print(file, "--> Documents moved to new folder")

    elif fileType in texts:
        newFolder = os.path.join(fileWay, "Texts")
        if not os.path.exists(newFolder):
            os.mkdir(newFolder)
        oldFolder = os.path.join(fileWay, file)
        newFolder = os.path.join(newFolder, file)
        shutil.move(oldFolder, newFolder)
        print(file, "--> Texts moved to new folder")

    else:
        newFolder = os.path.join(fileWay, "Other")
        if not os.path.exists(newFolder):
            os.mkdir(newFolder)
        oldFolder = os.path.join(fileWay, file)
        newFolder = os.path.join(newFolder, file)
        shutil.move(oldFolder, newFolder)
        print(file, "--> Others moved to new folder")