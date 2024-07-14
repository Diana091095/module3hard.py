data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum_num = 0
def calculate_structure_sum(dont_understend):
    global sum_num
    if isinstance(dont_understend, int):
        sum_num += dont_understend
    elif isinstance(dont_understend, str):
        sum_num += len(dont_understend)
    elif isinstance(dont_understend, dict):
        for key, value in dont_understend.items():
            calculate_structure_sum(key)
            calculate_structure_sum(value)
    elif isinstance(dont_understend, (list, tuple, set)):
        for i in dont_understend:
            calculate_structure_sum(i)

for i in data_structure:
    calculate_structure_sum(i)

print(sum_num)


result = calculate_structure_sum(data_structure)
print(result)