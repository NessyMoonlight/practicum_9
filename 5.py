def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_mileage():
  for mile in range(100000, 1000000):
    if is_palindrome(mile % 100000) and \
       is_palindrome((mile + 1) % 100000) and \
       is_palindrome(str((mile + 2) % 100000)[1:5]) and \
       is_palindrome(mile + 3):
      return mile
  return None

mileage = find_mileage()
if mileage:
  print("Пробег:", mileage)