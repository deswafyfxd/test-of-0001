import os
import subprocess

def clone_repo(repo_url):
    """
    Clone a repository from the given URL.
    
    Args:
    repo_url (str): The URL of the repository to be cloned.
    """
    
    try:
        # Run the git clone command
        result = subprocess.run(['git', 'clone', repo_url], check=True)
        print(f"Repository cloned successfully: {repo_url}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while cloning the repository: {e}")
        
# Example usage
if __name__ == "__main__":
    repo_url = os.environ.get('REPO_URL')
    if repo_url:
        clone_repo(repo_url)
    else:
        print("Repository URL not provided.")
