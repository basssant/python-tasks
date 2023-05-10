# creatinga lists of users, their PINs and bank statements
users = ('user1', 'user2', 'user3')
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0
flag = 0
# while loop checks existance of the enterd username
print("****************************************************************************")
print("*                                                                          *")
print("*                         Welcome to ATM MACHINE                           *")
print("*                                                                          *")
print("****************************************************************************")

user = input('\nENTER USER NAME: ')
for i in range(len(users)):
    if user == users[i]:
        flag = 1
        # comparing pin
        while count < 3:
            print('------------------')
            print('******************')
            pin = input('PLEASE ENTER PIN: ')
            print('******************')
            print('------------------')           
            if pin == pins[i]:
                break
            else:
                count += 1
                print('-----------')
                print('***********')
                print('INVALID PIN')
                print('***********')
                print('-----------')
                print()
        # in case of a valid pin- continuing, or exiting
        if count == 3:
            print('-----------------------------------')
            print('***********************************')
            print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
            print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
            print('***********************************')
            print('-----------------------------------')
            exit()
        else:
            print('-------------------------')
            print('*************************')
            print('LOGIN SUCCESFUL, CONTINUE')
            print('*************************')
            print('-------------------------')
if flag == 0:
    print('----------------')
    print('****************')
    print('INVALID USERNAME')
    print('****************')
    print('----------------')
    print()