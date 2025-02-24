import hashlib
import os
from collections import Counter


def compute_file_hash(file_path, algorithm='md5'):
    """Compute the hash of a file using the specified algorithm.
    hash_func = hashlib.new(algorithm)
    The named constructors are much faster than new() and should be preferred:
    md5(), sha1(), sha224(), sha256(), sha384(), and sha512() """
    hash_func = hashlib.md5()

    
    with open(file_path, 'rb') as file: # read binary mode
        while chunk := file.read(8192):  # Read the file in chunks of 8192 bytes. new syntax := that assigns values to variables as part of a larger expression. It is affectionately known as “the walrus operator”
            hash_func.update(chunk)
    
    return hash_func.hexdigest()


def list_all_files_in_folder(path):
    # os.walk() yields two lists for each directory it visits -- one for files and one for dirs.
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for file in filenames:
            file_list.append(os.path.join(dirpath, file))
    return file_list


def find_files_with_same_hash(dict):
    # finding duplicate values from dictionary using Counter
    count_dict = Counter(dict.values())
    result = [key for key, value in dict.items() if count_dict[value] > 1]
    print("duplicate files", str(result))


def main():
    folder_path = "E:\\lulz"
    algorithm = "sha256"
    file_names = list_all_files_in_folder(folder_path)
    hash_dict = {}
    file_counter = 1

    for file in file_names:
        file_hash = compute_file_hash(file, algorithm)
        #print(f"The {algorithm} hash of the file is: {file_hash}")
        hash_dict[file] = file_hash
        print(f"Reading file {file_counter} of {len(file_names)}")
        file_counter += 1

    find_files_with_same_hash(hash_dict)

if __name__ == "__main__":
    main()