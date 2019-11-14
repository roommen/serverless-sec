import json
import os
import subprocess

def lambda_handler(event, context):
    os.system('cat /var/task/lambda_function.py > /tmp/code.txt')

    f = open("/tmp/code.txt", "r")
    # print(f.read())
    return {'code': str(f.read())}
