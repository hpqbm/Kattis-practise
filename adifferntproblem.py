import sys

def main():
    input = sys.stdin.read()
    lines = input.strip().split('\n')
    
    for line in lines:
        if line:
            a, b = map(int, line.split())
            print(a - b)

if __name__ == "__main__":
    main()