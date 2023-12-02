from pandas import *
import re
files_data = read_csv("./Data_sheets/Advent_of_Code_23_sheets - Day_1 (1).csv")
files = files_data['text'].tolist()

nums_dict = {"zero":0, "one": 1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
test_list = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
def sum_list(text):
  # Split each value by number to nested list
  result_list = [re.split('(\d+)',cal) for cal in text]
  print(result_list)
  pattern = re.compile(r'[a-zA-z]+')
  result = []
  for sublist in result_list:
    convert_sub = []
    for item in sublist:
      if isinstance(item, int):
        convert_sub.append(item)
      elif isinstance(item, str) and item.isdigit():
        convert_sub.append(int(item))
      else:
        convert_sub.append(item)
    result.append(convert_sub)
  print(result)




print(sum_list(test_list))




#   result = []
#   count = 0
#   for x in text:
#     y = re.sub(r"[^\d]", "", x)
#     result.append(y)
#   print(result)
#   for i in result:
#     if len(i) <= 1:
#       j = i+i
#       print(j)
#       count += int(j)
#     else:
#       k =(i[0]) + (i[-1])
#       print(k)
#       count += int(k)
#   return count
# print(sum_list(files))
