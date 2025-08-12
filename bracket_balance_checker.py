print ("Bracket Balancer!")
 
mix={"}":"{", "]":"[", ")":"("}
 
while True:
    n=input ("Enter Only Brackets: ")
    if not n:
        print("Please Enter an input!")
        continue
    elif any(a not in "[](){}" for a in n):
        print("Only Brackets allowed!")
        continue        
    else:
        break                       
stack=[]
for i in n:
    if i in "{[(":
        stack.append(i)
    elif i in ")]}":
        if stack and stack[-1]==mix[i]:
            stack.pop()
            
        else:
            print("The Brackets are not balanced!")
            break      
                                                      
else:
    if not stack:
         print("The Brackets are balanced!")
    else:
          print("The Brackets are not balanced!")
