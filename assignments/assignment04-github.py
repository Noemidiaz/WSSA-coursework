# assignment04-github.py
# Description:
# By Noemi Diaz


# Step 1: Install PyGithub in Python using terminal (python -m pip install PyGithub)



# Step 2: Create a Github Token

# Step 3: Python code to access test.txt

from github import Github
from config import config as cfg

apikey = cfg["githubkey"]

# Using own key
g = Github(apikey)
for repo in g.get_user().get_repos():
 print(repo.name)

 #