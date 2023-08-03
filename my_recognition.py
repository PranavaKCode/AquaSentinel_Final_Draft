import jetson_inference
import jetson_utils
import argparse
import datetime
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import smtplib
from email.mime.text import MIMEText
import time

EMAIL_FROM = 'PranavaKCode@gmail.com' ###Replace this with your email
EMAIL_PASSWORD = 'eutq wmed ppcv ygzg'
EMAIL_TO = 'goodpranava@gmail.com' ###Replace this email with email to local authorities or conservation organizations

def send_email(subject, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def create_bar_chart(dates, counts):
    plt.figure(figsize=(10, 6)) 
    colors = cm.viridis(counts)
    plt.bar(dates, counts, color=colors, width=0.6)
    plt.xlabel('Date')
    plt.ylabel('Detection Count')
    plt.title('Monthly Lionfish Detection Counts')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('lionfish_detection_counts.png') 
    plt.close()  


def log_detection_data(filename, class_idx, confidence):
    with open("detection_data.txt", "a") as file:
        class_desc = net.GetClassDesc(class_idx)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if class_desc.lower() == 'lionfish':
            file.write("**** Found 🦁🐟 Lion Fish 🦁🐟✅ ****\n")
            subject = "Lionfish Detected!"
            message = f"Lionfish detected at {timestamp}. Image: {filename}. Confidence: {confidence * 100:.2f}%."
            send_email(subject, message)
        else:
            file.write("Found {}❌\n".format(class_desc.lower()))
        file.write("Timestamp: {}, Image: {}, Class: {}, Confidence: {}\n".format(timestamp, filename, class_desc, confidence))
       
        if class_desc.lower() == 'lionfish':
            file.write("For more information visit https://docs.google.com/document/d/1OOiA4ECzIOCy3uZa87wdsUrwACEAY9ehO1IteUYVS4k/edit\n")
        current_month_day = datetime.datetime.now().strftime("%Y-%m-%d")
        counts = {}
    with open("lionfish_detection_counts.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            counts[row["Date"]] = int(row["Count"])



    if class_desc.lower() == 'lionfish':
        counts[current_month_day] = counts.get(current_month_day, 0) + 1



    with open("lionfish_detection_counts.csv", "w", newline="") as csvfile:
        fieldnames = ["Date", "Count"]
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        for date, count in counts.items():
            csvwriter.writerow({"Date": date, "Count": count})


    # Create the bar chart and save it as a PNG file
    dates = list(counts.keys())
    counts = list(counts.values())
    create_bar_chart(dates, counts)


    # Display the counts in a tabular format
    print("\nDaily Lionfish Detection Counts:")
    print("-------------------------------")
    with open("lionfish_detection_counts.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            print("{} | {}".format(row["Date"], row["Count"]))
    print("-------------------------------")


parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="resnet-18", help="model to use, can be: googlenet, resnet-18, etc. (see --help for others)")
opt = parser.parse_args()




img = jetson_utils.loadImage(opt.filename)
net = jetson_inference.imageNet(opt.network)




class_idx, confidence = net.Classify(img)




class_desc = net.GetClassDesc(class_idx)
print("Image is recognized as '{}' (class #{}) with {:.2f}% confidence".format(class_desc, class_idx, confidence * 100))




log_detection_data(opt.filename, class_idx, confidence)










# Display additional information for Lionfish detection
if class_desc.lower() == 'lionfish':
    print("\nWhat to do:")
    print("Step 1: Alert local swimmers")
    print("Step 2: Contact the Caribbean regional presence at +1 868 727 1926")
    print("Step 3: Contact the Caribbean Nature Conservancy at +1 305-445-8352")
    print("Lionfish are highly invasive species in the Caribbean and cause significant ecological and economic harm.")
else:
    print("Found {}".format(class_desc.lower()))


def send_daily_email():
    with open("lionfish_detection_counts.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        total_lionfish_spotted = 0
        for row in csvreader:
            total_lionfish_spotted += int(row["Count"])

        subject = "Daily Lionfish Count Report"
        message = f"Total lionfish spotted today: {total_lionfish_spotted}."
        send_email(subject, message)


# Function to get the current time in seconds until midnight
def seconds_until_midnight():
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    midnight = datetime.datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day, hour=0, minute=0, second=0)
    return int((midnight - now).total_seconds())


# Send the daily email at 11:59 PM
while True:
    time.sleep(seconds_until_midnight())  # Sleep until midnight
    send_daily_email()




