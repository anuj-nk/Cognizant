age = int(input("How old are you?: "))

if age >= 18:
    print("Go Vote! You are able to! AHHHH!")
elif age < 18:
    print("OH NO! Your are NOT able to vote. Don't fret though. Only " + str(18 - age) + " years left!")

# Similar idea as to the first assigned to put print statements with math and concatenations with correctly parsed data types