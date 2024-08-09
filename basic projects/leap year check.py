print("welcome  to the leap year checker")

year = int(input("what is the year? "))
if year % 4 == 0:
 print(f"  {year} is a leap year")
 if year % 100 == 0:
  print(f" {year} is a leap year")
  if year % 400 == 0:
    print(f"{year} is a year")
else:
 print(f" {year} is not a leap year")