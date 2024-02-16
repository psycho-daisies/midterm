def readfile(file_name):
    arr1 = []
    # Open the file
    file = open(file_name, "r")
    # Read each line and add to array
    for line in file:
        # Append each line to the array
        arr1.append(line.strip())

    file.close()
    return arr1