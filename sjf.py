#SJF
import csv

print("SJF\n\nBefore Schedule/Given Processes")
print("------------------------------")
print("Process ID\t\t\tBurst Time")
print("------------------------------")

with open('processes.csv') as file:
  reader = csv.reader(file)

  processes1 = [] #list of processes used to sort 
  processes2 = [] #list of processes used to compare difference in index
  idNum = []      #list of pid's that correlates with burst time
  turnarr = []    #list of turn around times
  waitarr = []    #list of wait times

  #Before Schedule - prints out given
  count = 0
  for row in reader:
    if count != 0:
      id = "P" + row[0]
      burst = int(row[1])
      processes1.append(burst)
      processes2.append(burst)
      idNum.append(id)
      
      if count == 1:
        turnaround = burst
        wait = 0

      else:
        turnaround += burst
        wait = turnaround - burst

      print("\t",id,"\t\t",burst)
      
  
    if count >= 6:
      break
    count += 1

  print("\nAfter Schedule")
  print("-----------------------------------------------------------------------------")
  print("Process ID\t\tBurst Time\t\t\t\tTurnaround Time\t\t\t\tWait Time")
  print("-----------------------------------------------------------------------------") 

  #Scheduling of processes
  for i in range(len(processes1)):
    for j in range(i+1, len(processes1)):
      if processes1[i] > processes1[j]:
        processes1[i],processes1[j] = processes1[j],processes1[i]

  #Printing of processes in correct schedule
  #Also adds turnaround and wait times
  for i in range(len(processes1)):
    turnNum = 0
    waitNum = 0

    if processes1[i] in processes2:
      ind = int(processes2.index(processes1[i]))
      
      if i == 0:
        turnNum = processes1[i]
        turnarr.append(turnNum)

        waitNum = 0
        waitarr.append(waitNum)
      else:
        turnNum = processes1[i] + processes1[i-1]
        turnarr.append(turnNum)
        
        waitNum += turnarr[i-1]
        waitarr.append(waitNum)
      
      print("\t", idNum[ind], "\t\t", processes1[i], "\t\t\t", turnarr[i], "\t\t\t\t", waitarr[i])

  avgturn = sum(turnarr)/count
  avgwait = sum(waitarr)/count
  
  print("\nAverage Turnaround Time:", avgturn)
  print("Average Wait Time:\t\t", avgwait)