scores = [72, 45, 90, 61, 38]

# Counters and accumulator, starting at zero before the loop runs
pass_count = 0
fail_count = 0
total = 0

# Loop through every score in the list
for score in scores:

    # Work out the grade using if/elif/else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    # Print each score with its grade, on its own line
    print(f"Score: {score} -> Grade: {grade}")

    # Count passes and fails (pass = 50 or more)
    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1

    # Keep a running total for the average later
    total += score

# Calculate the average after the loop finishes
average = total / len(scores)

# Print the final results
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")
print(f"Average: {round(average, 1)}")