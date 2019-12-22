Following exploit files are present:

1. `fullNetCon.py` - Full internet access from within the FaaS

2. `funcHandlerAccess.py` - Ability to access the function handler of the executing serverless function

3. `subProcInvocation.py` - Demonstrates sub processes to be invoked at will from within the executon context

4. `systemCmd.py` - Execution of os.system() commands at will which is a major security risk

5. `tmpFolderReadWrite.py` - /tmp access to manipulate contents during the execution
