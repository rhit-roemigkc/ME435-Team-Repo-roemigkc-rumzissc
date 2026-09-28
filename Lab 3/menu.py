import plateloader

def main():
    print("Serial Menu")
    loader = plateloader.PlateLoader() 
    loader.connect()
    print("0. Exit")
    print("1. RESET")
    print("2. X-AXIS")
    print("3. GRIPPER")
    print("4. Z-AXIS")
    print("5. MOVE")
    print("6. Status")
    while True:
        selection = int(input("Selection: "))
        if selection == 0:
            break
        elif selection == 1:
            response = loader.send_command("RESET")
            print(response)
        elif selection == 2:
            pos = input("X-AXIS Selection: ")
            combined = "X-AXIS " + pos
            print(combined)
            response = loader.send_command(combined)
            print(response)

    loader.disconnect()
    print("Goodbye")
    



main()