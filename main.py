import os

run = True

while run:

    ask = str(input("Do you want to `login` or `signup`: "))

    if ask.lower() in ["signup", "s", "s_u", "su", "sign up", "sign_up", "create", "c", "create account", "ca", "create_account", "c_a"]:

        #Creating and looking for the file to store data

        if os.path.exists("info.txt"):
            pass
        else:
            with open("info.txt", "w") as f:
                f.write("\n")
                


        #Signup info logger

        account_name = str(input("Please enter your account name: "))


        # Checking if account exists

        with open("info.txt", "r") as read_file:
            for data in read_file.readlines():
                account_recheck = data.split(":")

                has_not_fixed_account_name = True

                while has_not_fixed_account_name:
                    if account_recheck[0] == account_name:
                        account_name = str(input("That account has already been registered. Try using another name for an account: "))
                    else:
                        has_not_fixed_account_name = False


        # Getting and Confirming Password

        password = str(input("Please enter your secure password: "))
        password_confirm = str(input("Please re-type your password for confirmation: "))

        has_incorrect_password = False
        if password == password_confirm:
                print(f"Account for \"{account_name}\" created successfully! Password confirmed and saved! Please login")


        else:
                has_incorrect_password = True
                while has_incorrect_password:
                    re_password = str(input("Your password was not matched!\nPlease re-enter your password: "))
                    if re_password == password:
                        print(f'Account for "{account_name}" created successfully')
                        has_incorrect_password = False



        
        
        #Working with signup data

        with open("info.txt", "a") as info_file:
            info_file.write(f"{account_name}:{password}")
            info_file.write("\n")






    elif ask.lower() in ["login", "l", "log in", "l i", "l_i", "signin", "sin", "s_i", "sign in"]:
        #Checking account and password

        login_fix = False

        with open("info.txt", "r") as f:
            info = f.readlines()

            while login_fix == False:
                login_name = str(input("Account name: "))
                login_password = str(input("Password: "))

                for i in info:
                    if i == f"{login_name}:{login_password}\n":
                        print(f"Welcome back {login_name}.")
                        login_fix = True
                        break
                else:
                    print("No account exists with that information.")
                    

    elif ask.lower() in ["q", "quit", "exit", "e"]:
        run = False