import subprocess

#Invoke an exe and wait for it to return
subprocess.call(["packer.exe", "validate", file])

#Invoke an exe and wait for it to return. On return the exit code will be checked
#If the return code is non-zero a CalledProcessError is raised
subprocess.check_call(["packer.exe", "validate", file])