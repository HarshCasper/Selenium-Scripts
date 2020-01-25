# Python Prigram to check whether two strings are anagrams or not
n=int(input())
for i in range(0,n):
    x=input()
    y=input()
    if(sorted(x)==sorted(y)):
        print("They are Anagrams")
    else:
        print("They are not Anagrams")
