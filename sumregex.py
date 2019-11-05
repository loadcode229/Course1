#import regular expressions
import re
#reads file specified
hand = open('regex_sum_286218.txt')
#sum declared as 0
sum = 0
#for each line, strip whitespace
#find all numbers in the file, and print the sum
for line in hand:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)
print(sum)

#**SIMPLIFIED VERSION TO ONE LINE**
import re
print(sum(int[re.findall('[0-9]+', line   .read('regex_sum_286218.txt')) ] ) )
