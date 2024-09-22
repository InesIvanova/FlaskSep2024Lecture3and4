from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(
    uppercase=1,  # need min. 1 uppercase letters
    numbers=1,  # need min. 1 digits
    special=1,  # need min. 1 special characters
    nonletters=1,  # need min. 1 non-letter characters (digits, specials, anything)
)


def validate_password_strength(value):
    errors = policy.test(value)

    if errors:



validate_password_strength("asd1!A")