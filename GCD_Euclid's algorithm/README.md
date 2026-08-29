# GCD Calculator (Euclidean Algorithm Variations)

This repository contains two Python implementations for finding the **Greatest Common Divisor (GCD)** of two integers using variations of the Euclidean subtraction method. 

The implementations include an **iterative version** using a `while` loop and a **recursive version** that solves the problem by calling itself.

---

## ðŸ› ï¸ Implementations

### 1. Iterative Approach (`gcd_iterative.py`)
This version optimizes memory usage by using a loop to continuously calculate the difference between numbers until a remainder of zero is achieved.

### 2. Recursive Approach (`gcd_recursive.py`)
This version uses functional recursion to pass down the calculated values (`max` and `min` of the current subset) into a new execution context until the base condition (`m % n == 0`) is satisfied.

---

## ðŸš€ How to Run

1. Make sure you have **Python 3.x** installed on your system.
2. Run either script using your terminal:

```bash
python gcd_iterative.py
```
*or*
```bash
python gcd_recursive.py
```

3. Enter two integers when prompted.

### Example Interaction:
```text
Enter the first number: 48
Enter the second number: 18
GCD is :  6
```

---

## ðŸ“Š Algorithm Overview
Both scripts rely on the property that the GCD of two numbers also divides their difference. 
- **Step 1:** Ensure $m \ge n$ by swapping if necessary.
- **Step 2:** Check if $m$ is divisible by $n$. If yes, $n$ is the GCD.
- **Step 3:** If not, calculate `diff = m - n`.
- **Step 4:** Repeat the process using the pair `max(n, diff)` and `min(n, diff)`