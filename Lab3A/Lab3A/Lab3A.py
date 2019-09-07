#cookToCode

#This program will ask the user how many * and calculate the calories and how long it will take to jog/run the calories off

#variable library
bigMac = 0
medFry = 0
smallShake = 0
calories = 0
jog = 0
run = 0

print('For every question, please only answer whole numbers. No one eats half of a Big Mac.......\n\n\n')
bigMac = int(input("How many Big Mac's did you eat? "))
medFry = int(input("\nHow many orders of medium fries did you eat? "))
smallShake = int(input("\nHow many small shakes did you drink? "))

#This will convert the food to calories
bigMac = bigMac*563
medFry = medFry*378
smallShake = smallShake*530
calories = bigMac+medFry+smallShake
#This portion converts calories to how many hours it will take to burn them
#rounded to the nearest tenths place
jog = round(calories/398, 1)
run = round(calories/557, 1)


print(f'\n\nIn total, you consumed {calories} calories.\n')
print(f'It will take {jog} hours to burn off {calories} calories while jogging.\n')
print(f'It will take {run} hours to burn off {calories} calories while running.\n')

