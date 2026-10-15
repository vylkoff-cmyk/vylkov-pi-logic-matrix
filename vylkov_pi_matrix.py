"""
The Vylkov Pi Logic Matrix (VPLM) Implementation
Author: Andrey Vylkov (vylkoff@gmail.com)
Description: Demonstrates the extraction of Pi digits using 6 discrete logical states.
"""

import mpmath

# Set high precision for verification (up to 100 digits)
mpmath.mp.dps = 100

def get_vylkov_state_precision(state_number):
    """Maps the 6 logical states to their respective mathematical boundaries."""
    states = {
        1: {"pair": (9, 7), "n_terms": 1},   # 14 digits accuracy
        2: {"pair": (8, 6), "n_terms": 2},   # 28 digits accuracy
        3: {"pair": (7, 5), "n_terms": 3},   # 42 digits accuracy
        4: {"pair": (6, 4), "n_terms": 4},   # 56 digits accuracy
        5: {"pair": (5, 3), "n_terms": 5},   # 70 digits accuracy
        6: {"pair": (4, 2), "n_terms": 6}    # 84 digits accuracy
    }
    return states.get(state_number)

def calculate_vylkov_pi(state_num):
    """Calculates Pi bound by the chosen Vylkov logical state."""
    state_data = get_vylkov_state_precision(state_num)
    if not state_data:
        return None
    
    # Core Ramanujan-Chudnovsky kernel controlled by the finite loop structure
    limit = state_data["n_terms"]
    sigma_sum = mpmath.mpf(0)
    
    for n in range(limit):
        numerator = mpmath.fac(6*n) * (545140134*n + 13591409)
        denominator = mpmath.fac(3*n) * (mpmath.fac(n)**3) * (640320**(3*n))
        term = mpmath.mpf(numerator) / mpmath.mpf(denominator)
        if n % 2 == 1:
            sigma_sum -= term
        else:
            sigma_sum += term
            
    c = 426880 * mpmath.sqrt(10005)
    pi_approximation = c / sigma_sum
    return pi_approximation

if __name__ == "__main__":
    print("=== The Vylkov Pi Logic Matrix Demonstration ===\n")
    
    for state in range(1, 7):
        state_info = get_vylkov_state_precision(state)
        p1, p2 = state_info["pair"]
        
        calculated_pi = calculate_vylkov_pi(state)
        # Format output to show where the 14-digit blocks stabilize
        pi_str = str(calculated_pi)[:86] 
        
        print(f"State {state} (Pair: {p1}-{p2}, Delta: {p1-p2})")
        print(f"Result: {pi_str}...\n")

