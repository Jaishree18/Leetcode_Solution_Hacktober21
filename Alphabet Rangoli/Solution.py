def print_rangoli(size):
    main_lst=[]
    for i in range(1,size+1):
        a = size
        temp = []
        while(i+a>=size+1):
            temp.append(chr(96+a))
            #print(temp)
            a-=1
        main_lst.append(temp)
    for elem in range(len(main_lst)-1,0,-1):
        previousobj=list(reversed(main_lst[elem-1]))
        main_lst[elem].extend(previousobj)
    totallen=size*2-1+(size-1)*2
    for elem in range(0,len(main_lst)):
        if elem==0:
            main_lst[elem]="".join(main_lst[elem])
        else:
            main_lst[elem]="-".join(main_lst[elem])
    for i in range(size):
        print("-"*((totallen-len(main_lst[i]))//2),main_lst[i],"-"*((totallen-len(main_lst[i]))//2),sep="")
    for i in range(size-2,-1,-1):
        print("-" * ((totallen - len(main_lst[i])) // 2), main_lst[i], "-" * ((totallen - len(main_lst[i])) // 2), sep="")


