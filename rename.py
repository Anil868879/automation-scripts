import os

folder = "files"
files = os.listdir(folder)

count = 1
for file in files:
    old = os.path.join(folder, file)
    new = os.path.join(folder, f"file_{count}.txt")
    os.rename(old, new)
    count += 1

print("Renaming complete!")
