from flask import jsonify

# Accessing the disk scratch space of GCF
def tmp_folder_read_write(request):
    f = open("/tmp/demofile.txt", "w")
    f.write("Sample file content inside the local disk mount point (/tmp) of GCF execution env")
    f.close()

    f = open("/tmp/demofile.txt", "r")
    return jsonify(str(f.read()))
