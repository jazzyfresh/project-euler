#!/usr/bin/env python

HI = 999
LO = 99
i = HI
j = HI

palindromes = []

# does unnecessary iterations, does it twice for mirror numbers
while i > LO:
  while j > LO:
    n = i * j
    # feel like there should be a way to do this w/ math...
    n_str = str(n)
    if n_str[::-1] == n_str:
      palindromes.append(n)
      break
    j = j - 1
  j = HI
  i = i - 1

palindromes.sort()
print palindromes[-1]
