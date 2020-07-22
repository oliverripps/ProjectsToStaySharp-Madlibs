
def getstuffs(na,no,v,a,nu):
    dic={
        "Names":[],
        "Nouns":[],
        "Verbs":[],
        "Adverb":[],
        "Numbers":[]
        }
    for i in range(na):
        temp=input("Enter a Name")
        dic["Names"].append(temp)
    for i in range(no):
        dic["Nouns"].append(input("Enter a Noun"))
    for i in range(v):
        dic["Verbs"].append(input("Enter a Verb"))
    return dic

def main():
    madlibnum=input("Which madlib would you like to do? madlib.txt or madlib2.txt. ")
    file1 = open(madlibnum,"r")
    madlib=file1.read()
    madlibwords=madlib.split()
    Name=0
    Noun=0
    Verb=0
    Adverb=0
    Numbers=0
    for i in madlibwords:
        if(i=="Name"):
            Name+=1
        if(i=="Noun."):
            Noun+=1
        if(i=="Verb"):
            Verb+=1
    replace = getstuffs(Name,Noun,Verb,Adverb,Numbers)
    madlibsfinal=[]
    for i in madlibwords:
        if(i=="Name"):
            currlist=replace.get("Names")
            curr=currlist[0]
            del currlist[0]
            madlibsfinal.append(curr)
        elif(i=="Noun."):
            currlist=replace.get("Nouns")
            curr=currlist[0]
            del currlist[0]
            madlibsfinal.append(curr)
        elif(i=="Verb"):
            currlist=replace.get("Verbs")
            curr=currlist[0]
            del currlist[0]
            madlibsfinal.append(curr)
        else:
            madlibsfinal.append(i)

    script=""
    for i in madlibsfinal:
        script+=i
        script+=" "
    print(script)
            
            
if __name__ == '__main__':
    main()
