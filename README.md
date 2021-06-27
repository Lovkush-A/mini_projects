# Mini Projects

## Summary
This repository stores the code and other artifacts for mini projects that I do. Some of projects are just little python scripts to automate a little task I wanted to do. Some of the projects are little investigations in a jupyter notebook.

## Projects
* askhole. askhole is a website with a list of 100 interesting questions you could have discussions about. When I copied the list of questions from the pdf file, it was a bit dirty, so I wrote a little python script to clean it up.
* hothand (incomplete). I read the book Hothand, which tells the story of the hothand phenomenon in basketball and the subtle statistics involved in trying to determine whether a sequence is random or not. This notebook contains my investigations into the relevant statistics/distributions.
* telestrations. During covid-19 pandemic, my friends and I played the game Telestrations by sending each other pictures of sentences/drawings over whatsapp.  I agreed that I would gather all the images and stitch them together to form the completed sequences of sentence-drawing-sentence-drawing-... . I therefore created this python script to do this stitching for me. It is not completely automated - it still requires me to manually name each of the image files before stitching can occur - but it is a big time saver!
* step_papers. STEP is a mathematics exam in the UK to help the elite universities choose candidates for mathematical subjects. I provide tuition for this and wanted to download past papers and solutions. This folder contains three different things that helped automate the process:
  * download_step.py. Simple script to download all the past papers that were available
  * download_step_solutions.py. More complex script, using `selenium`, to download solutions available on mea website
  * rename_solutions.py. Script to rename the solution files downloaded in the previous step, as they did not have consistent naming format
