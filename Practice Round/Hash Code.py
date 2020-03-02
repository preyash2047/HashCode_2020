file_name = input("Enter File Name in Required Formate")
dataset = open(file_name,'r')
data = dataset.readlines()
dataset.close()

data_line = []
for i in data:
    data_line.append(str(i).split())

maximum_slice = int(data_line[0][0])
types_of_pizza = int(data_line[0][1])
no_of_slices_in_pizza = data_line[1]

#!pip install itertools 
from itertools import permutations 
slices_permutation = list(permutations(no_of_slices_in_pizza))

def SliceToOrder(x):
    SUM = 0
    FinalList = []
    for i in x:
        SUM = SUM + int(i)
        FinalList.append(int(i))
        if SUM == maximum_slice:
            return SUM, FinalList
        elif SUM > maximum_slice:
            FinalList.remove(int(i))
            return (SUM - int(i)),FinalList

MaxSliceToOrder = 0
FinalSliceList = [] 
for i in slices_permutation:
    tempSUM, tempSliceList = SliceToOrder(i)
    if tempSUM >= MaxSliceToOrder:
        MaxSliceToOrder = tempSUM
        FinalSliceList = tempSliceList
FinalSliceList.sort()

PrintTypesOfPizza = len(FinalSliceList)
PrintIndexOfPizza = ""
for i in FinalSliceList:
    PrintIndexOfPizza = PrintIndexOfPizza + str(no_of_slices_in_pizza.index(str(i))) + " "

new_fileName = file_name + " Answer.in"
WriteFile = open(new_fileName,'w')
WriteFile.write(f"{PrintTypesOfPizza}\n{PrintIndexOfPizza}")
WriteFile.close()