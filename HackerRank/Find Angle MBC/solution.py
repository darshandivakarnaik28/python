# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = float(input())
bc = float(input())

angle_rad = math.atan2(ab, bc)
angle_deg = round(math.degrees(angle_rad))

print(f"{angle_deg}\u00b0")
