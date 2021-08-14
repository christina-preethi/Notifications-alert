This is a customized script that notifies a set of people when there are any new notifications on a perticular website. Here the website used is my college website "https://anits.edu.in/home.php". This website has a special scrolling for displaying the latest news. If there is any update in the latest news section this scripts will notify you via email.
To do so, the file containing the data is hosted on AWS S3 bucket, that lets you store all latest news available.

The 'first_time.py' script will run only once which PUTs the data into a S3 bucket in JSON format.

The 'notify_me.py' script does the following functions:
* It will GET the data from S3 bucket and checks if there are any updates
    * if so:
        * It will notify the listed people
        * It will update all the changes 
* Finally it will PUT the latest data available back into the S3 bucket. </ul>
The above scripts have been hosted on AWS EC2 instance. Since these scripts have to run timely, a timer is set by windows Task Scheduler that runs these scripts every hour according to the timer set.
