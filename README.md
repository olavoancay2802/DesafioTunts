# DesafioTunts

# Prerequisites

To run this project, you need the following prerequisites:

1. Python 2.6 or greater.

2. The <a href="https://pypi.org/project/pip/">pip</a> package management tool

3. Authorization credentials for a desktop application. To learn how to create credentials for a desktop application, refer to <a href="https://developers.google.com/workspace/guides/create-credentials">Create credentials.</a>

4. A Google account.

# How to run

1. To run the exercise, simply open your preferred command line shell of your Operational System(Windows Powershell or CMD).

2. Clone this repository with Git:

git clone https://github.com/olavoancay2802/DesafioTunts.git

3. After it gets downloaded, you'll have to install the dependencies first, open the project directory:

cd desafioTunts

4. Then, run

"python mainDesafio.py".

In some cases, you might have to run

"python3 mainDesafio.py"

4. (Optional) In case you get the following issue running the python script, go to the troubleshooting instructions below:

_Traceback (most recent call last):_
_File "mainDesafio.py", line 5, in <module>_
_from googleapiclient.discovery import build_
_ModuleNotFoundError: No module named 'googleapiclient'_

# Troubleshooting instructions:

_If you already have package manager "Pip" installed, simply run "pip install --upgrade google-api-python-client" from the command line._

\_Else, check the documentation at: https://pypi.org/project/pip/"
