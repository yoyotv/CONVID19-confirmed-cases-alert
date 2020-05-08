# CONVID19-confirmed-cases-alert
An auto alert push a slack message about convid-19 confirmed cases.


1. Use a python script to scratch the CONVID-19 information on Taiwan CDC center.

2. Send the information to "someone" on slack via webhook (https://api.slack.com/messaging/webhooks)

3. Using airflow to schedue the process everyday. 

Remember to let airflow get the permission of test.sh (chmod +x /home/ucare/test.sh)


## Demo
<p align="center">
  <img src="https://github.com/yoyotv/CONVID19-confirmed-cases-alert/blob/master/demo/demo_1.jpg" width="420" height="900">
</p>


<p align="center">
  <img src="https://github.com/yoyotv/CONVID19-confirmed-cases-alert/blob/master/demo/airflow.png" width="1200" height="300">
</p>
