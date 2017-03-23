#!/usr/bin/env python


def generate_collatz(n, l):
  l.append(n)
  if n % 2 == 0:
    return generate_collatz(n / 2, l)
  elif n == 1:
    return l
  else:
    return generate_collatz((3*n) + 1, l)

max_size = 0
longest_start = 0

for i in range(1, 1000000):
  l = generate_collatz(i, [])
  size = len(l)
  if size > max_size:
    max_size = size
    longest_start = i

print "longest start %d" % (longest_start, )
