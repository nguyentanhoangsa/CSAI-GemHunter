import copy

def DPLL(originalCNF, listPuzzle):

    cnf = copy.deepcopy(originalCNF)
    #1
    indexUnitClause=unitClause(cnf)
    while indexUnitClause!=-1:
        l=cnf[indexUnitClause][0]
        if l <0:
            listPuzzle[(-l)-1]="G"
        else :
            listPuzzle[l-1]="T"
        unitPropagate(l,cnf)
        indexUnitClause=unitClause(cnf)
    #2
    pureVariable=findPureVariable(cnf)
    while pureVariable!=-1:
        if pureVariable <0:
            listPuzzle[(-pureVariable)-1]="G"
        else :
            listPuzzle[pureVariable-1]="T"
        pureLiteralAssign(pureVariable,cnf)
        pureVariable=findPureVariable(cnf)
    
    if len(cnf)==0:
        return True,listPuzzle
    
    if [] in cnf:
        return False,None
    
    l=cnf[0][0]
    cnfNew = copy.deepcopy(cnf)
    cnfNew.append([l])
    listNewPuzzle=copy.deepcopy(listPuzzle)
    isSuccessfulSolver, newListPuzzle=DPLL(cnfNew,listNewPuzzle)
    if isSuccessfulSolver:
        return isSuccessfulSolver,newListPuzzle

    cnfNew1 = copy.deepcopy(cnf)
    cnfNew1.append([-l])
    listNewPuzzle1=copy.deepcopy(listPuzzle)
    isSuccessfulSolver1, newListPuzzle1=DPLL(cnfNew1,listNewPuzzle1)
    return isSuccessfulSolver1,newListPuzzle1


#-------------------------------   
#Duyệt tất cả tìm phần tử là mệnh đề đơn chứ k lm riêng dò từng phần tử được
#vì nếu là [[a,c],[b,d],[-c]] nó sẽ bỏ qua 0,1 dò tới 2 là [-c] nó sẽ bỏ c ra khỏi [a,c] để còn [[a],[b,d]] mà h nó hết vòng lặp rồi thì sao
#do đó nó sẽ bỏ qua phần tử đơn trong cnf do đó ta sẽ dò lại từ đầu luôn cho chắc
def unitClause(cnf):
    for i in range(len(cnf)):
        if  len(cnf[i])==1:
            return i
    return -1
def unitPropagate(l,cnf):
    i=0
    while i < len(cnf):
        #xóa các clause chứa biến l vì nó đã đúng sẵn rồi
        if l in cnf[i]:
            cnf.pop(i) 
            continue # chỗ này cần i-1 rồi i+1 nhưng như vậy là hòa rồi nên k cần

        #xóa các biến -l trong các mệnh đề đó vì l đúng thì -l sai nó k có ý nghĩa trong các mệnh đề khác
        if (-l) in cnf[i]:
            cnf[i].remove(-l)
        i+=1
#----------------------------------
def findPureVariable(cnf):
    newCNF = []
    #chuyển về mảng đơn gồm các phần tử
    for sublist in cnf:
        newCNF.extend(sublist)
    #tìm phần tử thuần túy trong danh sách
    for i in newCNF:
        if (-i) not in newCNF:
            return i
    return -1

def pureLiteralAssign(pureVariable,cnf):
    #làm như này là sai, chạy thử rồi biết
    # pureVariable=1
    # cnf=[[1,2,3],[-1,1,3,4],[2,3,-4,-1],[3,4],[1]]
    # for item in cnf:
    #     if pureVariable in item:
    #         cnf.remove(item)
    i=0
    while i<len(cnf):
        if pureVariable in cnf[i]:
            cnf.pop(i)

            i-=1
        i+=1
    
def main():
    cnf=[[2, 4, 5], [-2, 4, 5], [-4, 2, 5], [-5, 2, 4], [-2, -4, 5], [-2, -5, 4], [-4, -5, 2], [2, 5], [-2, 5], [-5, 2], [2, 5], [-2, 5], [-5, 2], [4, 5, 7],
          [-4, 5, 7], [-5, 4, 7], [-7, 4, 5], [-4, -5, 7], [-4, -7, 5], [-5, -7, 4], [5]]
    puzzle=[
        [3,"_",2],
        ["_","_",2],
        ["_",3,1],
    ]
    listPuzzle=[]
    for item in puzzle:
        for i in item:
            listPuzzle.append(i)
    a,b=DPLL(cnf,listPuzzle)
    res=[]
    row=[]
    for i in range(len(b)):
        row.append(i)
        if len(row)==len(puzzle[0]):
            res.append(row)
            row=[]
       
    if a:
        print("Dung")
        print(b)
    else:
        print("Sai")
main()


