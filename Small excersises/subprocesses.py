'''

'''

import subprocess
import os

# env = os.environ
# # subprocess.run(["date"], shell=True)

# result = subprocess.run(["host", "8.8.8.8"], capture_output=True, shell=True, env=env)
# print(result)

stream = os.popen('echo Returned output')
output = stream.read()
print(output)

process = subprocess.Popen(['ping', '-c 4', 'python.org'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

while True:
    output = process.stdout.readline()
    print(output.strip())
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output 
        for output in process.stdout.readlines():
            print(output.strip())
        break