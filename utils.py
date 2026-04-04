def validate_input(name, contact):
    if name.strip() == "" or contact.strip() == "":
        return False
    if not contact.isdigit() or len(contact) != 10:
        return False
    return True

def blood_groups():
    return ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]