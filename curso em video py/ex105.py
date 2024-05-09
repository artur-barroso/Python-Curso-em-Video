def notas(*n,sit=False):
    """
    ->Analisando notas de alunos,
    se vira ai que eu fiquei com preguiça
    """
    r={}
    r['total']=len(n)
    r['maior']=max(n)
    r['menor']=min(n)
    r['media']=sum(n)/len(n)
    if sit:
        if r['media']>=7:
            r['situação']='BOA'    
        elif r['media'] >= 5:
             r['situação']= 'RAZOAVEL'  
        else:
            r['situação']='RUIM' 
    return r

resp = notas(5.5,2.5,1.5,sit=True)
print(resp)
