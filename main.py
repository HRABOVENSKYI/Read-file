MACHINE_NAME = b'205.189.154.54'
FILE_TYPE = b'.txt'
CODE_STATUS = b' 200 '
DATE = b'01/Jul/1995'

if __name__ == "__main__":
    count = 0

    # First method
    # Double '\\' in path to escape '\' sign
    file = open("C:\\Users\\teodo\\Downloads\\access_log_Jul95", "rb")

    for line in file.readlines():
        if MACHINE_NAME in line and \
                FILE_TYPE in line and \
                CODE_STATUS in line and \
                DATE in line:
            count += 1

    file.close()

    print(count)

    # Second method
    count = 0

    file = open("C:\\Users\\teodo\\Downloads\\access_log_Jul95", "rb")

    for line in file.readlines():
        line_elements = line.split(b' ')
        try:
            machine_name = line_elements[0]
            date = line_elements[3][1:12]
            file_type = line_elements[-4][-4:]
            code_status = line_elements[-2]
        except IndexError:
            machine_name, date, file_type, code_status = b'', b'', b'', b''

        if MACHINE_NAME == machine_name and \
                DATE == date and \
                FILE_TYPE == file_type and \
                CODE_STATUS[1:4] == code_status:
            count += 1

    file.close()

    print(count)
