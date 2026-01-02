import os
from datetime import date

today = str(date.today())

# create folder if not exists
if not os.path.exists(today):
    os.mkdir(today)

file_path = os.path.join(today, "study_log.txt")

with open(file_path, "w") as f:
    f.write("Study Log\n")
    f.write("Date: " + today + "\n")
    f.write("--------------------\n")
    f.write("Topics Covered:\n")
    f.write("- \n")
    f.write("\nNotes:\n")
    f.write("- \n")

print("Log file created at:", file_path)
