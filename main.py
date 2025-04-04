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

results = run_grading("webtech-journey", repo_name)


feedback = report_generator.create_feedback(results)

g = Github(github_token)
repo = g.get_repo(repo_name)

report_generator.overwrite_report_in_readme(author, feedback, results)
overwrite_report_in_repo(repo,new_content=feedback)

notify_classroom(sum([25 if result else 0 for result in results]), github_token)