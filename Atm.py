class A:
    def __init__(self):
        print('\nEnter 1 to Sign-In ("Already a user")\nEnter 2 to Sign-Up\nEnter 0 to exit:')
        a=int(input())
        if a==1:
            obj=B()
            name = input('Enter the user name:')
            obj.operation(name)
        elif a==2:
            name = input('Enter the username')
            pw = input('Enter the pin')
            pw1 = input('Re-enter the pin')
            if pw == pw1:
                object=C()
                object.read(name,pw)
            else:
                print('Enter valid pin')
                self.__init__()
        elif a==0:
            exit()
        else:
            print('Enter valid input')
            self.__init__()
class C:
    def read(self,name,password,amo=0):
        with open('data_list.txt', 'a+') as file:
            tot=name+','+password+','+str(amo)+'\n'
            file.write(tot)
        print('Account created successfully')
        A().__init__()

class B:
    def read_data_from_file(self,file_name):
        with open(file_name, 'r') as file:
            data = file.readlines()
        nested_list = []
        for line in data:
            line = line.strip()  # Remove leading/trailing whitespaces
            elements = line.split(',')  # Assuming data is comma-separated
            nested_list.append(elements)
        return nested_list

    def read(self,current,pw,amount,details):
        with open('data_list.txt', 'a+') as file:
            tot=details[current][0]+','+pw+','+amount+'\n'
            file.write(tot)
    def default(self):
        print('Invalid input')

    def balance(self,current,details):
        print(details[current][2])
        return

    def withdraw(self,current,details):
        amount = int(input('Enter the withdraw amount'))
        if amount > int(details[current][2]):
            print('Insufficient balace')
        else:
            total = int(details[current][2]) - amount
            print('Your balance amount is ', total)
            return str(total)

    def deposit(self,current,details):
        amount = int(input('Enter the deposit amount'))
        total = int(details[current][2]) + amount
        print('Your balance is ', total)
        return str(total)

    def reset(self,current,details):
        new_pass = int(input('Enter the new pin'))
        re_pass = int(input('Re-enter the pin'))
        if new_pass == re_pass:
            print('Password updated')
            return str(new_pass)
        else:
            print('Type correct password')
            return
    def user_name(self,name,details):
        j = 0
        for i in range(len(details)):
            if name == details[i][0]:
                current = i
                j += 1
            else:
                pass
        if j == 0:
            print('Username not found')
            A().__init__()
        return current
    def password(self,current,details,k=2):
        password = input('Enter the pin:')
        for j in range(3, 0, -1):
            if password == details[current][1]:
                return password
            else:
                k -= 1
                print('Password incorrect, try again !')
                print('You have ', k+1, 'chances left.')
                password=input('Enter the pin:')
                # self.password(current,password,details)
                if k == 0:
                    print('Account is blocked')
                    A().__init__()

    def operation(self,name):
        file_name = "data_list.txt"
        details = self.read_data_from_file(file_name)
        # print(details)
        current=self.user_name(name,details)
        print(current,'p')
        password=self.password(current,details)
        if password:
            def switch_case():
                file_name = "data_list.txt"
                details = self.read_data_from_file(file_name)
                current=self.user_name(name,details)
                # print(current)
                print('\nEnter 1 for checking balance \nEnter 2 for Withdrawing amount \nEnter 3 for Depositing amount \nEnter 4 to reset password \nEnter 0 to complete the process')
                n = int(input('\nEnter a function name:'))
                if n == 0:
                    print('Thank you !!! Process completed')
                    A().__init__()
                elif n == 4:
                    #pin=input('Enter the pin:')
                    password = self.password(current, details)
                    npw = self.reset(current, details)
                    if npw:
                        self.read(current, npw, details[current][2], details)
                    A().__init__()
                elif n == 1:
                    #pin = input('Enter the pin:')
                    password = self.password(current, details)
                    self.balance(current, details)
                    switch_case()
                elif n == 2:
                    #pin = input('Enter the pin:')
                    password = self.password(current, details)
                    total = self.withdraw(current, details)
                    self.read(current, password, total, details)
                    switch_case()
                elif n == 3:
                    #pin = input('Enter the pin:')
                    password = self.password(current, details)
                    total = self.deposit(current, details)
                    self.read(current, password, total, details)
                    switch_case()
                else:
                    print('Enter valid function name')
                    switch_case()

        switch_case()

A()