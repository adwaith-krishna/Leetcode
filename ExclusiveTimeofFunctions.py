class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
    	stack=[]
    	res=[0]*n
    	prev_time=0

    	for log in logs:
    		fid,type,time = log.split(":")
    		fid=int(fid)
    		time=int(time)
    		if type=="start":
    			if stack:
    				crrfunc = stack[-1]
    				timeexec=time-prev_time
    				res[crrfunc]+=timeexec
    			stack.append(fid)
    			prev_time=time
    		else:
    			finished_function = stack.pop()
    			res[finished_function] += time - prev_time + 1
    			prev_time = time + 1

				 
			
    	return res




a=Solution()

n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
print(a.exclusiveTime(n,logs))

n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print(a.exclusiveTime(n,logs))

n = 2
logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
print(a.exclusiveTime(n,logs))