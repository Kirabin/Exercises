# Solution from StackOverflow

def convert(numerator, denominator):
    ans= str(numerator//denominator)+ "."
    l={}
    index=0
    numerator = numerator%denominator
    l[numerator]=index
    t=False
    while t==False:
        if numerator==0:
            break
        digit = numerator*10//denominator
        numerator=numerator*10-(numerator*10//denominator)*denominator
        if numerator not in l:
            ans+=str(digit) 
            index+=1
            l[numerator]=index
            t=False
        else:
            ans+=str(digit)+")"
            ans=ans[:l.get(numerator)+len(ans[:ans.index(".")+1])]+"("+ ans[l.get(numerator)+len(ans[:ans.index(".")+1]):]
            t=True
    return ans

print(convert(3, 14))