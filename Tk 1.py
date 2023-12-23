from tkinter import *
import tkinter.messagebox
import csv
import webbrowser
import customtkinter
from PIL import Image
import random
window = Tk()
window.title('Null Void')
window.geometry('1280x720')
window.resizable(False,False)
window.config(bg='White')
x = 0
y = 0
#########---------------Beginning of The Second Window----------------------------------------
def new_window(event):
    if password.get() == confirm_password.get():
        tkinter.messagebox.showinfo('Notice', 'Sign up successful')
        database = [username.get(), password.get(), confirm_password.get()]

        with open('Database', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(database)
        window.destroy()

        window2 = Tk()
        window2.title('Null Void')
        window2.geometry('1280x720')
        window2.resizable(False,False)
        window2.config(bg='White')

        ########-----------second window's Frames---------------------------------------------

        win_frame1 = Frame(window2, bg='white', width=320, height=900)
        win_frame1.pack(anchor='e', padx=50)

        win_frame2 = Frame(win_frame1, width=280, height=2, bg='black')
        win_frame2.place(x=10, y=224)

        win_frame3 = Frame(win_frame1, width=280, height=2, bg='black')
        win_frame3.place(x=10, y=295)

        win_frame4 = Frame(win_frame1, width=280, height=2, bg='black')
        win_frame4.place(x=10, y=367)

        win_frame5 = Frame(win_frame1, width=280, height=2, bg='black')
        win_frame5.place(x=10, y=425)

        win_frame6 = Frame(window2, height=500, width=500, bg='white')
        win_frame6.pack(anchor='w')

        #######---------------Second Windows Images-------------------------------------------

        win2_pic = PhotoImage(file='photo-14595.png')

        win2_label2 = Label(window2, image=win2_pic, bg='white')
        win2_label2.place(x=0, y=0)

        win2_pic2 = PhotoImage(file='429d.png')

        win2_label3 = Label(window2, image=win2_pic2, bg='white')
        win2_label3.place(x=520, y=370)

        #########-----------whatsapp and Gmail Button links------------------------------------

        def open_email():
            webbrowser.open_new(r'http://awadud197@gmail.com')

        def open_wap():
            webbrowser.open_new(r'http://www.whatsapp.com')

        #########-----------Whatsapp and Gmail Buttons-------------------------------------------

        win2_pic3 = PhotoImage(file='images.png')

        win2_label3 = Button(win_frame1, image=win2_pic3, bg='white', border=0,command=open_email)
        win2_label3.place(x=20, y=500)

        win2_pic4 = PhotoImage(file='images (1).png')

        win2_label3 = Button(win_frame1, image=win2_pic4, bg='white', border=0,command=open_wap)
        win2_label3.place(x=190, y=510)

        ########-------------My insanely long welcome message------------------------------------

        win2_label4 = Label(window2, text="We're absolutely thrilled to welcome", font=('Microsoft yaHei UI Light',),
                            bg='white', fg='#57a1f8')
        win2_label4.place(x=613, y=130)

        win2_label4 = Label(window2, text="you to our community at Null Void!", font=('Microsoft yaHei UI Light',),
                            bg='white', fg='#57a1f8')
        win2_label4.place(x=613, y=160)

        win2_label4 = Label(window2, bg='white', fg='#57a1f8', font=('Microsoft yaHei UI Light',),
                            text="Whether you're here to connect, learn,")
        win2_label4.place(x=613, y=190)

        win2_label4 = Label(window2,bg='white', fg='#57a1f8',font=('Microsoft yaHei UI Light',),text="or simply explore"
                            ", we're delighted to ")
        win2_label4.place(x=613,y=260)

        win2_label4 = Label(window2, bg='white', fg='#57a1f8', font=('Microsoft yaHei UI Light',)
                            ,text='have you as part of our growing family.')
        win2_label4.place(x=613,y=290)

        win2_label4 = Label(window2, bg='white', fg='#57a1f8', font=('Microsoft yaHei UI Light',)
                            , text='This platform is designed with one goal')
        win2_label4.place(x=613,y=320)

        win2_label4 = Label(window2, bg='white', fg='#57a1f8', font=('Microsoft yaHei UI Light',)
                            ,text='in mind: to create an inclusive and')
        win2_label4.place(x=613,y=350)

        win2_label4 = Label(window2, bg='white', fg='#57a1f8', font=('Microsoft yaHei UI Light',)
                            ,text='vibrant space where members can connect. Feel free to navigate around,')
        win2_label4.place(x=20, y=400)

        win2_label4 = Label(window2, bg='white', fg='#57a1f8', font=('Microsoft yaHei UI Light',)
                            ,text='engage with other members, share your insights and make the most of')
        win2_label4.place(x=20, y=430)

        win2_label4 = Label(window2, bg='white', fg='#57a1f8', font=('Microsoft yaHei UI Light',)
                            ,text='your experience. Should you have any questions or need assistance,')
        win2_label4.place(x=20, y=460)

        win2_label4 = Label(window2, bg='white', fg='#57a1f8', font=('Microsoft yaHei UI Light',)
                            ,text='our support team is always here to help. We encourage you to dive')
        win2_label4.place(x=20, y=490)

        win2_label4 = Label(window2, bg='white', fg='#57a1f8', font=('Microsoft yaHei UI Light',)
                            ,text='in, explore the various sections and make yourself at home. Your voice,')
        win2_label4.place(x=20, y=520)

        win2_label4 = Label(window2, bg='white', fg='#57a1f8', font=('Microsoft yaHei UI Light',)
                            ,text='opinions, and contribution are incredibly valuable and play a vital role in')
        win2_label4.place(x=20, y=550)

        win2_label4 = Label(window2, bg='white', fg='#57a1f8', font=('Microsoft yaHei UI Light', )
                            , text='shaping our community. Thank you for choosing to be part of Null Void')
        win2_label4.place(x=20, y=580)

        #########-----------Beginning of The Final Window-------------------------------------------

        def next_page(event):
            user_details = [
                win2_name.get() ,
                win2_lname.get() ,
                win2_email.get() ,
                win2_dob.get()
            ]

            with open('User_Data', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(user_details)

            window2.destroy()
            window3 = customtkinter.CTk()
            window3.title('Null Void')
            window3.geometry('1280x720')
            window3.resizable(True,True)
            window3.config(bg='white')
            #########-------------------------------------------------
            x = 0
            y = 0
            #########------------The Third Window's Images----------------------------------------

            win3_pic1 = PhotoImage(file='phone.png')

            win3_label = Label(window3, image=win3_pic1, bg='white', height=530)
            win3_label.place(x=870, y=120)

            win3_pic2 = customtkinter.CTkImage(light_image=Image.open('Vision-Glossary.png'),
                                               dark_image=Image.open('Vision-Glossary.png'),
                                               size=(260, 150))

            ########--------------The Name of The Chatbot----------------------------------------

            win3_label3 = Label(window3, text='Null Void Chatbot 🤖', font=('Impact', 20), bg='white', fg='#57a1f8')
            win3_label3.place(x=480, y=50)

            #######----------------My customer Service Button-----------------------------------------

            def customer_service():
                tkinter.messagebox.showinfo('Customer Service Line',
                                            'Contact the creator of Null Void On the following Number:\n'
                                            '    +233246850933, On WhatsApp and Telegram')

            win3_label4 = customtkinter.CTkButton(window3, image=win3_pic2, text='', corner_radius=30, bg_color='white',
                                                  fg_color='white',
                                                  command=customer_service)
            win3_label4.place(x=0, y=70)

            #########---------------Third Window's Frames----------------------------------

            win3_frame = customtkinter.CTkFrame(window3, width=650, height=530, corner_radius=80, bg_color='white')
            win3_frame.place(x=280, y=90)

            win3_frame7 = Frame(win3_frame, width=2, height=400, bg='white')
            win3_frame7.place(x=30, y=65)

            win3_frame8 = Frame(win3_frame, width=2, height=400, bg='white')
            win3_frame8.place(x=620, y=65)

            ########-------------The New Chat/Clear Chat Function-----------------------------------------

            def clear_chat():
                global y
                y = 0
                for widget in win3_frame9.winfo_children():
                    widget.destroy()

            #########-----------The Third Window's Buttons-------------------------------------------

            win3_button2 = customtkinter.CTkButton(window3, text='New Chat ++', width=250, height=50, border_width=0,
                                                   command=clear_chat,
                                                   corner_radius=30, bg_color='white', font=('impact', 20))
            win3_button2.place(x=10, y=250)

            win3_button3 = customtkinter.CTkButton(window3, width=250, height=50, border_width=0, corner_radius=30,
                                                   bg_color='white',
                                                   font=('impact', 20))
            win3_button3.place(x=10, y=320)

            win3_button4 = customtkinter.CTkButton(window3, width=250, height=50, border_width=0, corner_radius=30,
                                                   bg_color='white',
                                                   font=('impact', 20))
            win3_button4.place(x=10, y=400)

            win3_button5 = customtkinter.CTkButton(window3, width=250, height=50, border_width=0, corner_radius=30,
                                                   bg_color='white',
                                                   font=('impact', 20))
            win3_button5.place(x=10, y=480)

            win3_button6 = customtkinter.CTkButton(window3, width=250, height=50, text='Exit', command=quit,
                                                   border_width=0,
                                                   corner_radius=30, bg_color='white', font=('impact', 20))
            win3_button6.place(x=10, y=560)

            #########----------------------------------------------------------

            win3_frame9 = customtkinter.CTkFrame(win3_frame, width=580, height=405)
            win3_frame9.place(x=35, y=60)

            #########------------The Third Window's Entry Box--------------------------------------------

            def on_click(event):
                final_entry2.delete(0, 'end')

            def on_leave(event):
                if final_entry2 == '':
                    final_entry2.insert(0, 'Write a message')

            final_entry2 = customtkinter.CTkEntry(win3_frame, width=400)
            final_entry2.insert(0, 'Write a message')
            final_entry2.bind('<FocusIn>', on_click)
            final_entry2.bind('<FocusOut>', on_leave)
            final_entry2.place(x=80, y=490)

            ########----------------THE CORE OF THE CODE-----------------------------------------------

            def inquire():
                win3_label1.destroy()
                global y
                u = final_entry2.get()
                user = customtkinter.CTkLabel(win3_frame9, text=u + ' :🙅',wraplength=550,
                                              font=('Microsoft yaHei UI Light', 15, 'bold'), corner_radius=20)
                user.place(x=570, y=y + 20, anchor='e')
                final_entry2.delete(0, 'end')

                if 'Hello' in u or 'Hi' in u or 'Hey' in u or 'Hey there' in u:
                    response = ['Hello, how are you', 'Hi, how can I help you', 'Nice to meet you', 'Hi there', 'Hey',
                                "What's up"]
                    response = random.choice(response)

                    bot = customtkinter.CTkLabel(win3_frame9, text=f'🤖: {response}',
                                                 font=('Microsoft yaHei UI Light', 15, 'bold'), corner_radius=20)
                    bot.place(x=0, y=y + 45, anchor='w')

                elif 'How are you' in u or 'How are you doing' in u:
                    response_2 = ["I'm fine", "I'm fine, thanks for asking", "I'm good", "I'm good, what about you"]
                    response_2 = random.choice(response_2)

                    bot = customtkinter.CTkLabel(win3_frame9, text=f"🤖: {response_2}",
                                                 font=('Microsoft yaHei UI Light', 15, 'bold'), corner_radius=20)
                    bot.place(x=0, y=y + 45)

                elif 'Can i ask you something' in u:
                    response_3 = ['Sure, what is it?', 'Sure!', 'Okay, go ahead', 'Yes, of course', 'Yeah',
                                  'Yh, ask away']
                    response_3 = random.choice(response_3)

                    bot = customtkinter.CTkLabel(win3_frame9, text=f"🤖: {response_3}",
                                                 font=('Microsoft yaHei UI Light', 15, 'bold'), corner_radius=20)
                    bot.place(x=0, y=y + 45)

                elif u == '' or u == ' ':
                    response_4 = ['Please say something so that I may help you',
                                  "It seems you haven't entered any text. Please type something for me to respond to",
                                  "I'm sorry, but I couldn't understand your message. Could you please provide more information?",
                                  "It appeared you haven't entered any input. How can I assist you today?",
                                  "Hmm, It seems there's nothing in your message. Can you please provide a valid input?",
                                  "I'm afraid I can't respond to an empty message. Please enter a valid input or question"]
                    response_4 = random.choice(response_4)

                    bot = customtkinter.CTkLabel(win3_frame9, text=f"🤖: {response_4}",wraplength=550,
                                                 font=('Microsoft yaHei UI Light', 15, 'bold'), corner_radius=20)
                    window3.update_idletasks()
                    label_height = bot.winfo_reqheight()
                    bot.place(x=0, y=y + 45)
                    y += label_height + 5

                else:
                    from openai import OpenAI
                    client = OpenAI()
                    completion = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            # {"role": "system", "content": f"Hello"},
                            {"role": "user", "content": f"{u}"}
                        ]
                    )
                    a = completion.choices[0].message.content

                    bot = customtkinter.CTkLabel(win3_frame9, text=f"🤖: {a}",wraplength=550,
                                                 font=('Microsoft yaHei UI Light', 15, 'bold'), corner_radius=20)
                    window3.update_idletasks()
                    label_height = bot.winfo_reqheight()
                    bot.place(x=0, y=y + 45)
                    y += label_height + 5
                y += 60

            #########-----------The Third Window's Send Button-------------------------------------------

            send_button = customtkinter.CTkButton(win3_frame, text='Send', width=100, command=inquire)
            send_button.place(x=490, y=490)

            ########------------------The Third Windows Welcome Text--------------------------------------------
            user = database[0]
            win3_label1 = customtkinter.CTkLabel(win3_frame, text=f'Hello {user} and Welcome to Null Void Chatbot\n'
                                                                  f'How may I be of service to you',
                                                 font=('impact', 20, 'bold'),bg_color='#333333',
                                                 corner_radius=20,anchor='center')
            win3_label1.place(x=65, y=220)

            window3.mainloop()

        #######----------------The Second Window's Continuation------------------------------------------

        win2_label = Label(win_frame1, text="Tell Us About Yourself!", fg='#57a1f8', bg='white',
                           font=('Microsoft yaHei UI Light', 20, 'bold'))
        win2_label.place(x=0, y=100)

        #######---------------The Second Window's First Entry Box------------------------------------------

        def hover_in(event):
            win2_name.delete(0, 'end')

        def hover_out(event):
            if win2_name.get() == '':
                win2_name.insert(0, 'First Name')

        win2_name = Entry(win_frame1, border=0, font=('Microsoft yaHei UI Light',))
        win2_name.insert(0, 'First Name')
        win2_name.bind('<FocusIn>',hover_in)
        win2_name.bind('<FocusOut>',hover_out)
        win2_name.place(x=66, y=200)

        #######--------------The Second Window's Second Entry Box--------------------------------------------

        def hover_in(event):
            win2_lname.delete(0, 'end')

        def hover_out(event):
            if win2_lname.get() == '':
                win2_lname.insert(0, 'Last Name')

        win2_lname = Entry(win_frame1, border=0, font=('Microsoft yaHei UI Light',))
        win2_lname.insert(0, 'Last Name')
        win2_lname.bind('<FocusIn>',hover_in)
        win2_lname.bind('<FocusOut>',hover_out)
        win2_lname.place(x=66, y=270)

        #######--------------The Second Window's Third Entry Box--------------------------------------------

        def hover_in(event):
            win2_email.delete(0, 'end')

        def hover_out(event):
            if win2_email.get() == '':
                win2_email.insert(0, 'Email Address')

        win2_email = Entry(win_frame1, border=0, font=('Microsoft yaHei UI Light',))
        win2_email.insert(0, 'Email Address')
        win2_email.bind('<FocusIn>',hover_in)
        win2_email.bind('<FocusOut>',hover_out)
        win2_email.place(x=66, y=340)

        #######---------------The Second Window's Final Entry Box-------------------------------------------

        def hover_in(event):
            win2_dob.delete(0, 'end')

        def hover_out(event):
            if win2_dob.get() == '':
                win2_dob.insert(0, 'DD/MM/YYYY')

        win2_dob = Entry(win_frame1, border=0, font=('Microsoft yaHei UI Light',))
        win2_dob.insert(0, 'DD/MM/YYYY')
        win2_dob.bind('<FocusIn>',hover_in)
        win2_dob.bind('<FocusOut>',hover_out)
        win2_dob.place(x=66, y=400)

        continue_btn = Button(win_frame1, border=1, text='Continue', bg='#57a1f8', fg='white', width=25,
                              font=('Microsoft yaHei UI Light',))
        continue_btn.bind('<Button-1>', next_page)
        continue_btn.place(x=25, y=450)

        window2.mainloop()

    elif password.get() != confirm_password.get():
        tkinter.messagebox.showinfo('Notice', 'Password does not match: Please check and try again')

########---------------The First Window's Frames----------------------------------------------


frame1 = Frame(window,width=690, height=900, bg='Gray')
frame1.pack(side=LEFT)

frame2 = Frame(window,width=320, height=900, bg='white')
frame2.pack(side=LEFT)

frame3 = Frame(window,width=320, height=900, bg='white')
frame3.pack(side=LEFT)
#########---------------The First Window's Images------------------------------------------

pic = PhotoImage(file='Guy_and_computer@2x.png')

label = Label(frame1,text='',image=pic, bg='White')
label.place(anchor='center',x=100,y=300)

pic2 = PhotoImage(file='working-home-vector-.png')

label2 = Label(frame3,image=pic2,bg='white')
label2.place(anchor='center',x=160,y=600)

#########---------------------------------------------------------

heading = Label(frame2, text='Sign Up', bg='White', fg='#57a1f8',font=('Microsoft yaHei UI Light', 20, 'bold'))
heading.place(x=100,y=180)

#########-------------Code For The First Window's Username Entry Box--------------------------------------------

def hover_in(event):
    username.delete(0,'end')

def hover_out(event):
    if username.get() == '':
        username.insert(0,'username')


username = Entry(frame2, border=0,bg='White', width=25, font=('Microsoft yaHei UI Light',))
username.place(x=50,y=240)
username.bind('<FocusIn>',hover_in)
username.bind('<FocusOut>',hover_out)
username.insert(0,'username')

user_frame = Frame(frame2,width=285,height=2,bg='black')
user_frame.place(x=25,y=262)

#########--------------Code For The First Window's Password Entry Box-------------------------------------------

def hover_in(event):
    password.delete(0,'end')

def hover_out(event):
    if password.get() == '':
        password.insert(0,'password')


password = Entry(frame2, border=0, bg='white', width=25, font=('Microsoft yaHei UI Light',))
password.place(x=50,y=300)
password.bind('<FocusIn>',hover_in)
password.bind('<FocusOut>',hover_out)
password.insert(0,'password')

pass_frame = Frame(frame2,width=285,height=2,bg='black')
pass_frame.place(x=25,y=322)

#########--------------Code For The First Window's Confirm Entry Box------------------------------------

def hover_in(event):
    confirm_password.delete(0, 'end')


def hover_out(event):
    if confirm_password.get() == '':
        confirm_password.insert(0, 'confirm password')


confirm_password = Entry(frame2, border=0, bg='white', width=25, font=('Microsoft yaHei UI Light',))
confirm_password.place(x=50,y=360)
confirm_password.bind('<FocusIn>',hover_in)
confirm_password.bind('FocusOut>',hover_out)
confirm_password.insert(0,'confirm password')

con_frame = Frame(frame2,width=285,height=2,bg='black')
con_frame.place(x=25, y=382)

#########--------------Checkbox Button-------------------------------------------

check = Checkbutton(frame2, bg='white', text='Agree to all terms and conditions', font=('Microsoft yaHei UI Light',))
check.place(x=30,y=415)

#########----------------The First Window's Sign Up Button-----------------------

sign_btn = Button(frame2, border=1,text='Sign Up', bg='#57a1f8', fg='white',width=25,font=('Microsoft yaHei UI Light',))
sign_btn.bind('<Button-1>', new_window)
sign_btn.place(x=50,y=470)

window.mainloop()