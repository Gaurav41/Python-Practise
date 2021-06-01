temp = float(input("Enter temperature: "))
convertTo = input("Enter Unit: ")

if convertTo.upper() == 'C' :
    converted = ( (temp - 32) * 5/9 )
    print(converted,"C")
else:
    converted =(temp * 9/5) + 32
    print(converted, "F")
