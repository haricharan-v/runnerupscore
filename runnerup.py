n = int(input("Enter the number of scores you want to enter: "))
arr = map(int, input("Enter a list of scores with each score separated by space: ").split())

# Convert the map object to a list and remove duplicates by converting to a set
unique_scores = list(set(arr))

# Sort the unique scores in descending order
sorted_scores = sorted(unique_scores, reverse=True)

# The runner-up score is the second element in the sorted list
runner_up_score = sorted_scores[1]

print(f"The runner up score is {runner_up_score}")