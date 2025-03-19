def op(li,operator,func):
    k=0
    while k<len(li):
        if li[k]==operator:
            li[k]=func(k)
            del li[k+1]
            del li[k-1]
            k=k-1
        k+=1
        if operator not in li:
            k=len(li)
    return li

def strform(q):

    paren=[]
    form=[]

    i=0
    while True:
        if "(" in q or ")" in q:
            while True:
                if q[i]=="(":
                    paren.append(i)
                elif q[i]==")":
                    in_paren=q[paren[-1]:i+1].lstrip("(").rstrip(")")
                    break
                i+=1
        else:
            in_paren=q
            paren=[0]
            i=len(q)-1
        
        j_=0
        start=0
        tRf=False
        if in_paren[0]=='-':
            start=1
        
        for j in range(start,len(in_paren)):
            if in_paren[j].isdecimal()==tRf:
                form.append(in_paren[j_:j])
                if tRf==True:
                    tRf=False
                else:
                    tRf=True
                j_=j
                if j_==len(in_paren)-1:
                    form.append(in_paren[j_:])
        while len(form)!=1:
            if "**" in form:
                op(form,"**",lambda x: int(form[x-1])**int(form[x+1]))
    
            if "*" in form:
                op(form,"*",lambda x: int(form[x-1])*int(form[x+1]))
            elif "/" in form:
                op(form,"/",lambda x: int(form[x-1])/int(form[x+1]))
            elif "//" in form:
                op(form,"//",lambda x: int(form[x-1])//int(form[x+1]))
            elif "%" in form:
                op(form,"%",lambda x: int(form[x-1])%int(form[x+1]))
    
            if "+" in form:
                op(form,"+",lambda x: int(form[x-1])+int(form[x+1]))
            elif "-" in form:
                op(form,"-",lambda x: int(form[x-1])-int(form[x+1]))
    
        q=q.replace(q[paren[-1]:i+1],str(form[0]),1)
        i=paren[-1]+1
        form=[]
        del paren[-1]
    
        if q.isdecimal()==True:
            break
        
    return q