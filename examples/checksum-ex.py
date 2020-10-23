import genchecksum as checksum
import os

print("Generate Checksum of Directory")

path = input("Input the path of the directory: ")

hashType = input("md5? sha1? or sha256?: ").lower()

recursive = input("Recursive? (True or False): ").lower()

if recursive == 'false':
    isIgnoreFile = input("Read from an ignore_file? (True or False): ").lower()

    if isIgnoreFile == 'true':
        ignoreFilePath = input("Ignore File Path? (skip if .gitignore exists in same directory): ")
    else: ignoreFilePath = None
else:
    isIgnoreFile = False
    ignoreFilePath = None

ifCSVWrite = input("Write to CSV file? (True or False): ").lower()

if ifCSVWrite == 'true':
    CSVFilePath = input("CSV File Name/Path: ")
    if not os.path.isfile(CSVFilePath):
        CSVFilePath = os.path.join(os.path.dirname(__file__), CSVFilePath)
else: CSVFilePath = None

abspath = input("Use absolute path? (True or False): ").lower()
if abspath == 'true':
    abspath = True
else: abspath = False

bufferSize = int(input("Buffer Size? (int): "))

if hashType == 'md5':
    md5 = checksum.md5.dir_sum(bufferSize, path, isIgnoreFile, ignoreFilePath)
    if recursive == 'true':
        md5.recursive_checksum_dir(ifCSVWrite, abspath, CSVFilePath)
    elif recursive == 'false':
        md5.checksum_dir(ifCSVWrite, abspath, CSVFilePath)
elif hashType == 'sha1':
    sha1 = checksum.sha1.dir_sum(bufferSize, path, isIgnoreFile, ignoreFilePath)
    if recursive == 'true':
        sha1.recursive_checksum_dir(ifCSVWrite, abspath, CSVFilePath)
    elif recursive == 'false':
        sha1.checksum_dir(ifCSVWrite, abspath, CSVFilePath)
elif hashType == 'sha256':
    sha256 = checksum.sha256.dir_sum(bufferSize, path, isIgnoreFile, ignoreFilePath)
    if recursive == 'true':
        sha256.recursive_checksum_dir(ifCSVWrite, abspath, CSVFilePath)
    elif recursive == 'false':
        sha256.checksum_dir(ifCSVWrite, abspath, CSVFilePath)

input("Press ENTER to close")

