import customtkinter as ctk
from pypower import String
from pyperclip import copy
#screen and welcome
app = ctk.CTk()
app.geometry(f'1200x900+{(1680/2)+50}+{(1050/2)+50}')
ctk.CTkLabel(app, text='Welcome to sk!', font=('arial', 30)).pack(pady=20)
ctk.CTkLabel(app, text="   example: lpl] ➡ محمد", font=('arial arabic', 25)).place(x=0, y=100)
#input from user
text = ctk.CTkTextbox(app, width=800, font=('arial arabic', 30))
text.pack(pady=50)
result = ctk.CTkTextbox(app, width=800, font=('arial arabic', 30))
def convert():
    result.delete('1.0', 'end')
    result.insert('1.0', String(text.get('1.0', 'end')).sk().replace('\n\n', '\n'))
ctk.CTkButton(app, text='convert', font=('arial', 40), command=convert).pack()
result.pack(pady=30)
ctk.CTkButton(app, text='Copy', font=('arial', 40), command=lambda: copy(result.get('1.0', 'end'))).pack()
ctk.CTkButton(app, text='Clean', command=lambda: text.delete('1.0', 'end')).place(x=1030, y=200)
app.mainloop()
