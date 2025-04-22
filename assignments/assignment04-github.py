# assignment04-github.py
# Description:
# By Noemi Diaz


# Step 1: Install PyGithub in Python using terminal (python -m pip install PyGithub)



# Step 2: Create a Github Token

# Step 3: Python code to access test.txt

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from github import Github
from assignments.config import config as cfg

apikey = cfg["githubkey"]
 
# Using own key
g = Github(apikey)
for repo in g.get_user().get_repos():
 print(repo.name)

# Recconecting to Github and specific repository
g = Github(apikey)
repo = g.get_repo("Noemidiaz/lab-PyGithub")

# Getting information about the file
fileInfo = repo.get_contents("test.txt")
print(fileInfo)

# Direct download URL of the file and prints it
urlOfFile = fileInfo.download_url
print(urlOfFile)

# Printing the clone URL of the repository
print(repo.clone_url)
