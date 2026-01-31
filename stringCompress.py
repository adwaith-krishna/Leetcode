def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    res={}
    fres=[]
    #res.append(chars[0])
    for char in chars:
        if char in res:
            res[char]+=1
        else:
            res[char]=1



    for key,value in res.items():
        fres.append(key)
        fres.append(str(value))




    return len(fres)

# def compressTwo(chars):
#     pl=0
#     leng=len(chars)
#     pr=0
#     if chars is None:
#         return chars
#     while pr<leng:
#         curchar=chars[pr]
#         count=0
#         while pr<leng and curchar==chars[pr]:
#             pr+=1
#             count+=1
#         chars[pl]=curchar
#         pl+=1
#         if count>1:
#             for char in str(count):
#                 chars[pl]=char
#                 pl+=1

#     return chars[:pl]



chars = ["a","a","b","b","c","c","c"]
print(compress(chars))

chars = ["a"]
print(compress(chars))

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars))



# chars = ["a","a","b","b","c","c","c"]
# print(compressTwo(chars))

# chars = ["a"]
# print(compressTwo(chars))

# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# print(compressTwo(chars))