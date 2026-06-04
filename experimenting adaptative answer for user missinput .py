txt1="Failure" 
txt2="Again failure"
txt3="Try again?"
p=print
mistake=0
while True:
    name=input("NAME: ")
    if name.isalpha():
        break
    else:
        mistake=mistake+1
        p(f"you failed this much times: {mistake}")
        if mistake==1: p(txt1)
        if mistake==2: p(txt2)
        if mistake==3: p(txt3)
