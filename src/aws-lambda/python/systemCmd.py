import json
import os

def lambda_handler(event, context):
    # sample os.system invocation
    os.system('cat /var/task/lambda_function.py > /tmp/code.txt')
    os.system('ls -l /tmp/')

    os.system('ps auwx')
    os.system('pkill python3.7')
