import time

# ============================================
# 1. WITHOUT DP: Naive Recursive (Slow)
# ============================================
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# ============================================
# 2. WITH DP: Top-Down (Memoization)
# ============================================
def fib_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    return memo[n]

# ============================================
# 3. WITH DP: Bottom-Up (Tabulation)
# ============================================
def fib_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# ============================================
# TIMER FUNCTION
# ============================================
def time_function(func, n, name):
    start = time.time()
    result = func(n)
    end = time.time()
    print(f"{name:20} | Result: {result:10} | Time: {end - start:.6f} seconds")

# ============================================
# RUN THE COMPARISON
# ============================================
print("\n🔍 FIBONACCI PERFORMANCE COMPARISON (n = 55)\n")
print("Method                | Result     | Time")
print("-" * 55)

# Run with n=55 (large enough to see the difference)
N = 45

# 1. Recursive (may be slow for N > 40)
# time_function(fib_recursive, N, "1. Recursive")

# 2. Memoization
time_function(fib_memoization, N, "2. Memoization")

# 3. Tabulation
time_function(fib_tabulation, N, "3. Tabulation")