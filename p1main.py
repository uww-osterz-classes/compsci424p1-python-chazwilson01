"""
COMPSCI 424 Program 1
Name: Charlie Wilson
"""
import time
class PCB:
    def __init__(self, pid):
        self.pid = pid
        self.parent = None
        self.child = []

    def getPid(self):
        return self.pid
    def getParent(self):
        return self.parent
    def getChild(self):
        return self.child
    def getFirstChild(self):
        return self.child.pop(0)
    
    
    def setParent(self, new):
        self.parent = new
    
    def addChild(self, new):
        self.child.append(new)
    
    def removeChild(self, index):
        self.child.pop(index)
        
class ProcessManagerV1:
    def __init__(self):
        self.pcbs = []
    
    def create(self, p_pid):
        
        if len(self.pcbs) == 0:
            new_pid = 0
            first_pcb = PCB(new_pid)
            self.pcbs.append(first_pcb)
            return
            
            
        elif p_pid >= len(self.pcbs) or self.pcbs[p_pid] is None:
            return
        
        new_pid = len(self.pcbs)
        new_pcb = PCB(new_pid)
        self.pcbs.append(new_pcb)

        parent_pcb = self.pcbs[p_pid]
        
        parent_pcb.addChild(new_pcb)
        

        new_pcb.setParent(parent_pcb)
        

    def destroy(self, p_pid):
        if p_pid >= len(self.pcbs) or self.pcbs[p_pid] is None:
            return       
        
        
        pcb = self.pcbs[p_pid]
        
        
        parent = pcb.getParent()
        
        if parent is not None:
            
            parent.getChild().remove(pcb)
            

        self.recursive_destroy(pcb)
    
    def recursive_destroy(self, pcb):
        if pcb is None:
            return
        
       
        
        while len(pcb.getChild()) != 0:
#             print(i.getPid())
            i = pcb.getFirstChild()
            self.recursive_destroy(i)
            
    
    
#         parent = pcb.getParent()
        
        self.pcbs.remove(pcb)


#         if parent is not None:
#             print(pcb.getPid())
#             print( parent.getChild())
#             parent.getChild().remove(pcb)
#             print( parent.getChild())

#         print(self.pcbs[2].getParent())
#         parent = pcb.getParent()
#         if parent is not None:
#             print("Entered", pcb.getPid())
#             for index, pcb_c in enumerate(parent.getChild()):
#                 if pcb_c.getPid() == pcb.getPid():
#                     parent.removeChild(index)  
        



        
    
            
            
    def showProcessInfo(self):
            if len(self.pcbs) == 0:
                print("No current PCBs")
            for pid in range(0, len(self.pcbs)):
                pcb = self.pcbs[pid]
                if pcb:
                    if pcb.getParent():
                        parent_pid = pcb.getParent().getPid()
                    else:
                        parent_pid = -1
                        

                    if len(pcb.getChild()) == 0:
                        print(f'Process {pcb.getPid()}: parent is {parent_pid} and has no children')
                    else:
                        print(f'Process {pcb.getPid()}: parent is {parent_pid} and children are ', end='')
                        self.get_children(pcb, 0)

    def get_children(self, pcb, index):
        
        if index < len(pcb.getChild())-1:
            print(f'{pcb.getChild()[index].getPid()} ', end='')
            self.get_children(pcb, index+1)
            
        elif index == len(pcb.getChild())-1:
            print(pcb.getChild()[index].getPid())


            
        

        
class PCB2:
    def __init__(self, pid):
        self.pid = pid
        self.parent = None
        self.first_child = None
        self.younger_sibling = None
        self.older_sibling = None
        
    def getParent(self):
        return self.parent
    
    def getFirstChild(self):
        return self.first_child
    
    def getYoungerSibling(self):
        return self.younger_sibling
    
    def getOlderSibling(self):
        return self.older_sibling
    
    def getPid(self):
        return self.pid
    
    def setParent(self, new):
        self.parent = new
    def setFirstChild(self, new):
        self.first_child = new
    def setYoungerSibling(self, new):
        self.younger_sibling = new
    def setOlderSibling(self, new):
        self.older_sibling = new
        
class ProcessManagerV2:
    def __init__(self):
        self.pcbs = []
    
    def create(self, p_pid):
        if len(self.pcbs) == 0:
            new_pid = 0
            first_pcb = PCB2(new_pid)
            self.pcbs.append(first_pcb)
            return
        
        if p_pid >= len(self.pcbs) or self.pcbs[p_pid] is None:
            return
        
        new_pid = len(self.pcbs)
        new_pcb = PCB2(new_pid)
        self.pcbs.append(new_pcb)
        parent_pcb = self.pcbs[p_pid]
        
        new_pcb.setParent(parent_pcb)
        
        if parent_pcb.getFirstChild() == None:
            parent_pcb.setFirstChild(new_pcb)
            
        else:
            child = parent_pcb.getFirstChild()
            while child.getYoungerSibling() is not None:
                child = child.getYoungerSibling()
                
            child.setYoungerSibling(new_pcb)
            new_pcb.setOlderSibling(child)
            
    def destroy(self, targetPid):
        if targetPid >= len(self.pcbs) or self.pcbs[targetPid] is None:
                return
        
        pcb = self.pcbs[targetPid]
        
        
        if pcb.getParent() is not None:

            if pcb.getOlderSibling() is None:

                p = pcb.getParent()

                if pcb.getYoungerSibling is not None:



                    ys = pcb.getYoungerSibling()

                    p.setFirstChild(ys)

                else:

                    p.setFirstChild(None)


            else:

                os = pcb.getOlderSibling()

                if pcb.getYoungerSibling() is not None:

                    ys = pcb.getYoungerSibling()

                    ys.setOlderSibling(os)
                    os.setYoungerSibling(ys)

                else:

                    os.setYoungerSibling(None)

        if pcb.getFirstChild() is None:

            self.pcbs.remove(pcb)
            return
        
        child = pcb.getFirstChild()
        self.recursivlyDestroy(targetPid, child)
        self.pcbs.remove(pcb)
        
        
        
    def recursivlyDestroy(self, targetPid, pcb):
        
        child = pcb.getFirstChild()
        if child is not None:

            self.recursivlyDestroy(targetPid, child)
        
        if pcb.getYoungerSibling() is not None:
                
            self.recursivlyDestroy(targetPid, pcb.getYoungerSibling())
        
        self.pcbs.remove(pcb)
    
    def showProcessInfo(self):
        
        if len(self.pcbs) == 0:
            print("No current PCBs")
        
        for pid, pcb in enumerate(self.pcbs):
            
            if pcb:
                if pcb.parent:
                    parent_pid = pcb.getParent().getPid()
                else:
                    parent_pid = -1
                    
                if pcb.getFirstChild() is None:
                    print(f'Process {pcb.getPid()}: parent is {parent_pid} and has no children')
                
                else:
                    print(f'Process {pcb.getPid()}: parent is {parent_pid} and children are ', end='')
                    children = self.get_children(pcb.getFirstChild())
                    

    def get_children(self, child):
        
        
        if child.getYoungerSibling() is not None:
            print(f'{child.getPid()} ', end='')

            self.get_children(child.getYoungerSibling())
            
        else: 
            print(child.getPid())


            
    
def CmdSq(PM, seq):
    for i in range(0, len(seq)):
        N = seq[i][1]
        
        if seq[i][0].upper() == "CREATE":
            PM.create(N)
            # PM.showProcessInfo()
            # print()
            # print()

        elif seq[i][0].upper() == "DESTROY":
            PM.destroy(N)
            # PM.showProcessInfo()
            # print()
            # print()
    PM.showProcessInfo()
def timer1(seq):

    
    startTime1 = time.process_time_ns()

    for n in range(0,200):
        pm1 = ProcessManagerV1()

        for i in range(0, len(seq)):
            N = seq[i][1]

            if seq[i][0].upper() == "CREATE":
                pm1.create(N)

            elif seq[i][0].upper() == "DESTROY":
                pm1.destroy(N)
            
    endTime1 = time.process_time_ns()
    finalTime1 = endTime1 - startTime1
    
    print(f'Version 1 running time: {finalTime1}')
    
def timer2(seq):
    
    
    startTime1 = time.process_time_ns()

    for n in range(0,200):
        pm1 = ProcessManagerV2()

        for i in range(0, len(seq)):
            N = seq[i][1]

            if seq[i][0].upper() == "CREATE":
                pm1.create(N)

            elif seq[i][0].upper() == "DESTROY":
                pm1.destroy(N)
            
    endTime1 = time.process_time_ns()
    finalTime1 = endTime1 - startTime1
    
    print(f'Version 2 running time: {finalTime1}')
    
if __name__ == "__main__":

    stop = False
    cmd_lst = []

    while stop == False:
        cmd = input()
        cmd = cmd.split()
        
        if cmd[0].upper() not in ["CREATE", "DESTROY"]:
            break
        try:
            N = int(cmd[1])
            if N < 0 or N > 15:
                print("Int outside accpeted range entered")
                continue
        except:
            
            print("Valid int not entered")
            continue
        
        command = cmd[0]
        
        cmd_lst.append((cmd[0], N))
    
    
   
    
    
    pm1 = ProcessManagerV1()
    pm2 = ProcessManagerV2()
    
    CmdSq(pm1, cmd_lst)
    CmdSq(pm2, cmd_lst)
    
           

    timer1(cmd_lst)
    timer2(cmd_lst)
    
        


# There are many correct ways to solve this in Python, so I'm giving
# you minimal guidance for your Python code. Any correct solution is
# allowed.

