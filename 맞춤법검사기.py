import tkinter as tk
from tkinter import messagebox
from hanspell import spell_checker

def check_spelling():
    text = text_entry.get("1.0", "end-1c")
    corrected_text = spell_checker.check(text).checked
    

    result_text.delete("1.0", "end")
    result_text.insert("1.0", corrected_text)

    char_count_including_spaces = len(corrected_text)
    char_count_excluding_spaces = len(corrected_text.replace(' ', ''))
    char_count.set(f"공백포함: {char_count_including_spaces}, 공백제외: {char_count_excluding_spaces}")

def reset_text():
    text_entry.delete("1.0", "end")
    result_text.delete("1.0", "end")
    char_count.set("공백포함: 0, 공백제외: 0")

root = tk.Tk()
root.title("한글 맞춤법 검사기")


# 이미지를 로드
image = tk.PhotoImage(file="야옹이.png")

# 이미지를 표시할 레이블 생성
image_label = tk.Label(root, image=image)
image_label.pack()



text_entry = tk.Text(root, width=40, height=10)
text_entry.pack()

check_button = tk.Button(root, text="맞춤법 검사", command=check_spelling, 
                         bg="#498AFF", fg="white", font=("Helvetica", 12, "bold"))
check_button.pack()

result_text = tk.Text(root, width=40, height=10)
result_text.pack()

char_count = tk.StringVar()
char_count_label = tk.Label(root, textvariable=char_count)
char_count_label.pack()

reset_button = tk.Button(root, text="초기화", command=reset_text, 
                         bg="#498AFF", fg="white", font=("Helvetica", 12, "bold"))
reset_button.pack()

root.mainloop()
