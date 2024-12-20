#list of names already sorted,a character input 'p',return names starting with p/character.

names=[]
first_char=''

def Return_name(names,first_char):

    newnames=[]

    for name in names:
        if name[0]==first_char:
            newnames.append(name)

    return newnames if len(newnames)>0 else 'no name found'

        
    

print(Return_name(["abc","axv","abn","io","po"],'b'))

