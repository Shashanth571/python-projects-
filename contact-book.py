print("Contact Book Starting...")

contact_info = {
    "shashanth": "6303903648",
    "daddy": "90003472234",
    "mommy": "90003472234",
    "sister": "90003472234",
}

name = input("Enter the name of the contact to search: ").lower()

if name in contact_info:
    print(f"{name}'s contact number is: {contact_info[name]}")
else:
    print(f"{name} is not in the contact book.")