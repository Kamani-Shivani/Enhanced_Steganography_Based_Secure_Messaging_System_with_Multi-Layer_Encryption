def validate_message_length(message, max_limit=400):
    length = len(message)

    if length > max_limit:
        print("Error: Message too long")
        return False
    return True


def validate_password_length(password):
    length = len(password)

    if length < 4:
        print("Error: Password must be at least 4 characters")
        return False
    return True

