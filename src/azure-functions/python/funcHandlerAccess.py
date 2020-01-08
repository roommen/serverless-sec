import json
import os

def lambda_handler(event, context):
    os.system('cat /var/task/lambda_function.py > /tmp/code.txt')
    f = open("/tmp/code.txt", "r")
    
    return {'code': str(f.read())}
