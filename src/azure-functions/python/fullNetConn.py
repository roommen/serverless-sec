import json
import os

def lambda_handler(event, context):
    os.system('curl google.com')
    os.system('curl aws.amazonaws.com')
    
    return True
