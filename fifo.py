#FIFO/FCFS
import csv

with open('processes.csv') as file:
  reader = csv.reader(file)

  print("FIFO/FCFS\n")
  print("-----------------------------------------------------------------------------")
  print("Process ID\t\tBurst Time\t\t\t\tTurnaround Time\t\t\t\tWait Time")
  print("-----------------------------------------------------------------------------") 
  
  count = 0

  for row in reader:
    if count != 0:
      id = "P" + row[0]
      burst = int(row[1])
  
      if count == 1:
        turnaround = burst
        wait = 0
        
        sumturn = burst
        sumwait = 0
      else:
        turnaround += burst 
        wait = turnaround - burst

        sumturn += turnaround
        sumwait += wait

      print("\t",id,"\t\t",burst, "\t\t\t", turnaround, "\t\t\t\t", wait)

    if count >= 6:
      break
    count += 1
  avgwait = sumwait/(count)
  avgturn = sumturn/(count)
  print()
  print("Average Turnaround Time:", avgturn)
  print("Average Wait Time:\t\t", avgwait)