def thesaurus(*names):

    names = dict()
for el in name:
    name.setdefault(el[0], [])
name [el[0]].append(el)
return name

print(thesaurus('Даниил', 'Рома', 'Марина', 'Стас', 'Дмитрий', 'Сергей', 'Семён', 'Михаил', 'Ростислав'))