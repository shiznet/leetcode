class TokenBeans(object):
    uidMap={}
    def __init__(   self,
                    ut=None,
                    product=None,
                    ver=None,
                    **keyMap
                ):
        self.ut=ut
        self.product=product
        self.ver=ver
        for a in keyMap:
            if "ut" == a:
                self.ut = keyMap["ut"]
            elif "product" == a:
                self.product = keyMap["product"]
            elif "ver" ==a:
                self.ver = keyMap["ver"]
            else:
                self.uidMap[a]=keyMap[a]

    def toString(self):
        print 'TB:ut={},product={},ver={},emails={}'.format(
            self.ut,self.product,self.ver,self.uidMap)
    
    def toMap(self):
        tokenMap={}
        tokenMap["ut"]=self.ut
        tokenMap["product"]=self.product
        tokenMap["ver"]=self.ver
        tokenMap["uids"]=self.uidMap
        #print tokenMap["ut"]
        return tokenMap
