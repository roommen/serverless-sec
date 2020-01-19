import os
import builtins

def nonworking_system(*args, **kwargs):
    global original_system
    original_system(print("Not supported!"), *args, **kwargs)

def safe_system(*args, **kwargs):
    global original_system
    original_system(*args, **kwargs)

if __name__ == "__main__":
    #Let's backup the original(in this case the os.system() method call)
    original_system = os.system
    os.system

    os.system = nonworking_system
    os.system
    # should throw error
    os.system("cd /tmp; touch `date +%s`")

    # should work
    safe_system("cd /tmp; touch `date +%s`")
