----------------------------------------------------------------------------------------------------------------------------------------------------------------------

SIMPLIFY PATH

Question Link:
https://leetcode.com/problems/simplify-path/submissions/
        
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
path="/home/../"
stack=[]
        
for directory in path.split("/"):
    if directory=='':
        pass
    elif  directory==".":
        pass
    elif  directory=="..":
        if stack:
            stack.pop()
        else:
            pass
    else:
        stack.append(directory)
                
                
                
print( "/" + "/".join(stack)  )
