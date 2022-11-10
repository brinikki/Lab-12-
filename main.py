a_dictionary = {
  'Ethics in Technology' : 1, 
  'Intro to Psych.': 2, 
  'Calc I': 3, 
  'Engineering Physics': 4, 
  'Physical Ed.': 5, 
  'Intro to Scripting': 6}

max = 3
min = 50000
my_counter = 0
big_sum = 0
for key in a_dictionary:
  if a_dictionary[key] > max:
      max = a_dictionary[key]
  if a_dictionary[key] < min:
      min = a_dictionary[key]
my_counter = my_counter + 1
big_sum = big_sum + a_dictionary[key]
print(big_sum)