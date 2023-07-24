from gtts import gTTS
import tkinter as tk
from tkinter import filedialog
import os
from docx import Document
from PyPDF2 import PdfReader
from tkinter import messagebox

window = tk.Tk()
window.title("Text to speech")
window.geometry("300x200")

language = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Russian": "ru",
    "Spanish": "es",
    "Turkish": "tr",
}

def open_file():
    file_path = filedialog.askopenfilename()
    return file_path

def browse_and_print():
    selected_file = open_file()
    base_name, extension = os.path.splitext(selected_file)
    file_name = os.path.basename(selected_file)
    selected_lang = selected_language.get()

    if extension == '.pdf':
        with open(selected_file, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            tts = gTTS(text, lang=language[selected_lang])
            tts.save(f"{file_name}.mp3")
            messagebox.showinfo('Status', 'The file is saved in the same directory as this program')

    elif extension == '.docx':
        doc = Document(selected_file)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        tts = gTTS(text, lang=language[selected_lang])
        tts.save(f"{file_name}.mp3")
        messagebox.showinfo('Status', 'The file is saved in the same directory as this program')

    elif extension == '.txt':
        with open(selected_file, 'r') as file:
            text = file.read()
            tts = gTTS(text, lang=language[selected_lang])
            tts.save(f"{file_name}.mp3")
            messagebox.showinfo('Status', 'The file is saved in the same directory as this program')


label = tk.Label(window, text="Browse your file", font=8)
button_1 = tk.Button(window, text='Browse', command=browse_and_print)

selected_language = tk.StringVar()
selected_language.set(language["English"])
language_option = tk.OptionMenu(window, selected_language, *language.keys())

label.place(relx=0.5, rely=0.4, anchor='center')
button_1.place(relx=0.5, rely=0.8, anchor='center')
language_option.place(relx=0.5, rely=0.6, anchor='center')

window.mainloop()