import subprocess

for i in range(87,119):
    for j in range(1,4):
        i = i%100
        url = f"https://stepdatabase.maths.org/database/db/{i:02}/{i:02}-S{j}.pdf"
        subprocess.run(["wget", url])

for i in range(87,119):
    for j in range(1,4):
        i = i%100
        url = f"https://stepdatabase.maths.org/database/db/{i:02}/{i:02}-S{j}.tex"
        subprocess.run(["wget", url])
