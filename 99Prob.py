def closest_ending_99(n):
    # Calculate the lower and higher candidate numbers ending in 99
    lower_candidate = (n // 100) * 100 + 99
    higher_candidate = ((n // 100) + 1) * 100 + 99
    
    # If n is already ending with 99, return it
    if n % 100 == 99:
        return n
    
    # Calculate the absolute differences
    lower_diff = abs(n - lower_candidate)
    higher_diff = abs(n - higher_candidate)
    
    # Determine the closest candidate
    if lower_diff <= higher_diff:
        return lower_candidate
    else:
        return higher_candidate

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    print(closest_ending_99(n))
