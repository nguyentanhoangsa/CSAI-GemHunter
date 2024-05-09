import copy
from createCNF import *
def DPLL(originalCNFs, listPuzzle):

    cnfs = copy.deepcopy(originalCNFs)
    #1
    indexUnitClause=unitClause(cnfs)
    while indexUnitClause!=-1:
        l=cnfs[indexUnitClause][0]
        if l <0:
            listPuzzle[(-l)-1]="G"
        else :
            listPuzzle[l-1]="T"
        unitPropagate(l,cnfs)
        indexUnitClause=unitClause(cnfs)
    #2
    pureVariable=findPureVariable(cnfs)
    while pureVariable!=-1:
        if pureVariable <0:
            listPuzzle[(-pureVariable)-1]="G"
        else :
            listPuzzle[pureVariable-1]="T"
        pureLiteralAssign(pureVariable,cnfs)
        pureVariable=findPureVariable(cnfs)
    
    if len(cnfs)==0:
        return True,listPuzzle
    
    if [] in cnfs:
        return False,None
    
    l=cnfs[0][0]
    cnfNew = copy.deepcopy(cnfs)
    cnfNew.append([l])
    listNewPuzzle=copy.deepcopy(listPuzzle)
    isSuccessfulSolver, newListPuzzle=DPLL(cnfNew,listNewPuzzle)
    if isSuccessfulSolver:
        return isSuccessfulSolver,newListPuzzle

    cnfNew1 = copy.deepcopy(cnfs)
    cnfNew1.append([-l])
    listNewPuzzle1=copy.deepcopy(listPuzzle)
    isSuccessfulSolver1, newListPuzzle1=DPLL(cnfNew1,listNewPuzzle1)
    return isSuccessfulSolver1,newListPuzzle1


#-------------------------------   
#Duyệt tất cả tìm phần tử là mệnh đề đơn chứ k lm riêng dò từng phần tử được
#vì nếu là [[a,c],[b,d],[-c]] nó sẽ bỏ qua 0,1 dò tới 2 là [-c] nó sẽ bỏ c ra khỏi [a,c] để còn [[a],[b,d]] mà h nó hết vòng lặp rồi thì sao
#do đó nó sẽ bỏ qua phần tử đơn trong cnf do đó ta sẽ dò lại từ đầu luôn cho chắc
def unitClause(cnfs):
    for i in range(len(cnfs)):
        if  len(cnfs[i])==1:
            return i
    return -1
def unitPropagate(l,cnfs):
    i=0
    while i < len(cnfs):
        #xóa các clause chứa biến l vì nó đã đúng sẵn rồi
        if l in cnfs[i]:
            cnfs.pop(i) 
            continue

        #xóa các biến -l trong các mệnh đề đó vì l đúng 
        #thì -l sai nó k có ý nghĩa trong các mệnh đề khác
        if (-l) in cnfs[i]:
            cnfs[i].remove(-l)
        i+=1
#----------------------------------
def findPureVariable(cnfs):
    newCNF = []
    #chuyển về mảng đơn gồm các phần tử
    for sublist in cnfs:
        newCNF.extend(sublist)
    #tìm phần tử thuần túy trong danh sách
    for i in newCNF:
        if (-i) not in newCNF:
            return i
    return -1

def pureLiteralAssign(pureVariable,cnfs):
    #làm như này là sai
    # pureVariable=1
    # cnf=[[1,2,3],[-1,1,3,4],[2,3,-4,-1],[3,4],[1]]
    # for item in cnf:
    #     if pureVariable in item:
    #         cnf.remove(item)
    i=0
    while i<len(cnfs):
        if pureVariable in cnfs[i]:
            cnfs.pop(i)
            i-=1
        i+=1
    
def doDPLL(puzzle_origin):
    # print("-----")
    # print(puzzle_origin)
    #chuyển thành số nếu phần tử trong mảng 2 chiều là số
    puzzle=list(map(lambda row: [int(i) if i.isdigit() else i for i in row], puzzle_origin))
    cnfs=createCNFs(puzzle)
    listPuzzle=[]
    for item in puzzle:
        for i in item:
            listPuzzle.append(i)
    check,listNewPuzzle=DPLL(cnfs,listPuzzle)
    result=[]
    #Nếu đúng thì chuyển sang mảng hai chiều
    if(check):
        row=[]
        for i in range(len(listNewPuzzle)):
            row.append(listNewPuzzle[i])
            if len(row)==len(puzzle[0]):
                result.append(row)
                row=[]
        return check,result
    
    return check,None


