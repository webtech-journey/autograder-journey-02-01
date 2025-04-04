from github import Github
import base64
def overwrite_report_in_repo(repo,file_path="relatorio.md", new_content=""):
    try:
        # Get the current file content (if it exists)
        try:
            file = repo.get_contents(file_path)
            file_sha = file.sha
        except:
            # If the file doesn't exist, no sha is retrieved
            file_sha = None

        # Encode the updated content in base64
        updated_content_encoded = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')

        # Commit the new content to the repository (either overwrite or create new)
        commit_message = "Overwrite relatorio.md with new grading report"
        if file_sha:
            repo.update_file(file_path, commit_message, updated_content_encoded, file_sha)
        else:
            repo.create_file(file_path, commit_message, updated_content_encoded)

        print(f"Report successfully overwritten in {file_path}")
    except Exception as e:
        print(f"Error while updating {file_path}: {str(e)}")