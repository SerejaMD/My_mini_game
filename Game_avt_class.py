from tkinter import * 
from PIL import ImageTk as Image
import Lib_enter
import sqlite3




class General(Tk):
    def __init__(self, *arg, **kwargs):
        Tk.__init__(self, *arg, **kwargs)

        connect = sqlite3.connect('Game_avt.db')
        self.curso = connect.cursor()

        self.title("Game")
        width_display = self.winfo_screenwidth()
        height_display = self.winfo_screenheight()
        width_start = int(width_display/100*10)
        height_start = int(height_display/100*5)
        self.geometry('1530x900+{}+{}'.format(width_start,height_start))
        self.resizable(width=False, height=False)

        self.Frame_Enter = Frame(width=2300, height=900)
        self.Frame_Enter.place(x=1, y=1)
        self.bg_enter = Image.PhotoImage(file='Gen_back.png')
        self.canvas = Canvas(self.Frame_Enter, width=2300, height=900)
        self.canvas.create_image(100,100,image=self.bg_enter)
        self.canvas.place(x=0,y=0)

    #Размещение иконок, текста и полей ввода.#Перенести сначала создание кнопки

        self.user_ico = PhotoImage(file='user_ico.png')
        self.canvas.create_image(1530/2-190, 240, image=self.user_ico)

        inputs_login = Entry(self.Frame_Enter, font=("Comic Sans MS", 20))
        inputs_login.place(x=1530/2-150, y=220)
        inputs_login.insert(END, 'Логин')

        self.password_ico = PhotoImage(file='password_ico.png')
        self.canvas.create_image(1530/2-190, 390, image=self.password_ico)

        inputs_password = Entry(self.Frame_Enter, font=("Comic Sans MS", 20))#show='•') 
        inputs_password.place(x=1530/2-150, y=370)
        inputs_password.insert(END, 'Пароль') 


        self.Frame_new = Frame(width=2300, height=900)
        


        def lol():
            self.Frame_new.place_forget()
            self.Frame_Enter.place(x=10,y=10)


        but = Button(self.Frame_new, text="lol", command=lol, width=120, height=30)
        but.place(x=100, y=120)




        def test():
            self.Frame_Enter.place_forget()
            self.Frame_new.place(x=10, y=10)
           
            #Frame_new.grid()
            # self.Frame_Enter.grid_remove()
 


    
        Enter_start = Button(self.Frame_Enter, text='Вход', font=("Comic Sans MS", 15),
                        width=11, height=1,
                        bd=3, background='#ddfeff', relief=GROOVE,
                        activebackground='#faacb9', command=test)
        Enter_start.place(x=690, y=450) #(x=1530/2-90, y=470)

        #self.registr_ico = PhotoImage(width=20, height=20, file='registr_ico.png')
        Registr_but = Button(self.Frame_Enter, text="Регистрация", 
        font=("Comic Sans MS", 10), width=11, height=1,
        background='#ddfeff', relief=FLAT, bd=0,
        activebackground='#faacb9') #command=self.registr_start)
        Registr_but.place(x=715, y=545) #(x=1400, y=800)

           #Логика работы окна. 

        def inputs_login_clear(self):
            inputs_login.config(state='normal', background='white')
            if inputs_login.get() in 'Логин':
                inputs_login.delete(0, END)
            else:
                pass

        def inputs_login_txt(self):
            if inputs_login.get() == '':
                inputs_login.insert(END, 'Логин')
                inputs_login.config(state='disable', disabledbackground='white', show='')

        def inputs_password_clear(self):
            inputs_password.config(state='normal', background='white', show='•')
            if inputs_password.get() in 'Пароль':
                inputs_password.delete(0, END)
            else:
                pass

        def inputs_password_txt(self):
            if inputs_password.get() == '':
                inputs_password.insert(END, 'Пароль')
                inputs_password.config(state='disable', disabledbackground='white', show='')

        # Функия изменения цвета кнопки, при наведении

        if inputs_login.bind('<Enter>', inputs_login_clear)==True:
            pass
        elif inputs_login.bind('<Leave>',inputs_login_txt)==True:
            pass
        elif inputs_login.bind('<FocusOut>', inputs_password_txt)==True:
            pass

        if inputs_password.bind('<Enter>', inputs_password_clear)==True:
            pass
        elif inputs_password.bind('<Leave>',inputs_password_txt)==True:
            pass
        elif inputs_password.bind('<FocusOut>', inputs_password_txt)==True:
            pass
        

        def new_color_enter_start_1(self):
            Enter_start['background']='#b7fdff'

        def new_color_enter_start_2(self):
            Enter_start['background']='#ddfeff'

        Enter_start.bind('<Enter>', new_color_enter_start_1)
        Enter_start.bind('<Leave>', new_color_enter_start_2)

        def focus_registr(self):
            Registr_but['background']='#b7fdff'

        def no_focus_registr(self):
            Registr_but['background']='#ddfeff'

        Registr_but.bind('<Enter>', focus_registr)
        Registr_but.bind('<Leave>', no_focus_registr)

# # frame_start = Frame(win, width=300, height=300, bg='red')

#Класс окна входа, авторизации и старта
# class Enter():
#     def __init__(self, *arg, **kwars):
        
        
        
#       
#         

#        








class Menu(General):
    # def __init__(self, *arg, **kwargs):
    def test():
        print(">>>   ", 100)
            # self.self.Frame_Enter.forget(self.self.Frame_Enter)
            # Frame_Menu = Frame(width=2300, height=900)
            # Frame_Menu.place(x=1, y=1)

# def registr_start():
# #    win.forget(frame_2)
#     frame_2 = Frame(win, width=2300, height=900)
#     canvas = Canvas(frame_2, width=2300, height=900)
#     canvas.create_image(100,100,image=bg_enter)
#     canvas.place(x=1,y=1)
#     frame_2.place(x=1, y=1)
#     # print(lis)




#     # win.grid_remove()
#     # Win_Enter = Frame(win, width=590, height=620, bg='red')




# def start():
#     login = inputs_login.get()
#     password = inputs_password.get()
#     inputs_login.insert(0, '')
#     inputs_password.insert(0, '')
#     login = str(login)
#     password = str(password)
#     Lib_enter.check_enter(login, password)

  























# # def start_registr():
# #     login = inputs_login.get()
# #     inputs_login.insert(END, '')
# #     login = str(login)
# #     Lib_enter.chek_login(login) 
# #     z = Lib_enter.alerts(z='')

    














if __name__ == "__main__":
    general = General()
    general.mainloop()

