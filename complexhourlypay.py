# Prompt to enter hours.
hrs = input("Enter Hours: ")
h = float(hrs)

# Prompt to enter rate per hour.
rate = input("Enter Rate per Hour: ")
r = float(rate)

# Work out overtime pay.
if h > 40:
    overtimeRate = 0.5 * r
    overtime = (h-40) * overtimeRate
else:
    overtime = 0
# All finished up
grosspay = h * r
print("Pay: ", grosspay + overtime)
