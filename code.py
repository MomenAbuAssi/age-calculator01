
print("#" * 70)
print(" Wellcom Sir, We are happy to serve you ".center(70, '#'))
print("#" * 70)

ctyone = [ 'USA', 'Britain', 'Germany', 'France', 'Spain', 'gaza' ]
ctytow = ['Gaza', 'Palestine', 'Saudi Arabia', 'Egypt', 'Algeria', 'Yemen']
names = ['momen', 'ahmed', 'mohamed', 'mahmoud', 'ismael']
passwords =[]
passglobal = 'asd'

state = True
while state:
    name = input("Whats Your Name Sir :").strip()
    if name in names:
        print(f"Welcome Mester {name}")
        password = input("Enter the password: ").strip().lower()
        if password == passglobal or password in passwords:
            print(f"Profile | Name : {name} $ pass : {password}")
            edit = input("Do You Wont Edit Name Profile or skip.. (Y,N)/(S)").strip().lower()

            if edit == 's':
                country = input("whats your country Sir? : ").strip()

                if country in ctyone:
                    print("I only calculate the ages of citizens of Arab countries.")

                elif country in ctytow:
                    age = int(input("whats Your Age Sir :").strip())
                    unit = input("How do you want to calculate your age (years, months, weeks, days) : ").strip().lower()
                    years = age ; months = age * 12 ; weeks = months * 4 ; days = age * 365
                    if unit == 'years' or unit == 'y': print(f"Sir, your age of {years}")
                    if unit == 'months' or unit == 'm': print(f"Sir, months of your life is {months}")
                    if unit == 'weeks' or unit == 'w': print(f"Sir, weeks of your life is {weeks}")
                    if unit == 'days' or unit == 'd': print(f"Sir, days of your life is {days}")

                    logout = input("Thanks Sir, do You Wont Logout? (Y,N)").strip().lower()
                    if logout == 'y' or logout == 'yes':
                        state = False
                    elif logout == 'n' or logout == 'no':
                        continue

                else:
                    print("I can not answer")

            elif edit == 'y':
                update = input("Do you want to update or delete your name? (U,D)").strip().lower()
                if update == 'update' or update == 'u':
                    newname = input("Enter New Name : ")
                    names[names.index(name)] = newname
                    print(names)

                elif update == 'delete' or update == 'd':
                    names.remove(name)
                    print(names)
        else:
            print("***Username Or Password Error***")
            continue
    else:
        statelog = input("It seems that you are not listed in the list of users\ndo you want to be listed with the same name? (Y, N or L)")
        if statelog == 'y':
            newpass = input("Set a new password : ").strip()
            print("Please , Enter The password")
            passwords.append(newpass)
            names.append(name)
            print(f"Profile | Name : {name} $ pass : {newpass}")
        elif statelog == 'n':
            newuser = input("Enter New User : ")
            names.append(newuser)
            newpass = input("Set a new password : ").strip()
            passwords.append(newpass)
            print(f"Profile | Name : {newuser} $ pass : {newpass}")
        elif statelog == 'l':
            continue
