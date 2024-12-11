import os
import subprocess

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command {' '.join(command)}: {result.stderr}")
    return result

def clone_repo(repo_url, base_name, start_number, count, bitbucket_username, bitbucket_password, bitbucket_organization):
    for i in range(start_number, start_number + count):
        clone_name = f"{i:04d}-of-{base_name}"
        run_command(["git", "clone", repo_url, clone_name])
        os.chdir(clone_name)
        
        # Set Git user identity
        run_command(["git", "config", "user.email", "you@example.com"])
        run_command(["git", "config", "user.name", "Your Name"])
        
        # Construct Bitbucket repository URL
        bitbucket_repo_url = f"https://{bitbucket_username}:{bitbucket_password}@bitbucket.org/{bitbucket_organization}/{clone_name}.git"
        print(f"Setting remote URL: {bitbucket_repo_url}")
        
        run_command(["git", "remote", "set-url", "origin", bitbucket_repo_url])
        run_command(["git", "push", "-u", "origin", "main"])
        
        os.chdir("..")

if __name__ == "__main__":
    repo_url = "https://neon005lite@bitbucket.org/ifx4gyrc3g3y8kug9by597xrcgdxc/0015-of-01.git"
    base_name = "01"
    start_number = 18
    count = 3  # Number of clones to create
    bitbucket_username = os.getenv('BITBUCKET_USERNAME')
    bitbucket_password = os.getenv('BITBUCKET_APP_PASSWORD')
    bitbucket_organization = "ifx4gyrc3g3y8kug9by597xrcgdxc"
    clone_repo(repo_url, base_name, start_number, count, bitbucket_username, bitbucket_password, bitbucket_organization)
