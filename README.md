# Analysis of silo formation of political thought in TikTok

This is a research project investigating the phenomenon of political siloing on TikTok, focusing on the personalization algorithm of the platform and the formation of echo chambers. This project was conducted as part of my research course under the supervision of Prof. Vybihal at McGill University. The final report on the project can be found [here](https://github.com/ArpanSaha07/Siloing-of-Political-Thought-in-TikTok/blob/main/Arpan_Saha_COMP400.pdf).

## Introduction
In today's world social media plays a pivotal role in shaping political discourse. Thus, understanding how platforms like TikTok contribute to the polarization of political thought is crucial. We also aimed to get a glimpse at how social media algorithms put us into self-affirmative echo chambers, potentially polarizing viewpoints of the social media users and creating further divide between consumers of content from different silos.

 ## Experiment Setup
At first we conducted a survey of TikTok users on their usage behaviours of the app.

We wrote scripts to automate TikTok login and then to emulate the use of TikTok app. The emulation was based on the data gathered from the survey in order to mimic the usage behaviour of the target group.

The experiment was conducted in various sessions involving [bots](https://github.com/ArpanSaha07/Siloing-of-Political-Thought-in-TikTok/tree/main/bot_info), each with a set of preferences based on the survey results in order to test TikTok's personalization algorithm. The data of the usage during the experiment was stored in [csv files](https://github.com/ArpanSaha07/Siloing-of-Political-Thought-in-TikTok/tree/main/video_watch_info).

## Survey
We conducted a survey on TikTok users to collect data of TikTok usage behaviors in order to cross-reference with our experiment results and test our hypothesis. Description of the survey setup can be found on the report. The survey results can be found [here](https://github.com/ArpanSaha07/Siloing-of-Political-Thought-in-TikTok/tree/main/survey_results).

## Bot Algorithm
[Here](https://github.com/ArpanSaha07/Siloing-of-Political-Thought-in-TikTok/blob/main/diagrams/bot_diagram.png) you can find an overview of the algorithm used to dictate the TikTok usage behaviours of the bots during the experiments. Detailed explanation of the algorithm, the login and data scrapper code, and implementation of the bots can be found on the report.

## Results
The data and statistics of TikTok usage by the bot algorithms can be found in this [folder](https://github.com/ArpanSaha07/Siloing-of-Political-Thought-in-TikTok/tree/main/video_watch_info). The data were used to test our hypothesis and form conclusions.

## Running the script
If you are interested in running the bot algorithm:

You need to install an internet browser app and create a TikTok account before running the script.

The data scrapper has been tested to run TikTok in the Chrome browser (version=124) and TikTok (version from April 2024). 

The HTML tags in the code might need to be tweaked to run more recent versions of TikTok or to run in a different browser.
Enter the following commands in the command line:
```
pip install -r requirements.txt
py login.py
```
This will require you to solve any login puzzle manually.

To run the script using automatic TikTok login puzzle solver:
Signup on URL{https://rapidapi.com/}
Get an API key from https://rapidapi.com/reversecoders/api/flycaptcha
Then run `py TikTokCaptchaSolver.py`


## Acknowledgement
Special thanks to Tales Trindade Henriques L. Andrade (McGill Winter 2024) and Yanbo Wang (McGill Winter 2025) for collaborating on this project.
