import re

def password_strength(password):
    # Initialize the score
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Provide feedback and categorize strength
    if score == 5:
        return "Strong password", feedback
    elif 3 <= score < 5:
        return "Moderate password", feedback
    else:
        return "Weak password", feedback

# Example usage
password = input("Enter your password: ")
strength, suggestions = password_strength(password)

print(f"Password Strength: {strength}")
if suggestions:
    print("Suggestions to improve password strength:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
