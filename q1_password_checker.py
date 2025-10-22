import re 
# We import the 're' module, which stands for Regular Expressions. 
# This is a powerful, standard Python tool used to find and check complex text patterns (like "at least one uppercase letter").

# ------------------------- FUNCTION DEFINITION ----------------------------------

# 'def' is the essential Python keyword used to DEFINE a new function.
# 'check_password_strength' is the specific NAME we assign to this function.
# (password: str) is a TYPE HINT: 'password' is the INPUT (called an ARGUMENT) 
# and ': str' tells us it should be a string (text).
# -> bool is a TYPE HINT: it tells us the function will RETURN a 'bool' (boolean value: True or False).
def check_password_strength(password: str) -> bool:
    """
    Checks a password against defined strength criteria for security compliance.
    """
    
    # 'reasons' is a VARIABLE (a container for data). We initialize it as an empty list []. 
    # This list will store all the criteria the password fails.
    reasons = [] 

    # 1. Check for minimum length (at least 8 characters).
    # 'len()' is a DEFAULT PYTHON FUNCTION that returns the number of characters in the 'password' string.
    if len(password) < 8:
        # 'append()' is a built-in METHOD (a function attached to lists). It adds the failure message to our list.
        reasons.append("❌ Must be at least 8 characters long.")

    # 2. Contains uppercase letters.
    # 're.search()' looks for the pattern specified by r"[A-Z]" (any uppercase letter).
    # 'not' reverses the result: if search finds NOTHING, 'not' makes the condition True (meaning, it failed the check).
    if not re.search(r"[A-Z]", password):
        reasons.append("❌ Must contain at least one uppercase letter.")

    # 3. Contains lowercase letters.
    # r"[a-z]" is the pattern for any lowercase letter.
    if not re.search(r"[a-z]", password):
        reasons.append("❌ Must contain at least one lowercase letter.")

    # 4. Contains at least one digit (0-9).
    # r"\d" is the pattern shorthand for 'any digit'.
    if not re.search(r"\d", password):
        reasons.append("❌ Must contain at least one digit (0-9).")

    # 5. Contains at least one special character (!, @, #, $, %).
    # r"[!@#$%]" is the specific pattern requested in the assignment.
    if not re.search(r"[!@#$%]", password):
        reasons.append("❌ Must contain at least one special character (!, @, #, $, %).")

    # Final Check: If the 'reasons' list is empty (i.e., 'not reasons' is True), the password is strong.
    if not reasons:
        print("\n✅ Password is **STRONG**! It meets all security criteria.")
        return True # Return the boolean value True, signaling success.
    else:
        print("\n🚨 Password is **WEAK**. Failed criteria:")
        # Loop through the list of failures to print them
        for reason in reasons:
            print(f"  {reason}")
        return False # Return the boolean value False, signaling failure.

# ------------------------- SCRIPT EXECUTION ----------------------------------

# This is a standard Python entry point. Code inside here runs when the script is executed.
if __name__ == "__main__":
    print("--- DevOps Password Strength Checker ---")
    try:
        # 'input()' is a DEFAULT PYTHON FUNCTION that prompts the user for text input.
        user_password = input("Enter the password to check: ")
        
        # Simple check for empty input.
        if not user_password:
            print("Error: Password cannot be empty.")
        else:
            # Call our defined function 'check_password_strength'
            is_strong = check_password_strength(user_password)
            print(f"\nFinal Validation Result: {is_strong}")
            
    except Exception as e:
        # Graceful error handling for unexpected issues.
        print(f"An error occurred: {e}")
        
