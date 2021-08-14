<h4> DESCRIPTION </h4>

This is a customized script that notifies a given list of people via email, when there are any new notifications on my college website "https://anits.edu.in/home.php" in the 'latest news' section.
To do so, the 'latest.json' file containing the web scrapped data is hosted on AWS S3 bucket, that lets you store all latest news available.

The 'first_time.py' script will run only once which PUTs the data into a S3 bucket in JSON format.

The 'notify_me.py' script does the following functions:
* It will GET the data from S3 bucket, web scrapes the present web page and checks if there are any updates
    * if so:
        * It will [notify] the [listed people]
        * It will update all the changes 
* Finally it will PUT the latest data available back into the S3 bucket. </ul>
The above scripts have been hosted on AWS EC2 instance. Since these scripts have to run timely, a timer is scheduled by windows Task Scheduler that runs these scripts every hour according to the timer set.

