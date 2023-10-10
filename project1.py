from hanspell import spell_checker
text= '어비자가방에 들어가신다나는 오늘 코딩을했다.'
hanspell_sent = spell_checker.check(text)
print(hanspell_sent.checked)