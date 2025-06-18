import string

# Step 1: Get user input
password = input("Enter a password: ")

# Step 2: Set up checks
length_ok = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in string.punctuation for c in password)

# Collect feedback
feedback = []
if not length_ok:
    feedback.append("at least 8 characters")
if not has_upper:
    feedback.append("one uppercase letter")
if not has_lower:
    feedback.append("one lowercase letter")
if not has_digit:
    feedback.append("one digit")
if not has_special:
    feedback.append("one special character (e.g. @, #, $)")

# Step 3: Display results
if all([length_ok, has_upper, has_lower, has_digit, has_special]):
    print("Your password is strong!")
else:
    print("Your password needs:", ", ".join(feedback) + ".")

# Bonus: Strength meter (score out of 10)
score = 0
if length_ok:
    score += 2
if has_upper:
    score += 2
if has_lower:
    score += 2
if has_digit:
    score += 2
if has_special:
    score += 2

print(f"🔐 Password Strength Score: {score}/10")
