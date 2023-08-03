# AquaSentinel

AquaSentinel is an AI Object Detection project that combats the threat of Lionfish invasion in the Caribbean. 
Using Imagenet and resnet-18, it accurately identifies Lionfish even in challenging underwater conditions and can alert marine conservation teams, local authorities, or volunteers instantly. 
The project's potential impact extends globally, offering a pioneering approach to safeguarding marine ecosystems from invasive species threats, and collecting data on invasive lionfish. 

![add image descrition here](direct image link here)

## The Algorithm
This project uses the resnet-18 model and a custom-made imagenet classification program. The imagenet classification program was created on Jetson Nano and has a multitude of functions. 
Here are its following functions:
-Email Sending:It can send emails to marine conservation teams, local authorities, or volunteers as soon as a lionfish is detected as well as a daily report of how many lionfish were detected on that day using the smtplib and time libraries.(Currently only sends an email to myself as to not false report.)
Emails:[https://i.imgur.com/QPTAUwD.jpg](url) (Daily report  only works when running at 11:59 so no image) Email Code:[https://i.imgur.com/He6y0ea.jpg](url) Daily Email Code:[https://i.imgur.com/4VtMPvn.jpg](url)
-Csv file: It keeps track of how much lionfish are detected per day and shows it in the csv file as well as the terminal
in terminal and csv:[https://i.imgur.com/1SBb5Vy.jpg](url) A part of its code:[https://i.imgur.com/yaRajF9.jpg](url)
-Bar graph for data analysis: The bar graph takes the date and count values and shows them in a presentable visual graph.
bar graph:[https://i.imgur.com/mWEvP0M.jpg](url) bar graph code:[https://i.imgur.com/tjir5PX.jpg](url)
-Detection data/logs: The detection data shows what the program has detected and the timestamp, image, class, and confidence rating. 
If it has detected a lionfish it says "**** Found 🦁🐟 Lion Fish 🦁🐟✅ ****" the timestamp and other data and a link to a doc that contains information on what to do.
If it has detected something else resnet-18 knows it says "Found{class name}❌".
logs:[https://i.imgur.com/mnbYiph.jpg](url)  One of the parts of the code:[https://i.imgur.com/Nfyfbk6.jpg](url)
-s
## Running this project

1. Add steps for running this project.
   1. Log in to VsCode
   2. Connect to nano via remote ssh host
   3. Create a folder in vs code and name it(Ex. my-recognition)
   4. Create the following files my_recognition.py, lionfish_detection_counts.csv, and detection_data.txt(lionfish_detection_counts.png will be automatically generated after running)
   5. Type Date,Count into csv file and paste the my_recognition.py in github into your vscode file.
   6. Run the following commands
      1. cd my-recognition
      2. python3 my_recognition.py (insert image here and remove parenthesis).jpg(Ex. 1Lionfish.jpg or Jellyfish.jpg)
   7. The program shold work as intended.
3. Make sure to include any required libraries that need to be installed for your project to run.
All of these are default libraries 
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import smtplib
from email.mime.text import MIMEText
import time
[View a video explanation here](video link)
