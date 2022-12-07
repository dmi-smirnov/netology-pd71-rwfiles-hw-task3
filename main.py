import os

def get_files_rows_amount(files_dir_path):
    files_names_list = os.walk(files_dir_path).__next__()[2]
    result = dict()
    for file_name in files_names_list:
        count = 0
        file_path = os.path.join(files_dir_path, file_name)
        with open(file_path) as file:
            for line in file:
                count += 1
        result[count] = file_name
    return result

def write_result_file(files_dir_path, result_file_path):
    files_rows_amount = get_files_rows_amount(files_dir_path)
    with open(result_file_path, 'w') as result_file:
        for rows_amount in sorted(files_rows_amount.keys()):
            file_name = files_rows_amount[rows_amount]
            file_path = os.path.join(files_dir_path, file_name)
            with open(file_path) as file:
                result_file.write(file_name + '\n')
                result_file.write(str(rows_amount) + '\n')
                for line in file:
                    result_file.write(line)
                result_file.write('\n')

def main():
    files_dir_name = 'files'
    result_file_name = 'result.txt'

    code_dir_path = os.path.dirname(__file__)
    files_dir_path = os.path.join(code_dir_path, files_dir_name)
    result_file_path = os.path.join(code_dir_path, result_file_name)

    write_result_file(files_dir_path, result_file_path)
    
main()