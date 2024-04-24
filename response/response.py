import validators

validators.email('someone@example.com')
True

def main():
    email = "example@email.com"  # Replace with your actual email address
    print(validate(email))

def validate(s):
    if validators.email(s):
        return f"{s} is a valid email address."
    else:
        return f"{s} is an invalid email address."

if __name__ == "__main__":
    main()

