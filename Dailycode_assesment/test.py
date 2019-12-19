s1=list(int(input()))
s2=list(int(input()))

re=s1-s2
res=s2-s1
result=re.union(res)
print(sorted(result))
