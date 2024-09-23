import os
import shutil
import stat  # Import the stat module
from git import Repo

def handle_remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)  # Change file permission to writable
    func(path)

def clone_repository(git_url):
    repo_dir = "./cloned_repo"
    
    if os.path.exists(repo_dir):
        print("Repository already exists. Deleting existing repository...")
        shutil.rmtree(repo_dir, onerror=handle_remove_readonly)  # Delete the existing repository with error handling
    
    Repo.clone_from(git_url, repo_dir)
    print(f"Cloned repository to {repo_dir}")
    return repo_dir
