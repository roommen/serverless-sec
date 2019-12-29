import os
from flask import jsonify

def system_cmd(request):
    # sample os.system invocation
    os.system('ls -l /tmp/ > /tmp/output.txt; ls -l /var >> /tmp/output.txt')
    os.system('ps auwx >> /tmp/output.txt')

    f = open("/tmp/output.txt", "r")
    
    # Uncomment below line to kill the python proc itself
    # os.system('pkill python3.7')
    return jsonify(str(f.read()))
