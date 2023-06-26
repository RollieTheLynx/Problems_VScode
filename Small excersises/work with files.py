# file = open('README.md', encoding='utf8')
# print(file.readline().strip())
# print(file.readline())
# file.close()

# with open('README.md', encoding='utf8') as file2:
#     print(file2.read()) # с текущей строки до конца файла

import os
import sys
print(sys.argv)
filename = sys.argv[0]

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("New file created\n")
else:
    print('Error, the file {} already exists!'.format(filename))
    sys.exit(1)
    