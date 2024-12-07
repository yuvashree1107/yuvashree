letter=[['w','e','l','c','o','m','e'],
        ['e','l','e','p','h','a','n','t'],
        ['a','q','u','a','r','i','u','m']]
words=[['come','me','we','cow','owl'],
       ['pant','pan','hat','eat','net'],
       ['aqua','ram','rum','rim','aura','air']]
lives=3
score=0
level=0
while level<3:
    print("Level {}".format(level+1))
    print("create 3 words from the given letter")
    for c in letter[level]:
        print(c,end=' ')
    print()
    wordcount=0
    oldword=''
    word=''
    match=False
    while wordcount==0 or wordcount<3:
        match=False
        word=input("words:")
        if not(word.lower()==oldword.lower()):
            for w in words[level]:
                if word.lower()==w:
                    wordcount+=1
                    score+=1
                    match=True
                    oldword=word
                    break
                if oldword.lower()==word.lower():
                    print("Dont repeat")
                    break
        if not match:
            print('wrong guess')
            lives-=1
        if lives==0:
            print("Game over!!!")
            print("your score is {}".format(score))
    wordcount=0
    match=False
    word=''
    if lives==0:
        break
    if level==2:
        print("thanks for playing the game")
        print("your final score is {}".format(score))
        level+=1
    else:
        a=input("do you want to continue?(y/n)")
        if(a.lower()[0]=='y'):
            level+=1
        else:
            print("thanks for playing the game")
            print("your final score is {}".format(score))
            break