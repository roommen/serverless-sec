import json
import os
import subprocess

def lambda_handler(event, context):

    subprocess.Popen('touch /tmp/child', shell=True)

    os.system('ps auwx > /tmp/process.txt')
    f = open('/tmp/process.txt', 'r')
    print(f.read())
    f.close()
    
    # change the proc id to 7 or 8. That's usually the process id of /var/lang/bin/python3.7
    os.system('pstree -aps 7 > /tmp/processTree.txt')
    f = open('/tmp/processTree.txt', 'r')
    print(f.read())
    f.close()

    return True
