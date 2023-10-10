import tkinter as tk
from hanspell import spell_checker

spell = spell_checker()

def spell_check1():
    input_text.tag_remove("misspelled", "1.0", tk.END)
    text = input_text.get("1.0", "end-1c")
    words = text.split()
    has_errors = False
    
    for word in words:
        if not spell.correction(word) == word:
            start = "1.0"
            while True:
                start = input_text.search(word, start, stopindex=tk.END)
                if not start:
                    break
                end = f"{start}+{len(word)}c"
                input_text.tag_add("misspelled", start, end)
                input_text.tag_config("misspelled", foreground="red", underline=True)
                start = end
                has_errors = True
    
    if not has_errors:
        result_label.config(text="오류없음")
    else:
        result_label.config(text="오류있음")

def replace_word():
    selected_word = input_text.get(tk.SEL_FIRST, tk.SEL_LAST)
    corrected_word = spell.correction(selected_word)
    
    if corrected_word != selected_word:
        input_text.tag_remove("misspelled", tk.SEL_FIRST, tk.SEL_LAST)
        input_text.insert(tk.SEL_FIRST, corrected_word)
        input_text.tag_add("corrected", tk.SEL_FIRST, tk.SEL_LAST)
        input_text.tag_config("corrected", foreground="blue")

def reset_text():
    input_text.delete("1.0", tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("맞춤법 검사기")

input_text = tk.Text(root, height=10, width=40)
input_text.pack()

check_button = tk.Button(root, text="검사", command=spell_check1)
check_button.pack()

correct_button = tk.Button(root, text="맞춤법고치기", command=replace_word)
correct_button.pack(side=tk.RIGHT)

reset_button = tk.Button(root, text="초기화", command=reset_text)
reset_button.pack(side=tk.LEFT)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()