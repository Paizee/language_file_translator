import tkinter
from tkinter import font
from deep_translator import DeeplTranslator,GoogleTranslator
                        

def translate_():
    is_translated.delete("1.0","end")
    input = to_translate.get("1.0",tkinter.END)
    if selected_trans.get() == "Google Translator": 
        translator =  GoogleTranslator(source='auto', target=selected_lang.get())
    elif selected_trans.get() == "DeepL (api_key required)":
        translator = DeeplTranslator(source='auto', target=selected_lang.get(), api_key=api_key_input.get())
    inside_quotes = False
    current_part = ""
    input_list = []
    
    for char in input:
        if char == '"':
            inside_quotes = not inside_quotes
        elif char == ',' and inside_quotes:
            current_part += char
        elif char == ',' and not inside_quotes:
            input_list.append(current_part)
            current_part = ""
        else:
            current_part += char

    if current_part:
        input_list.append(current_part)
    
    
   
    for x in input_list:
        if x.count(":") == 1:
            parts = x.split(":", 1)

        
            if len(parts) == 2:
                left_side, right_side = parts[0].strip('"'), parts[1].strip('"')
                
                if len(right_side) == 1:
                    right_side = left_side
                    
                translated_string = f'"{left_side}": "{translator.translate(text=right_side)}",\n'
                

                is_translated.insert(tkinter.END,translated_string)
        else:
            parts = x.split(":", 2)

        
            if len(parts) == 3:
                left_side, right_side = parts[0].strip('"'), parts[2].strip('"')
                
                if len(right_side) == 1:
                    right_side = left_side
                    
                translated_string = f'"{left_side}:": "{translator.translate(text=right_side)}:",\n'
                
                                
                is_translated.insert(tkinter.END,translated_string)



mw=tkinter.Tk()
mw.title("Translator for Languages file")
mw.geometry("750x480")
mw.config(background="#303030")
mw.resizable(width=False, height=False)
mw.iconbitmap("my_icon.ico")

scrollbar = tkinter.Scrollbar(mw)
scrollbar.place(x=332,y=150,anchor= "e",height=200)

scrollbar1 = tkinter.Scrollbar(mw)
scrollbar1.place(x=720,y=150,anchor= "e",height=200)


label_font = font.Font(family='Helvetica', name='label_font', size=12, weight='bold')
text_font = font.Font(family='Arial', name='text_font', size=8, weight='bold')
label1 = tkinter.Label(mw,text="To Translate",font=label_font,bg="#303030",fg="#DCDCDC")
label1.place(x=110,y=10)


label2 = tkinter.Label(mw,text="Translated",font=label_font,bg="#303030",fg="#DCDCDC")
label2.place(x=515,y=10)


to_translate = tkinter.Text(mw,yscrollcommand = scrollbar.set,font=text_font)
to_translate.place(x=15,y=50,width=300, height=200)



is_translated = tkinter.Text(mw,yscrollcommand = scrollbar1.set,font=text_font)
is_translated.place(x=405,y=50,width=390, height=200)
scrollbar.config(command=to_translate.yview)
scrollbar1.config(command=is_translated.yview)

label2 = tkinter.Label(mw,text="Selected Language: " ,font=label_font,bg="#303030",fg="#DCDCDC")
label2.place(x=150,y=270)

label3 = tkinter.Label(mw,text="Selected Translator: " ,font=label_font,bg="#303030",fg="#DCDCDC")
label3.place(x=150,y=300)

label4 = tkinter.Label(mw,text="Api key: " ,font=label_font,bg="#303030",fg="#DCDCDC")
label4.place(x=150,y=330)




languages = GoogleTranslator().get_supported_languages()



list_of_translators = [
    "Google Translator",
    "DeepL (api_key required)"
]

selected_lang = tkinter.StringVar()
selected_lang.set( "nothing" )

selected_trans = tkinter.StringVar()
selected_trans.set( "nothing" )


api_key_input = tkinter.Entry(mw,font=text_font,bg="#303030",fg="#DCDCDC")
api_key_input.place(x=350,y=330,width=250,height=25,bordermode="ignore")

drop = tkinter.OptionMenu(mw,selected_lang,*languages)
drop.place(x=350,y=270,width=250,height=25,bordermode="ignore")

drop1 = tkinter.OptionMenu(mw,selected_trans,*list_of_translators)
drop1.place(x=350,y=300,width=250,height=25,bordermode="ignore")

button = tkinter.Button(mw, text='Translate', width=15, command=translate_)
button.place(x=300, y=450)





mw.mainloop()