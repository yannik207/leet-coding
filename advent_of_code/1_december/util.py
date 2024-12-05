def text_file_opener(file_path: str):
    with open(file_path, 'r') as file:
        both_lists = file.read()
    
    lines = both_lists.strip().split("\n")

    left_list = [int(line.split()[0]) for line in lines]
    right_list = [int(line.split()[1]) for line in lines]
    return left_list, right_list