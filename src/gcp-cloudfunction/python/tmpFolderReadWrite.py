import json
import os
import subprocess

def lambda_handler(event, context):
    f = open("/tmp/demofile.txt", "w")
    f.write("file content inside the /tmp of AWS lambda execution environment")
    f.close()

    f = open("/tmp/demofile.txt", "r")
    # print(f.read())
    return {'file': str(f.read())}
