import os
import pandas as pd
import subprocess


#os.environ['PATH'] += os.pathsep + 'C:/ProgramData/chocolatey/lib/maven/apache-maven-3.9.6/bin'

# Loading Issue Commits CSV File
df_c = pd.read_csv('issue_commits.csv')
commit_issues_id = df_c['Issue_ID'].tolist()
commit_issues_hash = df_c['Commit'].tolist()

# Loading Parent Commits CSV File
df_p = pd.read_csv('parent_commits.csv')
child_commit = df_p['Commit'].tolist()
parent_commit = df_p['Parents'].tolist()

# Path to your project
local_repo = "D:/ds4se/hadoop"

# Loop over each commit
for commit in commit_issues_hash:
    os.chdir(local_repo)

    # Discard any local changes
    subprocess.run(['git', 'reset', '--hard'], check=True)

    # Checkout the commit
    subprocess.run(['git', 'checkout', commit], check=True)

    # Compiling the project using Maven
    subprocess.run(['mvn', 'clean', 'install'], check=True)
