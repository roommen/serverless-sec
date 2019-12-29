import os

def full_net_conn(request):
    os.system('curl google.com')
    return jsonify(str("curl of google.com"))
