correct_username = "python2023"
correct_password = "arafat"
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        print("Incorrect username or password. Please try again.")
        attempts += 1

if attempts == max_attempts:
    print("Access denied. You have reached the maximum number of login attempts.")
