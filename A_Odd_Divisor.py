import sys

def solve():
    # Read the number of test cases
    t = int(sys.stdin.readline())
    for _ in range(t):
        # Read the input integer n
        n = int(sys.stdin.readline())
        
        # Keep dividing n by 2 until it becomes odd or 1
        while n % 2 == 0:
            n //= 2
            
        # If the resulting n is greater than 1, it means an odd divisor exists
        if n > 1:
            print("YES")
        else:
            # Otherwise, n was a power of two
            print("NO")

if __name__ == "__main__":
    solve()
