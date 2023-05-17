import os
import subprocess

def git_push(commit_message, repo_link=None):
    if not os.path.exists('.git'):
        # If there is no initial repository, prompt for commit message and create a new repository
        subprocess.run(['git', 'init'])
        subprocess.run(['git', 'add', '.'])
        
        # Create README.md file if it doesn't exist
        if not os.path.exists('README.md'):
            with open('README.md', 'w') as readme_file:
                readme_file.write('Initial commit')
            subprocess.run(['git', 'add', 'README.md'])
        
        subprocess.run(['git', 'commit', '-m', commit_message])
        
        # Rename the branch from master to main
        subprocess.run(['git', 'branch', '-M', 'main'])
        
        if repo_link is not None:
            # Add the remote repository
            subprocess.run(['git', 'remote', 'add', 'origin', repo_link])
            
            # Check if existing credentials are available
            email = subprocess.check_output(['git', 'config', '--get', 'user.email']).decode().strip()
            password = subprocess.check_output(['git', 'config', '--get', 'user.password']).decode().strip()
            
            if email == '' or password == '':
                use_existing = False
            else:
                use_existing = input("Existing credentials found. Do you want to use them? (yes/no): ").lower() == "yes"
            
            if use_existing:
                print("Using existing credentials.")
            else:
                # Prompt for email and password
                email = input("Enter your GitHub email: ")
                password = input("Enter your GitHub password: ")
                
                # Configure Git to use the provided credentials
                subprocess.run(['git', 'config', '--local', 'user.email', email])
                subprocess.run(['git', 'config', '--local', 'user.password', password])
            
            # Push changes to the repository
            subprocess.run(['git', 'push', '-u', 'origin', 'main'])
    else:
        # If the repository already exists, just commit the changes
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', commit_message])

        if repo_link is not None:
            # Retrieve stored email and password
            email = subprocess.check_output(['git', 'config', '--get', 'user.email']).decode().strip()
            password = subprocess.check_output(['git', 'config', '--get', 'user.password']).decode().strip()
            
            if email == '' or password == '':
                use_existing = False
            else:
                use_existing = input("Existing credentials found. Do you want to use them? (yes/no): ").lower() == "yes"
            
            if use_existing:
                print("Using existing credentials.")
            else:
                # Prompt for email and password
                email = input("Enter your GitHub email: ")
                password = input("Enter your GitHub password: ")
                
                # Configure Git to use the provided credentials
                subprocess.run(['git', 'config', '--local', 'user.email', email])
                subprocess.run(['git', 'config', '--local', 'user.password', password])
            
            # Push changes to the repository
            subprocess.run(['git', 'remote', 'add', 'origin', repo_link])
            subprocess.run(['git', 'push', '-u', 'origin', 'main'])

# Example usage:
commit_msg = input("Enter commit message: ")
repo_url = input("Enter repository URL (leave blank if not initialized): ")

git_push(commit_msg, repo_url)
