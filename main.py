"""
Anthony Quinn X00138635
16/11/2020
Week 6 Lab, nested ifs
"""

# Exercise 1


packageType = input("Please state your package type (letter or box): ").lower()

if packageType == "letter":
    letterWeight = float(input("Your parcels weight (in ounces): "))
    letterWeight = round(letterWeight)
    serviceType = input("Please input your delivery service (priority or standard): ").lower()
    if serviceType == "priority":
        fee = 12.00
    else:
        fee = 10.50
    print("The fee is €" + str(fee), "for a package with:")
    print("Type: ", packageType)
    print("Service: ", serviceType)
    print("Weight: ", int(letterWeight))
else:
    weight = float(input("Your parcels weight (in pounds): "))
    weight = round(weight)
    serviceType = input("Please input your delivery service (priority or standard): ").lower()
    if serviceType == "priority":
        if weight > 1:
            fee = 15.75 + (1.25 * weight) - 1.25
        else:
            fee = 15.75
    if serviceType == "standard":
        if weight > 1:
            fee = 13.75 + (1.00 * weight) - 1.00
        else:
            fee = 13.75
    print("The fee is €" + str(fee),"for a package with:")
    print("Type: ", packageType)
    print("Service: ", serviceType)
    print("Weight: ", int(weight))






