import os
import subprocess

def clone_repo(repo_url, custom_name):
    """
    Clone a repository from the given URL into a custom directory.
    
    Args:
    repo_url (str): The URL of the repository to be cloned.
    custom_name (str): The name of the directory to clone the repository into.
    """
    
    try:
        # Run the git clone command with custom directory name
        result = subprocess.run(['git', 'clone', repo_url, custom_name], check=True)
        print(f"Repository cloned successfully into {custom_name}: {repo_url}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while cloning the repository: {e}")
        
# Example usage
if __name__ == "__main__":
    repo_url = os.environ.get('REPO_URL')
    custom_name = os.environ.get('CUSTOM_NAME', 'cloned_repo')
    if repo_url:
        clone_repo(repo_url, custom_name)
    else:
        print("Repository URL not provided.")
