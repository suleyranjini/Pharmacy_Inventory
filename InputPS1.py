import Binary_Tree as bt
import re

#Function to Build or Update the Tree
def build_tree(inp_list):

    for i in range(len(inp_list)):
        key=inp_list[i][0]
        value=inp_list[i][1]
        #print(key,",",value)
        #print(True if root else False)
        try:
            if root:
                present=root.checkDrug(key,value)
                #print("Present",present)
                if present:
                    status=root.searchDrug(key,value)
                else:
                    #print("Node created for",key,':',value)
                    root.readDrugList(key,value)
        except:
            root=None
            if i==0:
                #print("Root created")
                root=bt.DrugNode(key,value)

    root.PrintTree()
    return root

if __name__=="__main__":
#Input 1 File Read
    inp_file=[line for line in open("inputPS1.txt")]
    print(inp_file)
    inp_list=[]
    for inp in inp_file:
        inp_tup=()
        inp=inp.strip('\n')
        #print(inp)
    
        #print('$',inp[:inp.index(',')],'$','$',inp[inp.index(',')+2:],'$')
        inp_tup = (int(inp[:inp.index(',')]),int(inp[inp.index(',')+2:]))
        inp_list.append(inp_tup)
    

    print(inp_list)
    for i in range(len(inp_list)):
        key=inp_list[i][0]
        value=inp_list[i][1]
        #print(key,",",value)
        #print(True if root else False)
        try:
            if root:
                present=root.checkDrug(key,value)
                #print("Present",present)
                if present:
                    status=root.searchDrug(key,value)
                else:
                    #print("Node created for",key,':',value)
                    root.readDrugList(key,value)
        except:
            root=None
            if i==0:
                #print("Root created")
                root=bt.DrugNode(key,value)

    root.PrintTree()

    #PromptPS File Read
    prom_file=[line for line in open("promptsPS2.txt")]
    print(prom_file)
    inp_list=[]
    for inp in prom_file:
        inp_tup=()
        if inp.startswith('updateDrugList'):
            #print(re.sub(r'(updateDrugList: )','',inp))
            inp=(re.sub(r'(updateDrugList: )','',inp)).strip('\n')
            #print(inp)
            inp_tup = (int(inp[:inp.index(',')]),int(inp[inp.index(',')+2:]))
            #inp_list=[inp_tup]
            print(inp_tup)
            #for i in inp_tup:
            key=inp_tup[0]
            value=inp_tup[1]
            print(key,",",value)
            #print(True if root else False)
            try:
                if root:
                    present=root.checkDrug(key,value)
                    print("********Present",present)
                    if present:
                        status=root.searchDrug(key,value)
                    else:
                        print("Node created for",key,':',value)
                        root.readDrugList(key,value)
            except:
                root=None
                if i==0:
                    #print("Root created")
                    root=bt.DrugNode(key,value)

            root.PrintTree()

        if inp.startswith('printDrugInventory'):
            if root:
                #root.PrintTree()
                output,total=root.printDrugInventory(root)
                fout = open("outputDrugInvent.txt","a")
                fout.write("Total number of medicines entered in the inventory: "+str(total)+"\n")
            if output:
                for data in output:
                    fout.write(data+"\n")
            fout.close()
                #oplst.append(f"{self.Uid},{self.availCount}")
        
        if inp.startswith('printStockOut'):
            if root:
                #root.PrintTree()

                output=root.printStockOut(root)
                fout = open("outputStockOut.txt","a")
                fout.write("The following medicines are out of stock:\n")
            if output:
                for data in output:
                    fout.write(data+"\n")
            fout.close()