def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    word=s.split()
    string = " ".join(word)
    fword=string.split()
    pl=0
    pr=len(fword)-1
    res=[]

    while pl<=pr:
        res.append(fword[pr])
        pr-=1

    return " ".join(res)
   

str1 = "the sky is blue"
print(reverseWords(str1))

str1 = "  hello world  "
print(reverseWords(str1))

str1 = "a good   example"
print(reverseWords(str1))