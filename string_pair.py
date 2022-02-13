s = input()

for x in range(0,len(s),2):
    if((x+1)<len(s)):
        if(s[x]>s[x+1]):
            print(s[x],end="")
        else:
            print(s[x+1],end="")
    else:
        print(s[x],end="")
    # print(f"\t{x/2}")
    