# creating strong password gui app, password creation inspired from geeksforgeeks.com

from tkinter import *
import random
import array
                                                



class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('340x160+500+300')
        self.root.title("Strong password generator")
        self.root.iconbitmap(None)
        self.root.configure(background='white')
        
        self.root.resizable(False, False)

        self.entryforpassword = Entry(self.root, text='', bg='white', fg='black', highlightbackground='white', justify='center')
        self.entryforpassword.place(x=75, y=110)

        self.yourpasslabel = Label(self.root, text='Your password', font=('Helvetica', 10), bg='white', fg='black')
        self.yourpasslabel.place(x=130,y=136)

        self.passlenlabel = Label(self.root, text='Password length', font=('Helvetica', 10), bg='white', fg='black')
        self.passlenlabel.place(x=130,y=40)

        self.passwordlength = Scale(self.root, from_=5, to=16, bg='white', fg='black', bd=1, troughcolor='white', orient=HORIZONTAL)
        self.passwordlength.place(x=120, y=0)

        self.createpassword = Button(self.root, text='Create password', highlightbackground='white', fg='black', command=self.create)
        self.createpassword.place(x=100,y=65)

        self.image = PhotoImage(file="copytoclipboard.png")

        self.copyentrytoclipboard = Button(self.root, image=self.image, bd=0, command=self.copytoclip, highlightbackground='white', fg='black')
        self.copyentrytoclipboard.image = self.image
        self.copyentrytoclipboard.place(x=270,y=114)

        self.password = ''



        self.root.mainloop()


    def copytoclip(self):
        #self.root.withdraw()

    
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password)



    def create(self):
        self.entryforpassword.delete(0,"end")

        ileznakow = int(self.passwordlength.get())
        self.password = self.creating_strong_password(ileznakow)
        self.entryforpassword.insert(0, self.password)


    def creating_strong_password(self, MAX_LEN):

        # maximum length of password needed

        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']

        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                            'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']

        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']

        # combines all the character arrays above to form one array
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

        # randomly select at least one character from each character set above
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)

        # combine the character randomly selected above
        # at this stage, the password contains only 4 characters but
        # we want a 12-character password
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


        # now that we are sure we have at least one character from each
        # set of characters, we fill the rest of
        # the password length by selecting randomly from the combined
        # list of character above.
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)

            # convert temporary password into array and shuffle to
            # prevent it from having a consistent pattern
            # where the beginning of the password is predictable
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)

        # traverse the temporary password array and append the chars
        # to form the password
        password = ""
        for x in temp_pass_list:
                password = password + x
                

        return password








App()