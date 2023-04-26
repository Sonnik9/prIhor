with open("proxyAm.txt", encoding="utf-8") as f2:    
    prLiAm = ''.join(f2.readlines()).split('\n')
    prLiAm = list(i.strip() for i in prLiAm)
    prLiAm = list(filter(lambda item: item != '', prLiAm))

def proxyGenerator(proxArg):
    proxiess = {       
        "https": f"http://{proxArg}"          
    }   
    return proxiess