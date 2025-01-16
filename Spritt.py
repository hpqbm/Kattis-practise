# Read the first line of input
num_classrooms, total_bottles = map(int, input().split())

# Initialize a variable to track the total bottles required
required_bottles = 0

# Loop through the number of classrooms to get their requirements
for _ in range(num_classrooms):
    required_bottles += int(input())

# Check if the total available bottles are enough
if required_bottles <= total_bottles:
    print("Jebb")
else:
    print("Neibb")