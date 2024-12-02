from util import text_file_opener
left_list, right_list = text_file_opener('advent_of_code/1_december.py/input.txt')

occuranc_scor = 0

for i in left_list:
    cou = right_list.count(i)
    occuranc_scor += (cou * i)

print(f"the occurance score is: {occuranc_score}")
    