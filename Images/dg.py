#Is prime
"""def isprime(n=8):
    if n <= 1:
       print("is not a prime number")
       return


    count = 0
    for i in range(1 , n+1):
        if n%i == 0:
         count = count + 1

    if count == 2:
        print("isprime")
    else:
        print("not")
    
isprime()
"""

#Sum of Digits of N
"""
def sum(N):
    sum = 0
    while N> 0:
        digits = N % 10
        sum = sum + digits
        N = N // 10
    print(sum)
sum(6764653)

"""

#Reverse N number   
# you can also do like first convert it to strong and reverse it and again back to int
#  reverse() is only used for list
"""
def reverse(N):             
    rev = str(N)
    reverse = rev[::-1]
    reverse = int(reverse)
    print(reverse)
reverse(123345)


"""



"""def reverse(N):
    rev =0
    while N>0:
        compliment = N % 10
        rev = rev*10 + compliment
        N = N//10
    print(rev)
reverse(2345)"""

#Count a digits of N
"""
def count_digits(n):
    count = 0
    if n == 0:
        print("1")
        return
    N = abs(n)
    while N>0:
        N = N // 10
        count=count + 1
    return count
print(count_digits(56776567896))
"""


#Check Armstrong number
"""
def Armstrong(N):
    # 1. Store the original number's digit count, as we need it for the exponent (k)
    k = len(str(N))
    
    # 2. Store the original number in a temporary variable (temp_N is a good practice, 
    # but we will use the user's variable name N for the loop)
    # We MUST save the original value of N for the final comparison.
    original_N = N 
    
    sum_of_powers = 0
    
    # We will use the original user's variable name 'sum_num' to hold the 
    # value we are processing (the digits are extracted from this value).
    sum_num = N
    
    # 3. Loop as long as the number we are processing (sum_num) is greater than 0
    while sum_num > 0:
        # 'digit' is correct: extracts the last digit from the number being processed (sum_num)
        digit = sum_num % 10
        
        # 'sum_of_powers' is correct: adds the powered digit. 
        # The exponent is the correct variable 'k' (the digit count).
        sum_of_powers += digit ** k
        
        # We must update sum_num, not k, to remove the last digit.
        sum_num //= 10
        
    # 4. Check the final result AFTER the loop finishes, comparing the calculated 
    # sum against the stored original number.
    if original_N == sum_of_powers:
        return True
    else:
        return False
        
print(Armstrong(371))
"""
"""
def print_multiplication_table(N):
    # Standard multiplication tables go from 1 to 10 (inclusive)
    # The range function needs '11' as the stop value to include 10.
    print(f"--- Multiplication Table for {N} ---")
    
    for i in range(1, 11):
        # Calculate the product
        product = N * i
        
        # Print the result in a formatted way: N x i = product
        print(f"{N} x {i:2} = {product:3}") 
        
# Example: Print the table for N = 7
print_multiplication_table(7)

"""
"""
A = 10
B = 5
temp = 0

# 1. temp gets the value of A
temp = A 
# temp is now 10

# 2. A gets the value of B
A = B
# A is now 5

# 3. B gets the original value of A from temp
B = temp
# B is now 10

print(f"After swap: A = {A}, B = {B}") 
# Output: After swap: A = 5, B = 10
"""

"""

#Level 2    Arrays / Lists / Strings

def reverse(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    print("Reversed array:", arr)
reverse([1, 2, 3, 7, 5])


"""
"""
#TWO SUM
# START

# Step 1: Input array and target
arr = [2, 7, 11, 15, 1, 8]
target = 9

# Step 2: Create empty dictionary to store numbers and their indices
seen = {}

# Step 3: Loop through array
for i, num in enumerate(arr):
    complement = target - num          # Number needed to reach target
    if complement in seen:
        # Step 4: Output the pair and their indices
        print("Two-sum pair found:", complement, num)
        print("Indices:", seen[complement], i)
        # Continue looping if you want all pairs
    seen[num] = i                       # Store current number with its index

# STOP
"""
"""
def TwoSum(arr,target):
    seen ={}
    
    for i, num in enumerate(arr):
        compliment = target - num
        if compliment in seen:
            print("values are",compliment,num)
            print("Indices are ",[seen[compliment],i])
        seen[num]=i
TwoSum([1,2,3,4,5,6,7,8,9,0,11,22,33,44,55,66,77,88,99],10)

"""

