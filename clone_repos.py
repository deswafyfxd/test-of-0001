import os
import subprocess

def clone_repo(repo_url, base_name, start_number, count, bitbucket_username, bitbucket_password, bitbucket_project):
    for i in range(start_number, start_number + count):
        clone_name = f"{i:04d}-of-{base_name}"  # Changed to keep '-of-01' constant
        subprocess.run(["git", "clone", repo_url, clone_name])
        os.chdir(clone_name)
        edit_file('one.sh', f"{i:04d}-of-one")  # Edit the file after cloning to reflect 0001-of-one pattern
        
        # Set Git user identity
        subprocess.run(["git", "config", "user.email", "you@example.com"])
        subprocess.run(["git", "config", "user.name", "Your Name"])
        
        # Update remote URL for Bitbucket
        bitbucket_repo_url = f"https://{bitbucket_username}:{bitbucket_password}@bitbucket.org/{bitbucket_project}/{clone_name}.git"
        subprocess.run(["git", "remote", "set-url", "origin", bitbucket_repo_url])
        
        subprocess.run(["git", "add", "one.sh"])
        subprocess.run(["git", "commit", "-m", "Update one.sh"])
        subprocess.run(["git", "push", "-u", "origin", "main"])
        os.chdir("..")

def edit_file(file_path, clone_name):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Edit: replace instances of "0001-of-one" with the clone name
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line.replace("0001-of-one", clone_name))

if __name__ == "__main__":
    repo_url = "https://github.com/your-username/your-repo.git"
    base_name = "01"  # The base name from your example
    start_number = 18  # Starting number, for example 0001
    count = 3  # Number of clones to create
    bitbucket_username = os.getenv('BITBUCKET_USERNAME')
    bitbucket_password = os.getenv('BITBUCKET_APP_PASSWORD')  # Update to match GitHub secret name
    bitbucket_project = "your-bitbucket-project"  # Replace with your Bitbucket project name
    clone_repo(repo_url, base_name, start_number, count, bitbucket_username, bitbucket_password, bitbucket_project)
