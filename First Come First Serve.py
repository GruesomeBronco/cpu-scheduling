import matplotlib.pyplot as plt


print("FCFS")
n= int(input("Enter number of processes: "))
d = dict()
 
for i in range(n):
    key = "P"+str(i+1)
    a = int(input("Enter arrival time of Process "+str(i+1)+": "))
    b = int(input("Enter service time of Process "+str(i+1)+": "))
    l = []
    l.append(a)
    l.append(b)
    d[key] = l
 
d = sorted(d.items(), key=lambda item: item[1][0])
 
FT = []
for i in range(len(d)):
    # first process
    if(i==0):
        FT.append(d[i][1][1])
 
    # gFt prevFT + newBT
    else:
        FT.append(FT[i-1] + d[i][1][1])
 
TAT = []
for i in range(len(d)):
    TAT.append(FT[i] - d[i][1][0])

print("Process | Arrival | Service | Exit | Turn Around | ")
for i in range(n):
      print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",FT[i],"  |    ",TAT[i],"  |  ")

print(FT)


for i in range(len(d)):
    #print(d[i][1][0]) if i == 0 else print(FT[i-1])
    #print(d[i][1][1]) if i == 0 else print(FT[i-1] + d[i][1][1])
    plt.barh(y=d[i][0], left=d[i][1][0] if i == 0 else FT[i-1], width=d[i][1][1])
plt.show()


# d[i][0] = process ID
# d[i][1][0] = process arrival time
# d[i][1][1] = process service time
# FT[i] = Exit Time of process[i]
# TAT[i] = Turnaround Time
# d[i][1][0] if i == 0 else FT[i-1]
# d[i][1][1] if i == 0 else FT[i-1] + d[i][1][1]