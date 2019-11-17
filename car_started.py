option = " "
current_state = " "
while True:
    option = input("> ").upper()
    
    if option == "START":
        print("Car started")

    elif option == "STOP":
        print("Car Stopped")

    elif option == "HELP":
        print("""
        start - start the car
        stop - stop the car
        quit - quit
        """)
    elif option == "QUIT":
        break

    else:
        print("Sorry don't understand")
