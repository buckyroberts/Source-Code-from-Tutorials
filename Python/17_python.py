def add_numbers(*args):
  total = 0
  for a in args:
    total += a
  print(total)

add_numbers(3)
add_numbers(3, 32)
add_numbers(3, 43, 5453, 354234, 463463)
