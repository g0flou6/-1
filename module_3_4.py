def single_root_words(root_word, *other_words):
    same_words = []
    root_lower = root_word.lower()
    for i in other_words:
        if root_lower in i.lower() or i.lower() in root_lower:
            same_words.append(i)
    return same_words

print(single_root_words('clan', 'wutangCLan', 'japanCLAN', 'clavakoka'))
print(single_root_words('Adorable', 'rABle', 'door', 'aDor'))