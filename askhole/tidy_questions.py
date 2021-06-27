import re

with open('questions.txt') as f:
    text = f.read()

text = re.sub('( ?www.askhole.io ?)+', '', text)
text = re.sub('#\d+ ', '', text)
text = re.sub('\? ', '?\n', text)
print(text)
