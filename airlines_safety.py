import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display , HTML

df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv")
print ("")
inc = df["incidents_85_99"]
fatal = df["fatalities_85_99"]
i = df[df.incidents_85_99 == df.incidents_85_99.max()]
x = i["airline"].tolist()
z = df[df.fatalities_85_99 == df.fatalities_85_99.max()]
y = z["airline"].tolist()
print ("1985-1999 arasinda" , max(inc) , "ile en yuksek kaza sayisi" , x , "," , max(fatal) , "ile en yuksek ölüm sayisi" , y , "aittir.")
print ("")
inc2 = df["incidents_00_14"]
fatal2 = df["fatalities_00_14"]
a = df[df.incidents_00_14 == df.incidents_00_14.max()]
b = a["airline"].tolist()
c = df[df.fatalities_00_14 == df.fatalities_00_14.max()]
d = c["airline"].tolist()
print ("2000-2014 arasinda" , max(inc2) , "ile en yuksek kaza sayisi" , b , "," , max(fatal2) , "ile en yuksek ölüm sayisi" , d , "aittir.")
print ("")
print ("Musteriler icin" , x , y , b , d , "sirketlerini tercih etmemek dogru karar olacaktir.")
if x==b:
    print ("Musteriler icin" , x ,"sirketini kesinlikle tercih etmemek dogru karar olacaktir.")
if x==d:
    print ("Musteriler icin" , x ,"sirketini kesinlikle tercih etmemek dogru karar olacaktir.")    
if y==b:
    print ("Musteriler icin" , y ,"sirketini kesinlikle tercih etmemek dogru karar olacaktir.")
if y==d:
    print ("Musteriler icin" , y ,"sirketini kesinlikle tercih etmemek dogru karar olacaktir.")    
if x==y:
    print ("Musteriler icin" , x ,"sirketini kesinlikle tercih etmemek dogru karar olacaktir.")
if b==d:
    print ("Musteriler icin" , b ,"sirketini kesinlikle tercih etmemek dogru karar olacaktir.")
print ("")
print ("Sirketlerin IASA(International Aviation Safety Assessment) Program'ına göre risk skorlari asagida gosterilmistir. Buna gore yuksek risk grubunda olan sirketler kara listede sayilmaktadir. Musterilerin bu risk grubunda ki sirketlerden kaçınması gerekir.")
print ("")
df["total"] = df["incidents_85_99"] + df["fatal_accidents_85_99"] + df["fatalities_85_99"] + df["incidents_00_14"] + df["fatal_accidents_00_14"] + df["fatalities_00_14"]
df["score"] = (df["avail_seat_km_per_week"]*780) / df["total"]
print("YUKSEK RISK 0.00-4.19     ORTA RISK 4.20-6.19     DUSUK RISK 6.20-10.00")
print ("")
n = pd.concat([df.airline, df.score], axis = 1)
print(n)
plt.figure(figsize=(10,5))
plt.subplot(2,2,1)   
plt.plot(df.airline,df.total,color="r") 
plt.xlabel("Havayolu")
plt.ylabel("Kaza Sayisi")
plt.title("Sirketlerin Toplam Kaza Tablosu")
plt.subplot(2,2,2)
plt.plot(df.airline,df.score,color="blue")
plt.xlabel("Havayolu")
plt.ylabel("Skor")
plt.title("Sirketlerin Skor Tablosu")
plt.show()    
