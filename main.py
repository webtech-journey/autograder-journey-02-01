import argparse
from tests import run_grading
import os
from export import notify_classroom
import report_generator
from github import Github
from commit_report import overwrite_report_in_repo
# Set up argument parser
parser = argparse.ArgumentParser(description="Process token argument.")
parser.add_argument("--token", type=str, required=True, help="GitHub token")
args = parser.parse_args()

repo_name = os.getenv("GITHUB_REPOSITORY")
github_token = args.token  # Use the token argument from argparse
author = os.getenv("GITHUB_ACTOR")
org = repo_name.split('/')[0]
results = run_grading(org, repo_name)


feedback = report_generator.create_feedback(results)
report_md = report_generator.generate_markdown_report_pt(author,feedback,results)

g = Github(github_token)
repo = g.get_repo(repo_name)

overwrite_report_in_repo(repo,new_content=report_md)

notify_classroom(sum([25 if result else 0 for result in results]), github_token)