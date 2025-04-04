from tests import run_grading
import os
from export import notify_classroom
import report_generator

repo_name = os.getenv("GITHUB_REPOSITORY")
github_token = os.getenv('GITHUB_TOKEN')
author = os.getenv("GITHUB_ACTOR")
results = run_grading("webtech-journey",repo_name) 

notify_classroom(sum([25 if result else 0 for result in results]),github_token)

feedback = report_generator.create_feedback(results)
report_generator.overwrite_report_in_readme(author,feedback,results)