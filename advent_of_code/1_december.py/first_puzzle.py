from util import text_file_opener
left_list, right_list = text_file_opener('advent_of_code/1_december.py/input.txt')

left_list.sort()
right_list.sort()

multiplied_list = sum(abs(a-b) for a,b in zip(left_list, right_list))

print(f"caluclated distance is: {multiplied_list}")