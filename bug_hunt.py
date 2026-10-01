count = 1
total = 0

# BUG: the while statement was missing a colon at the end — Python requires ':' to start a loop block
# BUG: the condition used 'count < 5', which stops the loop before count reaches 5, so 5 was never added to total — changed it to 'count <= 5' so the loop includes count equal to 5
while count <= 5:
    total = total + count
    count = count + 1

# BUG: tried to join a string and an integer directly with '+', which Python doesn't allow — wrapped total in str() to convert it to text first
print("Sum of 1 to 5 is: " + str(total))