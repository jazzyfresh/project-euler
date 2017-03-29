#!/usr/bin/env ruby

MAX = 4000000
sum = 0
n1 = 1
n2 = 2

while (n1 < MAX)
  sum += n1 if n1 % 2 == 0
  new_n1 = n2
  n2 = n2 + n1
  n1 = new_n1
end

print sum, "\n"
