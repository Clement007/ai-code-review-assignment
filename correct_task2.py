# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

def is_valid_email(email):
  
    if not isinstance(email, str):
        return False

    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    local, domain = email.split("@")
    if not local or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


def count_valid_emails(emails):
   
    count = 0

    for email in emails:
        if is_valid_email(email):
            count += 1

    return count

