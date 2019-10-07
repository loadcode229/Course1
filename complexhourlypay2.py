# Defining function to combine pay.
def computepay(h ,r):
    grosspay = h * r
    return grosspay

# Get hours and rate per hour.
hrs = input("Enter Hours: ")
rate = input("Enter rate per hour: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Enter numeric value please.")
    quit()

# Work out pay and overtime if necessary.
if h > 40:
    overtimeRate = 0.5 * r
    overtime = (h-40) * overtimeRate
else:
    overtime = 0

#All done
p = computepay(h, r)
print("Pay", p + overtime)
