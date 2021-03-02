# Replace magic numbers with named constanst

# Given two point charges, calcualte the electric force exerted on them.
def get_electric_force(q1, q2):
  COULUMB_CONST = 8.9875517923*1e9
  distance = int(input("Enter the distance between two charges: "))
  force = COULUMB_CONST * q1 * q2/(distance**2)
  print ("Electric Force between q1 and q2 is: ", force, "Newton")


def odd_even(num):
  if num % 2 == 0:
      print(num, "is an even number.")
  else:
      print(num, "is an odd number.")

if __name__ == "__main__":
  q1 = int(input('Enter a value of charge q1: '))
  q2 = int(input('Enter a value of charge q2: '))
  get_electric_force(q1, q2)

  num = int(input('Enter an integer number: '))
  odd_even(num)