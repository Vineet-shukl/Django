def facti(b,a,*args,**kwargs):
    print(f"{type(b)=}, {type(a)=}, {type(args)=}, {type(kwargs)=}")
    print(kwargs)
    print(args)
facti(1, 2,5,87,8,2, x=89, y="HELLO")