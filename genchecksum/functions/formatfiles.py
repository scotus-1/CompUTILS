import csv


def csv_writer(material, csv_filename):
    with open(f'{csv_filename}.csv', 'a') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow(material)


def format_csv(csv_file_path):
    with open(csv_file_path, 'r') as file:
        csvList = file.readlines()
        for index, line in enumerate(csvList):
            if line == '\n':
                del csvList[index]
        with open(csv_file_path, 'w') as newFile:
            for key in csvList:
                newFile.write(key)


def format_ignore(ignore_file_path):
    try:
        with open(ignore_file_path, 'r') as ignoreFile:
            ignoreList = ignoreFile.readlines()
            for index, line in enumerate(ignoreList):
                if line.startswith('#') or line == "\n":
                    del ignoreList[index]
                    continue
                ignoreList[index] = line.rstrip("\n")
        return ignoreList
    except FileNotFoundError:
        print(f"{ignore_file_path} Not Found")
        return None