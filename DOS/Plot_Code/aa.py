import matplotlib.pyplot as plt 
import csv 


with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\DOS\\5.5\\Fe DOS.csv" , "r") as y:
    reader=csv.reader(y)
    with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\DOS\\5.5\\Fe DOS2.csv","w",newline="") as x:
            writer=csv.writer(x)
            
            d=[]
            for row in reader:
                  c=[]
                  print(row[0],                row[1])
                  writer.writerow(c)
              
        #c.append(float(row[0].strip()))
        #d.append(float(row[1].strip())+50)
y.close