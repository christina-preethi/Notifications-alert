from selenium import webdriver
import smtplib
import json
import logging
import boto3
from botocore.exceptions import ClientError
import os

def notify_all(new_link):
    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()
  

    s.login("christina.ncp@gmail.com", "christina@@")
    sender = 'christina.ncp@gmail.com'
    receiver = ['nchristinapreethi.18.cse@anits.edu.in', 'christina.ncp@gmail.com']
    # message to be sent
    message = "There is an update on the website!!\n"+new_link+" has been added!!"
    
    # sending the mail
    s.sendmail(sender, receiver, message)
    
    # terminating the session
    s.quit()

def update_latest(data):
    with open("latest.json", "w") as outfile:
        json.dump(data, outfile)

    
    file_name = 'latest.json'
    bucket = 'notifications-alert'
    object_name = 'latest.json'

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)



def check_new(url):
    driver.get(url)

    button = driver.find_element_by_name('submit')
    button.click()

    elements = driver.find_elements_by_class_name("latestnews_exams")

    s3 = boto3.client('s3')
    file_name = 'latest.json'
    bucket = 'notifications-alert'
    object_name = 'latest.json'

    json_object = s3.download_file(bucket, object_name, file_name)

    with open('latest.json', 'r') as openfile:
  
        json_object = json.load(openfile)

    values = json_object.values()

    data = {}
    i = 0
    for block in elements:
        a_tags = block.get_attribute("href")

        if a_tags == None:
            continue
        i += 1
        data[i] = a_tags
        if a_tags  in values:
            continue
        print("It will be notified")
        notify_all(a_tags)
        print("It is notified")
        print(a_tags)

    update_latest(data)

if __name__ == '__main__':
    webdriver_path = "chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=webdriver_path)

    url = "https://anits.edu.in/home.php"

    check_new(url)

driver.close()