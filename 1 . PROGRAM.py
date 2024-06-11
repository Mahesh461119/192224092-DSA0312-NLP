import re
def main():
    text = input("Enter text: ")
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_addresses = re.findall(email_pattern, text)
    print("\nEmail Addresses:")
    for email in email_addresses:
        print(email)
    first_email_match = re.search(email_pattern, text)
    if first_email_match:
        print("\nFirst Email Address Found:")
        print(first_email_match.group())
    else:
        print("\nNo email address found in the text.")
if __name__ == "__main__":
    main()
