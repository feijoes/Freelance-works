import threading
import csv


file = open("matrix1.csv", "r")
X = list(csv.reader(file, delimiter=","))

file.close()

file = open("matrix2.csv", "r")
Y = list(csv.reader(file, delimiter=","))

file.close()

m = len(Y)
listaResult = []
def mult(X, Y):
   global a
   result = [[0]*m]
   for z in range(len(Y[0])):
       for k in range(len(Y)):
           result[0][z] += int(X[0]) * int(Y[k][z])
           
   listaResult.append(result)
   print(f" {result}")
 
threads= list()

for i in range(len(X[0])):
   x = threading.Thread(target = mult, args=(X[i], Y))
   threads.append(x)
   x.start()

for thread in threads:
   thread.join()

with open('result.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for i in listaResult:
        writer.writerows(i)