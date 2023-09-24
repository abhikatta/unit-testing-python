def factorise(str:str)->str:
    splits=str.split("+")
    stack=[]
    for i in range( len(splits)):
        stack.append(splits[i])
    return  stack