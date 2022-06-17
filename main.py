print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100!")
print("\n")
print("(Please remember to type an integer value.)")
print("\n")

number = 37
yourNumber = 0

while number != yourNumber:
  
  yourNumber = int(input("What number do you guess? "))
  if number > yourNumber and yourNumber >= 1:
    print(" Guess is too low.")
  elif number < yourNumber and yourNumber <= 100:
    print(" Guess is too high.")
  elif number == yourNumber:
    print(" You guessed the right number!")
  elif yourNumber < 1 or yourNumber > 100:
    print(" Please remember to guess a number between 1 and 100.")

print("\n Thank you for playing!")