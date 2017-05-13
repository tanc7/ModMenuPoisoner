import socket
import operator
import os
import sys
from termcolor import colored
import StringIO


official_repo_dir = '/root/Documents/GitHub/ModMenuPoisoner'
official_repo_url = 'https://github.com/tanc7/ModMenuPoisoner'
official_repo_branch = 'master'

def git_push(official_repo_branch):
    print colored('[*] Now pushing this repo as the new git update','yellow',attrs=['bold'])
    cmd_String = 'git push origin %s' % official_repo_branch
    os.system(cmd_String)
def git_remote_verify():
    text = colored('[*] Remotely verifying git repo','yellow',attrs=['bold'])
    print text
    cmd_String = 'git remote -v'
    os.system(cmd_String)
    git_push(official_repo_branch)
def git_remote_add(official_repo_url):
# root@Cylon-Basestar:~/Documents/GitHub/Arms-Commander# git remote add origin https://github.com/tanc7/Arms-Commander
    text = colored('[*] Adding URL as origin','yellow',attrs=['bold'])
    print text
    cmd_String = 'git remote add origin %s' % official_repo_url
    os.system(cmd_String)
    git_remote_verify()
    return official_repo_url

def git_commit():
    commit_name = str(raw_input("Enter a name for commit: "))
    text = colored('[*] Commiting local git repo as remote','yellow',attrs=['bold'])
    print text
    cmd_String = 'git commit -m "%s"' % commit_name
    os.system(cmd_String)
    git_remote_add(official_repo_url)
    return commit_name

def git_add(official_repo_dir):
    text = colored('[*] Adding local directory as a local git repo','yellow',attrs=['bold'])
    print text
    cmd_String = 'git add .'
    os.system(cmd_String)
    git_commit()
    return

def git_init(official_repo_dir):
    os.chdir(official_repo_dir)
    cmd_String = 'git init'
    os.system(cmd_String)
    git_add(official_repo_dir)
    return official_repo_dir

git_init(official_repo_dir)
