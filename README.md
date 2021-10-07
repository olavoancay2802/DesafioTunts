# DesafioTunts

# Prerequisites

To run this project, you need the following prerequisites:

1. Python 2.6 or greater.

2. The <a href="https://pypi.org/project/pip/">pip</a> package management tool

3. Authorization credentials for a desktop application. To learn how to create credentials for a desktop application, refer to <a href="https://developers.google.com/workspace/guides/create-credentials">Create credentials.</a>

4. A Google account.

# How to run

1. Open your preferred command line shell from the Operational System (Windows Powershell, CMD, terminal, etc.).

2. Clone this repository with Git:

git clone https://github.com/olavoancay2802/DesafioTunts.git

3. After cloning the repo, you'll have to install Google's API Client for Python. Go to the project folder and run the following command:

cd desafioTunts
pip install --upgrade google-api-python-client

4. If you have not created the credentials yet, <a href="https://developers.google.com/workspace/guides/create-credentials">Create credentials.</a> After creating credentials, don't forget to generate token.json and rename the file to "token.json". After that, add the file to the project.

5. Then, run the command:

python mainDesafio.py
(In some cases, you might have to run "python3" instead of just "python").

# Troubleshooting instructions:

Else, check the documentation at: https://pypi.org/project/pip/"
