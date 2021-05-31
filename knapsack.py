def fractional_Knapsack(mass,n,profit,weight):
    sorted=[]
    for i in range(n):
        sorted.append((profit[i]/weight[i],(weight[i],profit[i])))
    sorted.sort()
    total_profit=0
    i=n-1
    
    while(mass>0 and i>=0 ):
        print(i, mass,total_profit,sorted[i][1][1],sorted[i][1][0] )
        if mass >=sorted[i][1][0]:
            total_profit+= sorted[i][1][1]
            mass-=sorted[i][1][0]
        else:
            total_profit+= (mass/sorted[i][1][0])*sorted[i][1][1]
        i-=1
    print(total_profit)

def Zero_One_Knapsack(mass,n,profit,weight):
    sorted=[]
    for i in range(n):
        sorted.append(((weight[i],profit[i])))
    sorted.sort()
    # print(sorted)
    knapsackTable=[[0 for i in range(mass+1)] for i in range(n+1)]
    for i in range(len(knapsackTable)):
        for j in range(len(knapsackTable[0])):
            if i!=0 and j!=0:
                if j < sorted[i-1][0]:
                    knapsackTable[i][j]=knapsackTable[i-1][j]
                else:
                    knapsackTable[i][j]=max(knapsackTable[i-1][j], sorted[i-1][1]+ knapsackTable[i-1][j-sorted[i-1][0]])
            
    # for i in knapsackTable:
    #     print(i)
    print(knapsackTable[-1][-1])


M=50
n=3
profit=[60,100,120]
weight=[10,20,30]
# fractional_Knapsack(M,n,profit,weight)


Zero_One_Knapsack(M,n,profit,weight)
# arr[] = {{60, 10}, {100, 20}, {120, 30}} 