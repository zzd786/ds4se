import pandas as pd
import re
from pydriller import Repository

# Local repo
assignment_repo = r"E:\ds4se_assignment1\ds4se\hadoop"

df = pd.read_excel('hdfs_id.xlsx')

# Reading Issue IDs from a column named 'Key'
issue_ids = df['Key'].tolist()
print(issue_ids)

# Dicts to hold the results
issue_commits = {}
parent_commits = {}

# Mine the local repository
for commit in Repository(assignment_repo).traverse_commits():
    for issue_id in issue_ids:
        # Check if the issue ID is in the commit message using regex
        if re.search(r'\b' + issue_id + r'\b', commit.msg):
            # Store the commit hash of issues and it's Parent
            issue_commits[issue_id] = commit.hash, commit.committer_date
            parent_commits[commit.hash] = [parent for parent in commit.parents], commit.committer_date

print(issue_commits)
print(parent_commits)

# Dicts to DF and saving in CSV
pd.DataFrame(list(issue_commits.items()), columns=['Issue_ID', 'Commit']).to_csv('issue_commits.csv', index=False)
pd.DataFrame(list(parent_commits.items()), columns=['Commit', 'Parents']).to_csv('parent_commits.csv', index=False)


# Dicts to DF and saving in Sorted CSV
issue_commits_df = pd.DataFrame(list(issue_commits.items()), columns=['Issue_ID', 'Commit'])
issue_commits_df[['Commit_hash', 'Date']] = pd.DataFrame(issue_commits_df['Commit'].tolist(), index=issue_commits_df.index)
issue_commits_df = issue_commits_df.sort_values(by='Date', ascending=False)
issue_commits_df.to_csv('sorted_issue_commits.csv', index=False)

parent_commits_df = pd.DataFrame(list(parent_commits.items()), columns=['Commit', 'Parents'])
parent_commits_df[['Parents', 'Date']] = pd.DataFrame(parent_commits_df['Parents'].tolist(), index=parent_commits_df.index)
parent_commits_df = parent_commits_df.sort_values(by='Date', ascending=False)
parent_commits_df.to_csv('sorted_parent_commits.csv', index=False)
