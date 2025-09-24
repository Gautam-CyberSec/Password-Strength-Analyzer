import string

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    if not any(c.isupper() for c in password):
        return "Weak: Add at least one uppercase letter."
    if not any(c.islower() for c in password):
        return "Weak: Add at least one lowercase letter."
    if not any(c.isdigit() for c in password):
        return "Weak: Add at least one number."
    if not any(c in string.punctuation for c in password):
        return "Weak: Add at least one special character."
    
    return "Strong Password ✅"

# Sample test
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    result = check_password_strength(password)
    print(result)