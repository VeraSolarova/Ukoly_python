"""
2. práce se set (množina)
vytvořte soubor 10_set.py
mám 2 sety přátel (např jako na facebooku) a chci jistit, kteří jsou společní a 
kolik je to celkem lidí

friends_set1 = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"}
friends_set2 = {"Charlie", "Eve", "Bob", "Frank", "Mallory", "Oscar", "Peggy", "Trent", "Victor", "Walter"}
udělejte printy pro kontrolu
"""

friends_set1 = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"}
friends_set2 = {"Charlie", "Eve", "Bob", "Frank", "Mallory", "Oscar", "Peggy", "Trent", "Victor", "Walter"}

common_friends = friends_set1 & friends_set2 # & - průnik
print(common_friends,"celkem splečných přátel:", len(common_friends))