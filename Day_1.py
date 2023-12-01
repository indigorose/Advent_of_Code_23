from pandas import *
import re
files_data = read_csv("./Data_sheets/Advent_of_Code_23_sheets - Day_1 (1).csv")
files = files_data['text'].tolist()

def sum_list(text):
  result = []
  count = 0
  for x in text:
    y = re.sub(r"[^\d]", "", x)
    result.append(y)
  print(result)
  for i in result:
    if len(i) <= 1:
      j = i+i
      print(j)
      count += int(j)
    else:
      k =(i[0]) + (i[-1])
      print(k)
      count += int(k)
  return count
print(sum_list(files))
