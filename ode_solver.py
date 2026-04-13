import sympy as sp

def solve_assignment_ode():
    # 1. Setup symbolic variables
    x = sp.Symbol('x')
    y = sp.Function('y')(x)
    
    print("--- Second Order ODE Solver ---")
    print("Equation format: ay'' + by' + cy = f(x)")
    
    try:
        # 2. Input Coefficients
        a = float(input("Enter coefficient a (for y''): "))
        b = float(input("Enter coefficient b (for y'): "))
        c = float(input("Enter coefficient c (for y): "))
        
        # 3. Input the Forcing Function f(x)
        rhs_input = input("Enter f(x) (e.g., 0, sp.exp(x), or sp.sin(x)): ")
        f_x = eval(rhs_input)
        
        # Define the Differential Equation
        ode = sp.Eq(a*y.diff(x, x) + b*y.diff(x) + c*y, f_x)
        
        # 4. Input Auxiliary Conditions (Initial Values)
        # The prompt specifically asked for these
        print("\n--- Auxiliary Conditions ---")
        x0 = float(input("Enter initial x value (usually 0): "))
        y0 = float(input(f"Enter y({x0}): "))
        y_prime0 = float(input(f"Enter y'({x0}): "))
        
        # Define initial conditions dictionary
        ics = {y.subs(x, x0): y0, y.diff(x).subs(x, x0): y_prime0}
        
        # 5. Solve the Equation
        # We solve for the general solution first to extract parts
        # Then solve with ICS for the particular result
        
        # Homogeneous part (Complementary Function)
        homo_ode = sp.Eq(a*y.diff(x, x) + b*y.diff(x) + c*y, 0)
        yh = sp.dsolve(homo_ode, y).rhs
        
        # Full General Solution (without ICS)
        general_sol = sp.dsolve(ode, y).rhs
        yp = general_sol - yh
        
        # Specific Solution (with ICS applied)
        specific_sol = sp.dsolve(ode, y, ics=ics).rhs
        
        # 6. Final Output
        print("\n" + "="*30)
        print("FINAL RESULTS")
        print("="*30)
        print(f"Homogeneous Solution (yh): {yh}")
        print(f"Particular Solution (yp):   {yp}")
        print(f"General Solution (y):      {general_sol}")
        print("-" * 30)
        print(f"Solution with Auxiliary Conditions: y(x) = {specific_sol}")
        print("="*30)

    except Exception as e:
        print(f"\nError: {e}")
        print("Ensure you use 'sp.' for math functions (e.g., sp.exp(x)).")

if __name__ == "__main__":
    solve_assignment_ode()