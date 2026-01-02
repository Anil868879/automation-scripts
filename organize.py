import os
import shutil

mapping = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3"],
    "Software": [".zip", ".exe"]
}

for filename in os.listdir():
    for folder, exts in mapping.items():
        if filename.endswith(tuple(exts)):
            if not os.path.exists(folder):
                os.mkdir(folder)
            shutil.move(filename, folder + "/" + filename)

print("Organizing complete!")
