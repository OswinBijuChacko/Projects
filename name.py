import random
consonants=['b','d','f','g','h','j','k','l','m','n','p','r','s','t','v','z']
vowels=['a','e','i','o','u']
def randname():
    name_list=[]
    name1=consonants[random.randint(0,15)]+'o'+consonants[random.randint(0,15)]+'i'+consonants[random.randint(0,15)]+'a'
    name2=consonants[random.randint(0,15)]+'o'+consonants[random.randint(0,15)]+'u'
    name3=consonants[random.randint(0,15)]+'i'+consonants[random.randint(0,15)]+'a'
    name4=consonants[random.randint(0,15)]+'a'+consonants[random.randint(0,15)]+'i'
    name5=consonants[random.randint(0,15)]+'i'+consonants[random.randint(0,15)]+'u'
    name6=consonants[random.randint(0,15)]+'e'+consonants[random.randint(0,15)]+'a'
    name_list.append(name1)
    name_list.append(name2)
    name_list.append(name3)
    name_list.append(name4)
    name_list.append(name5)
    name_list.append(name6)
    return name_list[random.randint(0,5)]
def trueorfalse():
    tf=random.randint(0,1)
    result=False
    if tf == 0:
        result =False
    if tf == 1:
        result = True
    return result
def realname():
     name_list=['Oswin','Riya','Rakesh','Danny',"Daniel",'Roshan','Aditi','Amber','Tim',"Josh",'Lokesh','Rahul','Maddison']
print(randname())
            
            
