# Greatest Common Divisor (GCD) Calculator

A simple Python program to calculate the **Greatest Common Divisor (GCD)**—also known as the Highest Common Factor (HCF)—of two user-provided integers.

## 🚀 How It Works

The project includes the original implementation alongside optimized versions that improve processing speed for larger numbers.

### 1. Brute-Force Approach (Original)
This approach finds the GCD by checking every single integer from `1` up to the smaller of the two numbers. 

* **Time Complexity:** \(O(\min(m, n))\) — Linear time.
* **Pros:** Intuitive and easy to understand.
* **Cons:** Slows down significantly for very large numbers (e.g., 9-digit numbers or higher) because it iterates through every number and allocates memory for a list of factors.

```python
def gcd(m, n):
    common_factor = []
    for i in range(1, min(m, n) + 1):
        if (m % i) == 0 and (n % i) == 0:
            common_factor.append(i)
    return common_factor[-1]
```

### 2. Optimized Approach (Euclidean Algorithm)
This version uses the **Euclidean Algorithm**, which repeatedly divides the larger number by the smaller number and takes the remainder until the remainder becomes zero.

* **Time Complexity:** \(O(\log(\min(m, n)))\) — Logarithmic time.
* **Pros:** Extremely fast; handles huge numbers instantly without high memory usage.

```python
def gcd(m, n):
    while n:
        m, n = n, m % n
    return m
```

### 3. Standard Library Approach (Recommended for Production)
Python provides a built-in, highly optimized `gcd` function inside the native `math` module.

```python
import math
result = math.gcd(n1, n2)
```

---

## 💻 How to Run

1. Make sure you have **Python 3.x** installed.
2. Save the code into a file, for example, `gcd_calc.py`.
3. Open your terminal or command prompt and run:
   ```bash
   python gcd_calc.py
   ```
4. Enter two integers when prompted.

### Example Output
```text
Enter the first number : 60
Enter the second number : 48
12
```

---

## 🛠️ Requirements
* Python 3.6 or higher (No external dependencies required).
