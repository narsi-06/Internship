import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email) is not None

emails = [
    "user@example.com", "test.email+alex@domain.co", "invalidemail.com", "user@.com", "user@domain"]

for e in emails:
    print(f"{e}: {is_valid_email(e)}")
