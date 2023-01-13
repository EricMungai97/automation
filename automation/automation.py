import re


def get_data(filepath):
    with open(filepath, "r") as file:
        potential_contacts = file.read()
        return potential_contacts


# telephone number search with regex
def get_phone_numbers(data):
    phone_numbers = []
    phone_numbers.extend(
        re.findall('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}',
                   data))

    # To Prevent duplicates since sets cannot have duplicate values
    duplicates = list(set(phone_numbers))
    duplicates.sort()
    print(len(duplicates))
    return duplicates


# email addresses search with regex
def get_email_addresses(data):
    email_address = []
    email_address.extend(re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", data))

    email_remove_duplicates = list(set(email_address))
    email_remove_duplicates.sort()
    print(len(email_remove_duplicates))
    return email_remove_duplicates


def write_to_file(data, path):
    result = ""
    for item in data:
        result += item + "\n"
    with open(path, "w") as new_file:
        new_file.write(result)


def main():
    data = get_data("assets/potential-contacts.txt")
    phone_numbers = get_phone_numbers(data)
    emails = get_email_addresses(data)
    write_to_file(emails, "assets/emails.txt")
    write_to_file(phone_numbers, "assets/phone_numbers.txt")


if __name__ == "__main__":
    main()
