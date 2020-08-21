usernameInput = input("Username : ")
passwordInput = input("Password : ")
max_attempts = 5
count = 1
while usernameInput != "admin" or passwordInput != "1234":
    print('Incorrect username or password, you have %d attempts left to try.' % (max_attempts - count))
    if count == 5:
        exit(0)
    count = count + 1
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
print("Done")
