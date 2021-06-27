import os
import re

dir = "/Users/lovkush/Desktop/Folder/Teaching/STEP/past papers solutions"

filenames = os.listdir(dir)

step_pat = (
    r"STEP ([I1]{1,3})\: ([0-9]{4,4}).*[^0-9]([0-9]{1,4}[a-dA-D]?)([a-z\.]{4,4})$"
)

for filename in filenames:
    if filename == ".DS_Store":
        continue
    if filename == "answer_urls.txt":
        continue
    print(filename)
    match = re.match(step_pat, filename)
    step = match.group(1)
    year = match.group(2)
    q = match.group(3)
    ext = match.group(4)
    step = str(len(step))
    #    print(f"{filename:30}, {step:3} {year} {q:3} {ext}")
    filename_new = f"{year}-S{step}-{q}{ext}"
    print(f"{filename:30} {filename_new}")

    os.rename(dir + "/" + filename, dir + "/" + filename_new)
