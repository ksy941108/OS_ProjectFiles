#Question 4
import csv

print("Question 4\n\nBefore Schedule/Given Processes")
print("------------------------------")
print("Process ID\t\t\tBurst Time")
print("------------------------------")

with open('processes.csv') as file:
  reader = csv.reader(file)

  burstarr = []
  idarr = []
  waitarr = []

  #Before Schedule - prints out given
  count = 0
  for row in reader:
    if count != 0:
      id = "P" + row[0]
      burst = int(row[1])

      if count == 1:
        turnaround = burst
        wait = 0
      else:
        turnaround += burst
        wait = turnaround - burst
      print("\t", id, "\t\t", burst)
    
      burstarr.append(burst)
      idarr.append(id)
      waitarr.append(wait)
    if count >= 250:
      break
    count += 1
    

  #calculating = 
  #print(calculating)
  print("\nScheduling")
  print("-------------------------------------------------------")
  print("Process ID\t\tBurst Time\t\t\t\tCompletion Time")
  print("-------------------------------------------------------")

  #Scheduling of processes
  tq = 4200000000000
  totalBurst = sum(burstarr)
  ct = 0 #completion time
  ctarr = []
  turntimes = []
  waittimes = []
  sumwait = 0
  waitNum = 0
  
  i = 0
  while len(burstarr) > 0:
    print("\t", idarr[i], "\t\t", burstarr[i], end = " ")

    if(burstarr[i] > tq):
      newVal = burstarr[i] - tq
      burstarr.append(newVal)
      idarr.append(idarr[i])
      ct += tq
      waitNum += tq
      
      
      
    else:
      ct += burstarr[i]
      turntimes.append(ct)
      
      
    waitarr.append(waitNum)
    burstarr.pop(i)
    idarr.pop(i)
    print("\t\t\t", ct, "\t")

 
  avgturn = sum(turntimes)/count
  avgwait = sum(waitarr)/count

  print("\nAverage Turnaround Time: ", avgturn)
  print("Average Wait Time:\t\t ", avgwait)