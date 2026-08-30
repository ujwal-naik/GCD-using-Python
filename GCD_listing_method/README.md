# Greatest Common Divisor (GCD) Calculator

A comprehensive Python project implementing and benchmarking various algorithms to find the Greatest Common Divisor (GCD) of two integers.

## ðŸ“‚ Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Algorithms Implemented](#-algorithms-implemented)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Complexity Comparison](#-complexity-comparison)
- [License](#-license)

## ðŸ“ Overview
The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both numbers without leaving a remainder. This project showcases the evolution of solving this problem from a basic brute-force implementation to the highly efficient, mathematically optimal Euclidean algorithm.

## âœ¨ Features
- **Interactive CLI:** Accepts dynamic user inputs for calculations.
- **Multiple Solvers:** Contains naive, optimized linear, and logarithmic implementations.
- **Resource Efficient:** Includes memory-optimized options using zero array allocations.

## ðŸ§® Algorithms Implemented

### 1. Naive Brute-Force
Generates complete factor lists for both inputs independently, intersects them, and selects the largest common value.
- **File Implementation:** `gcd_naive.py`

### 2. Optimized Backward Loop
Iterates backward from the smaller of the two inputs directly down to 1, returning immediately upon finding the first valid common divisor.
- **File Implementation:** `gcd_optimized.py`

### 3. Euclidean Algorithm
Repeatedly replaces the larger integer with the remainder of the two numbers until the remainder reaches zero.
- **File Implementation:** `gcd_euclidean.py`

## âš™ï¸ Getting Started

### Prerequisites
- Python 3.6 or higher installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gcd-calculator.git
   ```
2. Navigate into the project directory:
   ```bash
   cd gcd-calculator
   ```

## ðŸš€ Usage
Execute the script using your terminal:
```bash
python gcd_calculator.py
```

**Example Execution:**
```text
Enter the first number: 48
Enter the second number: 18
GCD is : 6
```

## ðŸ“Š Complexity Comparison

| Algorithm | Time Complexity | Space Complexity | Best For |
| :--- | :--- | :--- | :--- |
| **Naive Brute-Force** | $O(m + n)$ | $O(m + n)$ | Academic demonstrations |
| **Optimized Loop** | $O(\min(m, n))$ | $O(1)$ | Smaller integer sets |
| **Euclidean Algorithm** | $O(\log(\min(m, n)))$ | $O(1)$ | Production & massive integers |

## ðŸ“„ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.