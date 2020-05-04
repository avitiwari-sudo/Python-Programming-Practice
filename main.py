import os

def createIfNotExists(folders):
    for dir in folders:
        if not os.path.exists(dir):
             os.makedirs(dir)
        else:
             print('Already Exists')

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

folder = ['Images','Docs', 'Media', 'Text','PDF', 'Others']
print(createIfNotExists(folder))

files = os.listdir()
files.remove("main.py")
print(files)

print("======================================================================")

imgExts = [".png"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
#print(images)

docExts = [".docx"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
#print(docs)

meExt = [".mp4"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in meExt]
#print(medias)

te = [".txt"]
text = [file for file in files if os.path.splitext(file)[1].lower() in te]
#print(text)

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in te) and (ext not in meExt) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)
#print(others)

move("Images", images)
move("Text", text)
move("Media", medias)
move("Docs", docs)
move("Others", others)
