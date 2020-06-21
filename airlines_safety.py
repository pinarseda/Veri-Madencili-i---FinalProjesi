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
print ("Sirketlerin risk skorlari asagida gosterilmistir. Buna gore yuksek risk grubunda olan sirketler kara listede sayilmaktadir. Musterilerin bu risk grubunda ki sirketlerden kaçınması gerekir.")
print ("")
df["total"] = df["incidents_85_99"] + df["fatal_accidents_85_99"] + df["fatalities_85_99"] + df["incidents_00_14"] + df["fatal_accidents_00_14"] + df["fatalities_00_14"]
df["score"] = df["avail_seat_km_per_week"] / df["total"]
if  ((df["score"] > 0) & (df["score"] <= 4.19)).all():
    print ("0.00   YUKSEK RISK   4.19")
    print (df["score"])  
if ((df["score"] > 4.20) & (df["score"] <= 6.19)).all():
    print ("4.20   ORTA RISK   6.19")
    print (df["airline"])
if (df["score"] > 6.20).all():
    print ("6.20   DUSUK RISK   10.00")
    print (df["airline"])
down_side = df["airline"]
left_side = df["total"]
plt.plot(down_side,left_side)
plt.title("Sirketlerin Toplam Kaza Tablosu")
plt.show()
down_side = df["airline"]
left_side = df["score"]
plt.plot(down_side,left_side)
plt.title("Sirketlerin Score Tablosu")
plt.show()
