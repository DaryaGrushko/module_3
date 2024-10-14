# Самостоятельная работа по уроку "Произвольное число параметров"

def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in other_words:
        i = i.lower()
        if i.find(root_word) != -1:
            same_words.append(i)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Able', 'Disablement', 'Mable', 'Disable', 'Bagel'))
