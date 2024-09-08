command = ''
started = False
stopped = False
while command != "quit":
    command = input("> ").lower()
    if command == 'start' and started == False:
        print("Car started")
        started = True
    elif command == 'start' and started == True:
        print("Already started")
    elif command == 'stop' and stopped == False:
        print("Car Stopped")
        stopped = True
    elif command == 'stop' and stopped == True:
        print("Already stop")
    elif command == 'quit':
        break
    elif command == 'help':
        print('''
start - to start the game
stop - to stop the car
quit - to exit the game
''')
    else:
        print("i dont understand")