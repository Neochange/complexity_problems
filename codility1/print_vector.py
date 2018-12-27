
n=10000
i=0
vector= "["
while i < n:
    vector+=str(i)+ ","
    i+=1

vector=vector[:-1]
vector=vector + "]"
print(vector)