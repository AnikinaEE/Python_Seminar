# Задача №27
# Пользователь вводит текст (строка). Словом считается
# последоватльность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом
# тексте.

text = "She sells sea shells on the shore The shells \
        that she sells I'm sure.So if she sells sea \
        shells on the sea shore I'm sure that shells \
        are sea shore shells".lower()
text = text.replace('.', ' ').split()
set_text = set(text)
print(len(set_text))
