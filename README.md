# AquaSentinel - Lionfish Detector and Data Collector
[https://github.com/PranavaKCode/AquaSentinel_Final_Draft.git](url)

[Video Demonstration](https://www.youtube.com/watch?v=RJb2n-2TQB0)

AquaSentinel is an AI Object Detection project that combats the threat of Lionfish invasion in the Caribbean. 
Using Imagenet, resnet-18, and a complex custom image classification program it accurately identifies Lionfish even in challenging underwater conditions and can alert marine conservation teams, local authorities, or volunteers instantly via email. 
It also collects data on lionfish such as how much lionfish were detected each day, a bar graph to show that in a visual format, and logs that show the timestamp, class, image, and more data.
The project's potential impact extends globally, offering a pioneering approach to safeguarding marine ecosystems from invasive species threats, and collecting data on invasive lionfish. 


## The Algorithm
This project uses the resnet-18 model and a custom-made imagenet classification program. The imagenet classification program was created on Jetson Nano and has a multitude of functions. 
Here are its following functions:

**Email Sending: It can send emails to marine conservation teams, local authorities, or volunteers as soon as a lionfish is detected as well as a daily report of how many lionfish were detected on that day using the smtplib and time libraries.(Currently only sends an email to myself as to not false report.)**

Emails:
![Emails:](https://i.imgur.com/QPTAUwD.jpg) 

Email Code:![Email Code](https://i.imgur.com/mpd8aBB.jpg) 

Daily Email:

![image](https://github.com/PranavaKCode/AquaSentinel_Rough_Draft/assets/126040433/45d27a3b-70af-4f3b-931d-cf695cf902da)


Daily Email Code Runs at a specific time every day:![image](https://github.com/PranavaKCode/AquaSentinel_Rough_Draft/assets/126040433/97561d88-4036-43d9-8e17-08630ff93c8e)

**Csv file: It keeps track of how much lionfish are detected per day and shows it in the csv file as well as the terminal**

in terminal and csv:![in terminal and csv](https://i.imgur.com/1SBb5Vy.jpg) 

A part of its code:

![A part of its code](https://i.imgur.com/yaRajF9.jpg)

**Bar graph for data analysis: The bar graph takes the date and count values and shows them in a presentable visual graph.**

bar graph:![](https://i.imgur.com/mWEvP0M.jpg) 
bar graph code(creates a bar graph and gives it values):

![](https://i.imgur.com/tjir5PX.jpg)

**Detection data/logs: The detection data shows what the program has detected and the timestamp, image, class, and confidence rating. 
If it has detected a lionfish it says "**** Found 🦁🐟 Lion Fish 🦁🐟✅ ****" the timestamp and other data and a link to a doc that contains information on what to do.
If it has detected something else resnet-18 knows it says "Found{class name}❌".**

logs:![](https://i.imgur.com/mnbYiph.jpg)  
One of the parts of the code(generates logs that are different based on whether it is a lionfish or not):![](https://i.imgur.com/Nfyfbk6.jpg)
-s
## Running this project

1. **Steps For Running this project**
   
   1. Create an email and get its app key password. [Video showing how to get app key password](https://www.youtube.com/watch?v=hXiPshHn9Pw)
   2. Log in to VsCode
   3. Connect to nano via remote ssh host
   4. Create a folder in vs code and name it(Ex. my-recognition)
   5. Create or Download from Aquasentinel github(url given at top of this doc) the following files my_recognition.py, lionfish_detection_counts.csv, and detection_data.txt(lionfish_detection_counts.png will be automatically generated after running)
   6. fill out the def send_email(subject, message) function in the my_recognition.py with your email, app key password, and the email(s) of local conservation organizations or authorities.
   7. Type Date,Count into lionfish_detection_counts.csv(ignore if already there) file and paste the files from step 5(or drag and drop the files dowloaded) in github into your vscode folder.
   8. Run the following commands
      1. cd my-recognition(or whatever the name of your folder is)
      2. python3 my_recognition.py (insert image name here and remove parenthesis).jpg  (e.g. python3 my_recognition.py 1Lionfish.jpg)
   9. Enjoy the program!
2. **Libraries used in my project**

All of these are default libraries that you dont need to install but need to use for the project to work

import csv

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

import matplotlib.cm as cm

import smtplib

from email.mime.text import MIMEText

import time
## Miscellaneous Resources
[https://www.w3schools.com/python/default.asp](url)

[https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-console-2.md](url)

[https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-example-python-2.md](url)
## Video Explanation

[View a video explanation here](https://www.youtube.com/watch?v=RJb2n-2TQB0)
