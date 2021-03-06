`monkeyPatch.py` - Demonstrates a possible scenario with Python monkey patching that eclipses the current functionality of _os.system()_ with a new definition

Have this file included as part of the serverless package to patch the original functionality with the new behaviour. Following exploit files are present for **AWS Lambda**, **GCP CloudFunction** and **Azure Functions**:

1. `fullNetCon.py` - Full internet access from within the FaaS environment

2. `funcHandlerAccess.py` - Ability to access the function handler of the executing serverless function

3. `subProcInvocation.py` - Demonstrates sub processes to be invoked at will from within the execution context

4. `systemCmd.py` - Execution of os.system() commands at will which can become a major security risk

5. `tmpFolderReadWrite.py` - /tmp access to manipulate contents during execution time
