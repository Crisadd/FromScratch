"""
Objective
In this challenge, you will work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent
(the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest
integer.

Example
mealCost = 100
TipPercent = 15
taxPercent = 8

A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value 123 and return from the function.
"""
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent

meal_cost = float(input('Meal Cost: ').strip())
tip_percent = int(input('Tip Percent: ').strip())
tax_percent = int(input('Tax Percent: ').strip())


def solve(meal_cost, tip_percent, tax_percent):
   tip = (meal_cost*tip_percent)/100
   tax = (meal_cost*tax_percent)/100
   print(round(meal_cost + tip + tax))

solve(meal_cost, tip_percent,tax_percent)