# Домашнее задание по теме "Генераторы"

def all_variants(text):

    for i in range(len(text)):
        for j in range(i, len(text)):
            yield text[i:j+1]

a = all_variants("abc")
for s in a:
    print(s)