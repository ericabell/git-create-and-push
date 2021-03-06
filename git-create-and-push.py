import os
import sys
import subprocess

def main():
    # assume we are in the directory we want to create a repo in

    # get the name of the directory
    repo_name = os.getcwd()

    # run git init
    print( subprocess.check_output(['git', 'init']))

    # create a README.md file with the name of the repo,
    # if it doesn't exist already
    print( subprocess.check_output(['touch', 'README.md']))

    # git add .
    print( subprocess.check_output(['git', 'add', '.']))

    # git commit -m "Initial commit"
    message = "Initial commit"
    print( subprocess.check_output(['git', 'commit', '-m', message]))

    # create the repo on github
    # curl -u 'USER' https://api.github.com/user/repos -d '{"name":"REPO"}'
    # still need to figure out how 2-factor auth/tokens would work...

    # git remote add origin URL
    print( subprocess.check_output(['git', 'remote', 'add', 'origin', github_url]))

    # git push origin master
    print( subprocess.check_output(['git', 'push', 'origin', 'master']))

if __name__ == "__main__":
    main()
