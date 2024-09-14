# PRODIGY_CS_03
In this task, the objective is to build a tool that assesses the strength of a password based on various criteria like length, use of uppercase and lowercase letters, digits, and special characters. The code provides feedback on whether the password is weak, moderate, or strong, and gives suggestions on how to improve it.

Regular Expressions (re):

The re library is used for regular expressions, which help in pattern matching for characters in the password (like lowercase letters, uppercase letters, digits, and special characters).
Password Strength Function (password_strength):

This function assesses the password's complexity by checking the following:
Length: The password must be at least 8 characters long.
Lowercase Letters: The password should contain at least one lowercase letter.
Uppercase Letters: The password should contain at least one uppercase letter.
Digits: The password should contain at least one number.
Special Characters: The password should contain at least one special character like !@#$%^&*.
For each condition that is met, the score increases by 1. Based on the final score, the password is categorized as Strong, Moderate, or Weak.

Feedback Mechanism:

If a password doesn’t meet a particular condition (e.g., no special character), a feedback message is added to a list, suggesting how the password can be improved.
Password Strength Categories:

Strong: A password is classified as strong if it meets all 5 conditions.
Moderate: If the password satisfies 3 or 4 conditions.
Weak: If the password satisfies fewer than 3 conditions.
