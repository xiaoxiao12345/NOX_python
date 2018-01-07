try:
    records_data = open("records")
    for each_line in records_data:
        try:
            print(each_line)
        except ValueError:
            pass
    records_data.close()
except IOError:
    print("this file is missing")