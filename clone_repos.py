import os
import subprocess

def clone_repo(repo_url, base_name, start_number, count, bitbucket_username, bitbucket_password, bitbucket_project_name):
    for i in range(start_number, start_number + count):
        clone_name = f"{i:04d}-of-{base_name}"
        subprocess.run(["git", "clone", repo_url, clone_name])
        os.chdir(clone_name)
        edit_file('one.sh', f"{i:04d}-of-one")
        
        # Set Git user identity
        subprocess.run(["git", "config", "user.email", "you@example.com"])
        subprocess.run(["git", "config", "user.name", "Your Name"])
        
        # Construct Bitbucket repository URL
        bitbucket_repo_url = f"https://{bitbucket_username}:{bitbucket_password}@bitbucket.org/{bitbucket_project_name}/{clone_name}.git"
        print(f"Setting remote URL: {bitbucket_repo_url}")
        result = subprocess.run(["git", "remote", "set-url", "origin", bitbucket_repo_url], capture_output=True, text=True)
        if result.stderr:
            print(f"Error setting remote URL for {clone_name}: {result.stderr}")
        
        result = subprocess.run(["git", "add", "one.sh"], capture_output=True, text=True)
        if result.stderr:
            print(f"Error adding one.sh for {clone_name}: {result.stderr}")
        
        result = subprocess.run(["git", "commit", "-m", "Update one.sh"], capture_output=True, text=True)
        if result.stderr:
            print(f"Error committing one.sh for {clone_name}: {result.stderr}")
        
        result = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
        if result.stderr:
            print(f"Error pushing to remote for {clone_name}: {result.stderr}")
        
        os.chdir("..")

def edit_file(file_path, clone_name):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Edit: replace instances of "0001-of-one" with the clone name
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line.replace("0001-of-one", clone_name))

if __name__ == "__main__":
    repo_url = "https://neon005lite@bitbucket.org/ifx4gyrc3g3y8kug9by597xrcgdxc/0015-of-01.git"
    base_name = "01"
    start_number = 18
    count = 3  # Number of clones to create
    bitbucket_username = os.getenv('BITBUCKET_USERNAME')
    bitbucket_password = os.getenv('BITBUCKET_APP_PASSWORD')
    bitbucket_project_name = "bashiawsmsr3gyt4buu6gry1fgd5c3tg0v6t9"
    clone_repo(repo_url, base_name, start_number, count, bitbucket_username, bitbucket_password, bitbucket_project_name)
