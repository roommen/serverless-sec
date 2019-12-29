import os
import subprocess
from flask import jsonify

def sub_proc_invocation(request):
    subprocess.Popen('touch /tmp/child', shell=True)

    os.system('ps auwx > /tmp/process.txt')
    f = open('/tmp/process.txt', 'r')
    
    # change the proc id to 11 or 12 from the output above. That's usually the process id of /env/bin/python3.7
    os.system('pstree -aps 11 > /tmp/processTree.txt')
    f2 = open('/tmp/processTree.txt', 'r')

    return jsonify(str(f.read()) + str(f2.read()))
