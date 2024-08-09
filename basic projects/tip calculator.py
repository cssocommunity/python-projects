''' here we will 
tips = integer and bill = float 

'''

print("welcome to tip calculator.?")
bill = float(input("what is your total bill? "))
tip = int(input("how much percent do you want to give money as a tip?  "))
spilt_with_friends = int(input(" spilt your bill how many people?  "))
tip_calculate = (tip / 100 * bill + bill)

print(tip_calculate / spilt_with_friends)