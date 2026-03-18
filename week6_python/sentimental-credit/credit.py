from cs50 import get_string
import re

credit = get_string("Number: ")
copy_credit = credit[::1] #create a new array from index 0 to final by 1 lag so my credit won't change (if i let copy_credit = credit whe i change copy my crdit will be changed too)
multiple_code = copy_credit[-2::-2]
rest_code = copy_credit[-1::-2]

sum_1 = 0
sum_2 = 0
for digit in multiple_code:
    digits = int(digit)*2
    sum_1 += (digits//10) + (digits%10)

for digit in rest_code:
    sum_2 += int(digit)

total_sum = sum_1 + sum_2 #dont use sum
if total_sum % 10 == 0:
    if len(credit) == 15 and credit[0:2] in ['34', '37']: #credit is a string string == ""
        print("AMEX")
    elif len(credit) == 16 and 51 <= int(credit[0:2]) <= 55: # transport into int
        print("MASTERCARD")
    elif len(credit) in [13,16] and credit[0] == '4' :# len() is an int
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")
