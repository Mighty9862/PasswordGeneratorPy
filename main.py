import customtkinter
import tkinter
import random

customtkinter.set_appearance_mode("light")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Генератор паролей')
        self.geometry('600x600')

        chars = 'qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM'
        symbols = '+-#&%#$@^*$'
        a = ''

        self.chars_with_symbols = list(chars + chars.upper() + symbols)
        self.chars_without_symbols = list(chars + chars.upper())


        self.count_pass = customtkinter.CTkLabel(self, text='Кол-во паролей: ').place(x=70, y=410)
        self.entry_count = customtkinter.CTkEntry(self, width=100)
        self.entry_count.place(x=190, y=410)

        self.len_pass = customtkinter.CTkLabel(self, text='Длина паролей: ').place(x=70, y=460)
        self.entry_len = customtkinter.CTkEntry(self, width=100)
        self.entry_len.place(x=190, y=460)

        self.btn_clear = customtkinter.CTkButton(self, text='Очистить', command=self.clear)
        self.btn_clear.place(x=350, y=520)

        self.btn_generate = customtkinter.CTkButton(self, text='Генерировать', command=self.generate)
        self.btn_generate.place(x=150, y=520)

        self.text_field = customtkinter.CTkTextbox(self, width=560, height=300)
        self.text_field.place(x=20, y=30)


        self.symbol_var = tkinter.BooleanVar()
        self.symbol_var.set(False)
        customtkinter.CTkLabel(self, text='Специальные символы: ').place(x=350, y=400)
        customtkinter.CTkRadioButton(self, text='Без специальных символов', variable=self.symbol_var, value=False).place(x=350, y=440)
        customtkinter.CTkRadioButton(self, text='Со специальными символами', variable=self.symbol_var, value=True).place(x=350, y=470)

    def validate_input(self, entry):
        try:
            int(entry.get())
            return True
        except ValueError:
            return False

    def generate(self):
        if self.validate_input(self.entry_len) and self.validate_input(self.entry_count):
            len_passwords = int(self.entry_len.get())
            count_passwords = int(self.entry_count.get())
            if self.symbol_var.get():
                characters = self.chars_with_symbols
            else:
                characters = self.chars_without_symbols
            for i in range(count_passwords):
                password = ''
                for j in range(len_passwords):
                    password += random.choice(characters)
                self.text_field.insert(tkinter.END, password+'\n')
            self.text_field.insert(tkinter.END, '-'*80+'\n')
        else:
            tkinter.messagebox.showerror("Ошибка!", "Неверные данные. Введите целые числа")
        
    def clear(self):
        self.text_field.delete(0.0, tkinter.END)


if __name__ == '__main__':

    app = App()
    app.mainloop()