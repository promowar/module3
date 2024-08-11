def single_root_words (root_ward, *other_words):
    same_words=[]
    a = root_ward.lower()
    b = [x.lower() for x in other_words]
    for i in b:
        if i.count(a) or a.count(i):
            same_words.append(i)
    return print(same_words)
single_root_words('rich','richiest', 'orichalcum', 'cheers', 'richies' )
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')