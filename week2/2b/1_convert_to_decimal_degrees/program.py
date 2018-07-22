def hms2dec(h, m, s):
  return 15 * h + m * 0.25 + s/240
  
def dms2dec(d, m, s):
  return d + m/60 + s/3600 if d >= 0 else d - m/60 - s/3600

if __name__ == '__main__':
  # Test Case 1
  print(hms2dec(23, 12, 6))

  # Test Case 2
  print(dms2dec(22, 57, 18))

  # Test Case 3
  print(dms2dec(-66, 5, 5.1))