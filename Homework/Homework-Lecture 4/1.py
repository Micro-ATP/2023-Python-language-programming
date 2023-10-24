wants = {"13.3英寸M1芯片 8+7核 16GB + 512GB, 官方标配": 9999, "BOSE QuietComfort 45": 3500, "ATP SUPER PLUS KEYBOARD": 2000}

totalCost = sum(wants.values())

availableFunds = int(input("Please enter your available funds: "))

if availableFunds >= totalCost:
    print("买买买，直接下单!")
    print(f"{wants}马上就到家咯")
else:
    print("买不起一点，还不如睡觉!")
