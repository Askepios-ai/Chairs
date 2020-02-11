f = open("reservations")

for reservation in f:
    name, number = reservation.split(",")
    try:
        chairs_per_person = 50 / int(number)
    except ValueError:
        print('Could not calculate chars pr. person', name, number)
        print('Please read over name and number and correct if wrong')
        name = input('please type name again\n')
        number = input('please type number again\n')
        chairs_per_person = 50/int(number)
    except TypeError:
        print("Wrong type of arguements, you sure it is actually a real name and a number as integer?")
    except ZeroDivisionError:
        print(name," had 0 chairs, purged from list")
        

    print("{} will get {} chairs per person".format(name, chairs_per_person))
