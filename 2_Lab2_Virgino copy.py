#Name: Nicola A.R. Virgino
#Date: 09/23/2018

#Description: An if-else statement that determines whether the points variable
#is outside the range 5 to 41. If the varible's value is outside this range it
#should display "Invalid points". Otherwise, it will display "Valid Points".

#Declare Variables:
points = 0

#Get Inputs:


points = int(input("Please enter a point of x: "))

#Begin Processing:



if points < 5 or points > 41:
    print('Invalid Points.')
else:
    print('Valid Points.')
