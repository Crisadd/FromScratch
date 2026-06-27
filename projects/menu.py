import flight_distance_calculator

# answer = [1,2,3,4,5,6,7,8,9,10]
while True:
    print('========= MENU =========')
    print('1 - Flight Distance Calculator')
    print('2 - Small Airport Database')

    print('0 - Exit')

    answer = int(input('Select a number: '))


    if answer == 1:
        flight_distance_calculator.main()

    elif answer == 0:
        print("Goodbye!")
        break
    else:
        print("Goodbye!")
        break