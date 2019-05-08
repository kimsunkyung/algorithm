s= "Aa aaaaa            AAAAAA"
answer = ""
i = 0
k = 0
while k<len(s):
    if s[k] == " ":
        answer = answer + " "
        i = 0
        k+=1
    elif i%2 == 0:
        answer = answer + s[k].upper()
        i+=1
        k+=1
    else:
        answer= answer + s[k].lower()
        k+=1
        i+=1
print(answer)