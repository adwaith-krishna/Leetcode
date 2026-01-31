
class Solution(object):
    def reverseVowels(s):
    	"""
    	:type s: str
    	:rtype: str
    	"""
    	VOW={"a","e","i","o","u","A","E","I","O","U"}
    	pl=0
    	pr=len(s)-1
    	s=list(s)
    	while pl<pr:
        	if pl<pr and s[pl] not in VOW:
            	pl+=1
        	if pl<pr and s[pr] not in VOW:
            	pr-=1
        	if pl<pr:
            	s[pl],s[pr]=s[pr],s[pl]
            	pl+=1
            	pr-=1

    	return "".join(s)   