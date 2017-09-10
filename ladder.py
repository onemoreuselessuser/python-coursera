import sys
steps = int(sys.argv[1])

i = 1

while i <= steps:
  print ((steps - i) * " " + i * "#")
  i = i + 1