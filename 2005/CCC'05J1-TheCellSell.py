daytime = int(input())
evening = int(input())
weekend = int(input())

paidMinutesA = 0
paidMinutesB = 0

def calculatePlanA():
    if daytime > 100:
        paidMinutesA = daytime - 100
    else:
        paidMinutesA = 0
    
    totalCost = (paidMinutesA * 0.25) + (evening * 0.15) + (weekend * 0.2)
    return totalCost
    

def calculatePlanB():
    if daytime > 250:
        paidMinutesB = daytime - 250
    else:
        paidMinutesB = 0
    
    totalCost = (paidMinutesB * 0.45) + (evening * 0.35) + (weekend * 0.25)
    
    return totalCost
    

planACost = round(calculatePlanA(), 2)
planBCost = round(calculatePlanB(), 2)

if str(planACost).count(".0") == 1:
    planACost = str(planACost) + "0"
    
    
if str(planBCost).count(".0") == 1:
    planBCost = str(planBCost) + "0"


print("Plan A costs", planACost)
print("Plan B costs", planBCost)

if planACost < planBCost:
    print("Plan A is cheapest.")
elif planACost > planBCost:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")
