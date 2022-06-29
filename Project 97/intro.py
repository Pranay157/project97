guess=int(input("Enter the numbers "))
number= guess<9
chances=0<5
while chances < 5:
 if guess== number:
    print("Congratulation YOU WON !!!")
    break
if not chances < 5:
    print("Oh YOU LOSE !! The Number is " ,number)
