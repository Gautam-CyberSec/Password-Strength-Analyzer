# Task 10: Password Strength Analyzer

### OBJECTIVE  
Build a Python tool that checks the strength of a password using defined rules for security best practices.

### PASSWORD STRENGTH RULES  
A password is considered **strong** if it meets the following criteria:

1.  At least 8 characters long  
2.  Contains at least one uppercase letter (A-Z)  
3.  Contains at least one lowercase letter (a-z)  
4.  Contains at least one digit (0-9)  
5.  Contains at least one special character (e.g., !@#$%^&*)

### LOGIC USED IN CODE

Python functions and checks implemented:

- `len(password)` → Check minimum length  
- `any(c.isupper() for c in password)` → Check for uppercase letters  
- `any(c.islower() for c in password)` → Check for lowercase letters  
- `any(c.isdigit() for c in password)` → Check for numbers  
- `any(c in string.punctuation for c in password)` → Check for special characters  

### SAMPLE INPUT/OUTPUT

##### Input: `Broskieshub99`  
**Output:** Weak: Add at least one special character.

##### Input: `BroskiesHub99()`  
**Output:** Strong Password

### CONCLUSION  
This tool demonstrates how to enforce password security standards programmatically. Users can test the strength of their passwords and receive real-time feedback on how to improve them. This is an essential skill in building secure authentication systems and promoting good password hygiene.
