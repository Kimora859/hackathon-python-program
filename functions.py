def generate_fibonacci(n):
    sequence = [0, 1]  # Initialize the sequence with the first two terms

    # Generate the Fibonacci sequence up to the specified term
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]  # Calculate the next term
        sequence.append(next_term)  # Add the next term to the sequence

    return sequence

# Get the value of n from the user
n = int(input("Enter the number of terms for Fibonacci sequence: "))

# Generate and print the Fibonacci sequence up to the specified term
fib_sequence = generate_fibonacci(n)
print("Fibonacci sequence up to term", n, ":", fib_sequence)
