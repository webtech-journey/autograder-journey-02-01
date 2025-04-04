from tests import run_grading
import os
from export import notify_classroom
repo_name = os.getenv("GITHUB_REPOSITORY")
score = run_grading("webtech-journey",repo_name) 
github_token = os.getenv('GITHUB_TOKEN')

notify_classroom(score,github_token)
