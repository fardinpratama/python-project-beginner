from feature import (
    get_data,
    create_contact,
    set_contact,
    search_contact,
    edit_contact,
    delete_contact,
    file_name,
)

# get data
data = get_data(file_name)
# main
print("******************************")
print("**      Contact Book        **")
print("******************************")
print("This is a Contact Book which has many features.")
print("please choose what you want to do :")
print("1. Create contact")
print("2. Search contact")
print("3. Update contact")
print("4. Delete contact")
print("-- press 'q' if you want to exit --")
choose = input("Select (1 - 4) : ")

if choose == "1":
    print("Create a new contact")
    print("=============================")
    data_contact = create_contact(data)
    data.append(data_contact)
    set_contact(data)
    print("saved contacts")
elif choose == "2":
    print("Search contact")
    search_contact(data)
elif choose == "3":
    print("Update contact")
    edit_contact(data)
elif choose == "4":
    print("Delete contact")
    delete_contact(data)
elif choose.lower() == 'q':
    pass
else:
    print("Please, choose according to the options!!!!")
