# Вариант 19. На трех участках выращиваются следующие сельскохозяйственные культуры: картофель, лук, морковь, горох,
# капуста, редис. Определить, какие из этих культур имеются на каждом участке, имеются хотя бы на одном из участков,
# и не имеются ни на одном участке.

cltres = {
    "участок1": ["картофель", "редис", "горох"],
    "участок2": ["морковь", "картофель", "редис"],
    "участок3": ["картофель", "капуста"]
}
uch1 = set(cltres["участок1"])
uch2 = set(cltres["участок2"])
uch3 = set(cltres["участок3"])

# пересечение
alluch = uch1.intersection(uch2, uch3)
if alluch == set():
    alluch = ('нет таковых')

# все элементы каждого списка
oneall = uch1.union(uch2, uch3)
if oneall == set():
    oneall = 'нет таковых'

noall = set(["картофель", "лук", "морковь", "горох", "капуста", "редис"]) - oneall
if noall == set():
    noall = ('нет таковых')

print("Культуры, которые есть на каждом участке:", *alluch)
print("Культуры, которые есть хотя бы на одном участке:", *oneall)
print("Культуры, которые не выращиваются ни на одном участке:", *noall)
