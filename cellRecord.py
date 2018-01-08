import json
records_str = ''
try:
    with open('records') as records_files:
        for each_line in records_files:
            records_str = records_str + each_line.strip()
        print(records_str)
        result_data = json.loads(records_str)
        print(result_data)
        for key in result_data.keys():
            if result_data[key]['name'] == 'file':
                print(result_data[key])
except IOError:
    print("this file is missing")