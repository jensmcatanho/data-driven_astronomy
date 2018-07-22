import numpy as np

def angular_dist(r1, d1, r2, d2):
  r1_rad = np.radians(r1)
  d1_rad = np.radians(d1)
  r2_rad = np.radians(r2)
  d2_rad = np.radians(d2)
  
  a = np.sin(np.abs(d1_rad - d2_rad) * 0.5) ** 2
  b = np.cos(d1_rad) * np.cos(d2_rad) * (np.sin(np.abs(r1_rad - r2_rad) * 0.5) ** 2)
  d = 2 * np.arcsin(np.sqrt(a + b))
  
  return np.degrees(d)

if __name__ == '__main__':
  # Test Case 1
  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  # Test Case 2
  print(angular_dist(10.3, -3, 24.3, -29))
