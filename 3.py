import re

def check_password_strength(password):
    
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[@$!%*?&]', password))
    
        strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    
    if strength_score == 5:
        strength_level = "Very Strong"
    elif strength_score == 4:
        strength_level = "Strong"
    elif strength_score == 3:
        strength_level = "Moderate"
    elif strength_score == 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"
    
       feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Include at least one numeric digit.")
    if not special_char_criteria:
        feedback.append("Include at least one special character (e.g., @, $, !, %, *, ?, &).")
    
    return strength_level, feedback


password = input("Enter your password: ")
strength, suggestions = check_password_strength(password)
print(f"Password Strength: {strength}")
if suggestions:
    print("Suggestions to improve your password:")
    for suggestion in suggestions:
        print(f"- {suggestion}")