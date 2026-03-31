def calculate_equilibrium(a, b, c, d):
    """
    Calculates the equilibrium price and quantity for a linear market model.
    D = a - bP
    S = c + dP
    Equilibrium: S = D => a - bP = c + dP => P = (a - c) / (b + d)
    """
    # 1. Calculate Equilibrium Price (P)
    try:
        price = (a - c) / (b + d)
        
        # 2. Calculate Equilibrium Quantity (Q) using either equation
        quantity = a - (b * price)
        
        return price, quantity
    except ZeroDivisionError:
        return None, None

def main():
    print("--- Market Equilibrium Simulator ---")
    
    # Example values (Attributes of the system)
    a = 100  # Max demand at price 0
    b = 2    # Demand drop rate
    c = 10   # Min supply price
    d = 1    # Supply increase rate
    
    p, q = calculate_equilibrium(a, b, c, d)
    
    if p:
        print(f"Equilibrium Price: ${p:.2f}")
        print(f"Equilibrium Quantity: {q:.2f} units")
    else:
        print("Error: Could not calculate equilibrium (Division by zero).")

if __name__ == "__main__":
    main()
