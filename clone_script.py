import os
import subprocess

def clone_repo(full_url, custom_name):
    """
    Clone a repository from the given URL into a custom directory.
    
    Args:
    full_url (str): The full URL with credentials of the repository to be cloned.
    custom_name (str): The name of the directory to clone the repository into.
    """
    
    try:
        # Run the git clone command with custom directory name
        result = subprocess.run(['git', 'clone', full_url, custom_name], check=True)
        print(f"Repository cloned successfully into {custom_name}: {full_url}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while cloning the repository: {e}")

# Example usage
if __name__ == "__main__":
    repo_url = os.environ.get('REPO_URL')
    username = os.environ.get('BITBUCKET_USERNAME')
    password = os.environ.get('BITBUCKET_APP_PASSWORD')
    custom_name = os.environ.get('CUSTOM_NAME', 'cloned_repo')

    if repo_url and username and password:
        full_url = f"https://{username}:{password}@{repo_url}"
        clone_repo(full_url, custom_name)
    else:
        print("Required environment variables are not provided.")
