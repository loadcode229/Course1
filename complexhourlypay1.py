# Prompt to enter hours.
hrs = input("Enter Hours: ")
rate = input("Enter Rate per Hour: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

print(h, r)

# Work out overtime pay.
if h > 40:
    overtimeRate = 0.5 * r
    overtime = (h-40) * overtimeRate
else:
    overtime = 0
# All finished up
grosspay = h * r
print("Pay: ", grosspay + overtime)
