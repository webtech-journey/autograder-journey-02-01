import requests
import base64
def check_main_branch(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/branches/main"
    response = requests.get(url)
    return response.status_code == 200

def check_at_least_one_commit(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    response = requests.get(url)
    return len(response.json()) > 0

def check_resume_txt_exists(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/resumo.txt"
    response = requests.get(url)
    return response.status_code == 200

def check_resume_txt_lines(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/resumo.txt"
    response = requests.get(url)
    if response.status_code == 200:
        file_content = response.json()['content']
        decoded_content = base64.b64decode(file_content).decode('utf-8')
        return len(decoded_content.splitlines()) >= 3
    return False

def run_grading(repo_owner, repo_name):
    total_points = 0
    results = []
    # Check for main branch
    results.append(check_main_branch(repo_owner, repo_name))
    # Check for at least one commit
    results.append(check_at_least_one_commit(repo_owner, repo_name))

    # Check for resume.txt
    results.append(check_resume_txt_exists(repo_owner, repo_name))
    if results[2]:
        results.append(check_resume_txt_lines(repo_owner,repo_name))
    else:
        results.append(False)
    
    return results
