class DrugNode:
    
    def __init__(self, Uid, availCount):
        self.Uid = Uid
        self.availCount = availCount
        self.chkoutCtr=1
        self.left = None
        self.right = None
    
#     def __str__(self):
#         #InvRoot = self.Uid if self.Uid else '<>'
#         left = f'{self.left}, ' if self.left else ''
#         right = f', {self.right}' if self.right else ''
#         return f'{left} {self.Uid}:{self.availCount}, {self.right}'
#         #return f'<{InvRoot}>'
        
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(f"{self.Uid}:{self.availCount} ->{self.chkoutCtr}"),
        if self.right:
            self.right.PrintTree()
    
    #Build Tree from Input List
    def readDrugList(self,Uid,availCount):
        if Uid:
            if Uid <= self.Uid:
                if self.left == None:
                    self.left=DrugNode(Uid,availCount)
                else:
                    self.left.readDrugList(Uid,availCount)
            elif Uid > self.Uid:
                if self.right == None:
                    self.right=DrugNode(Uid,availCount)
                else:
                    self.right.readDrugList(Uid,availCount)
        else:
            self.Uid = Uid
            self.availCount = availCount
            self.chkoutCtr=1
    
    def checkDrug(self, Uid, availCount):
        print(f"CHECK Uid: {Uid},self.Uid: {self.Uid}, self.availCount: {self.availCount}, self.chkoutCtr: {self.chkoutCtr}")
        if Uid == self.Uid:
            print("*******self.Uid",self.Uid)
            return True
        elif Uid < self.Uid and self.left:
            print("In Left")# recursive case
            return self.left.checkDrug(Uid, availCount)
        elif Uid > self.Uid and self.right:
            print("In Right")# recursive case
            return self.right.checkDrug(Uid, availCount)
        else:
            return False
        
    def upd_availCount(self, Uid, availCount):
        self.chkoutCtr+=1
        print(f"Before Uid: {Uid},self.Uid: {self.Uid}, self.availCount: {self.availCount}, self.chkoutCtr: {self.chkoutCtr}")
        if self.chkoutCtr%2 == 0:
            self.availCount-=availCount
        else:
            self.availCount+=availCount
        print(f"After Uid: {Uid},self.Uid: {self.Uid}, self.availCount: {self.availCount}, self.chkoutCtr: {self.chkoutCtr}")
        return
    
    def searchDrug(self, Uid, availCount):
        if Uid == self.Uid:
            print(f"Uid: {Uid},self.Uid: {self.Uid}, self.availCount: {self.availCount}, self.chkoutCtr: {self.chkoutCtr}")
            self.upd_availCount(Uid, availCount)
            return True
        elif Uid < self.Uid and self.left:             # recursive case
            return self.left.searchDrug(Uid, availCount)
        elif Uid > self.Uid and self.right:            # recursive case
            return self.right.searchDrug(Uid, availCount)
        else:
            return False
    
    def findTotal(self,total,outlst):
        if self.left:
            outlst,total=self.left.findTotal(total,outlst)
        #print(f"{self.Uid}:{self.availCount}")
        outlst.append(f"{self.Uid},{self.availCount}")
        total+=1
        if self.right:
            outlst,total=self.right.findTotal(total,outlst)
        return outlst,total
    
    def findStockOut(self,stkoutlst):
        if self.left:
            stkoutlst=self.left.findStockOut(stkoutlst)
        #print(f"{self.Uid}:{self.availCount}")
        if self.availCount <= 0:
            stkoutlst.append(f"{self.Uid}")
        if self.right:
            stkoutlst=self.right.findStockOut(stkoutlst)
        return stkoutlst
   
    def printDrugInventory(self,Node):
        output=[]
        total=0
        output,total=self.findTotal(total,output)
        return output,total
        #print(output)
        #print(total)
        
    def printStockOut(self,Node):
        stkoutput=[]
        stkoutput=self.findStockOut(stkoutput)
        return stkoutput