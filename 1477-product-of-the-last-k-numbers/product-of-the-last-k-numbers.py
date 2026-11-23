class ProductOfNumbers:

    def __init__(self):
        self.ls=[]
        

    def add(self, num: int) -> None:
        
        self.ls.append(num)
        

    def getProduct(self, k: int) -> int:
        res=1
        for n in self.ls[-k:]:
            res*=n
        return res
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)