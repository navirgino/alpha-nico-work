#Name: Nicola A.R. Virgino
#Date: 09/11/2018

#Program Description: This program calculates miles-per-gallon.

#Declare Variables
milesDriven = 0.0
gallonsGasUsed = 0.0
milesPerGallon = 0.0
#Get Inputs
milesDriven = float(input("Please enter the amount of miles driven: "))

gallonsGasUsed = float(input("Please enter how many gallons of gas was used: "))

#Begin Processing

milesPerGallon = milesDriven // gallonsGasUsed

#Display Outputs

print("The amount of miles per gallon is" , format (milesPerGallon, '.2f'), end = ".")
