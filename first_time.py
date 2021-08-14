from selenium import webdriver
import smtplib
import json
import logging
import boto3
from botocore.exceptions import ClientError
import os

def first_run(url):
    driver.get(url)

    button = driver.find_element_by_name('submit')
    button.click()

    elements = driver.find_elements_by_class_name("latestnews_exams")
   
    i = 0
    data = {}
    for block in elements:
        a_tags = block.get_attribute("href")
        if a_tags != None :
            i += 1
            data[i] = a_tags
           

    file_name = 'latest.json'
    bucket = 'notifications-alert'
    object_name = 'latest.json'

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
           
    with open("latest.json", "w") as outfile:
        json.dump(data, outfile)
   
    


if __name__ == "__main__":
    webdriver_path = "chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=webdriver_path)

    url = "https://anits.edu.in/home.php"

    first_run(url)
    driver.close()

