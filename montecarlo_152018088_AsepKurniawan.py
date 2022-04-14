import random as ran
import numpy as np
import matplotlib.pyplot as plt

#angka acak bahan
x=[]

#frekuensi
y=[]

#probabilitas
z=[]

#probabilitas kumulatif
xx=[]

#batas bawah
yy=[]

#batas atas
zz=[]

#angka acak uji coba
xxx=[]

#angka permintaan
yyy=[]

#total prediksi
zzz=[]

#total dana
total=[]

#pengelompokan
aa=0
bb=0
cc=0
dd=0
ee=0
aaa=[]#plot a

print("*******  MONTECARLO  ********")
print("=============================")

#n angka
n=int(input("masukan jumlah angka : "))
for i in range (0,n) :
    a=ran.randint(0,4) #mengambil nilai random
    x.append(a)
print("Data statistik : "+ str(x))

#n frekuensi
for i in range (0,n):
    if x[i] == 0 :
        aa+=1
    elif x[i] == 1 :
        bb+=1
    elif x[i] == 2 :
        cc+=1
    elif x[i] == 3 :
        dd+=1
    elif x[i] == 4 :
        ee+=1
y.append(aa) #menambahkan item
y.append(bb)
y.append(cc)
y.append(dd)
y.append(ee)
print("frekuensi : "+ str(y))

#n prob  
for i in range (0,5):
    a=y[i]/n
    z.append(a)
print("probabilitas : "+ str(z))

#n prob kumulatif
a=z[0]
xx.append(a)
for i in range (0,4):
    b=xx[i]+z[i+1]
    xx.append(b)
print("probabilitas kumulatif : "+ str(xx))

#b.bawah
a=0
yy.append(a)
for i in range (0,4):
    a=xx[i]
    yy.append (a)
print("batas bawah kelas : "+ str(yy))

#b.atas
for i in range (0,4):
    a=xx[i]-0.01
    zz.append(a)
a=1
zz.append(a)
print("batas atas kelas : "+ str(zz))


#interval
print("=====================================================")
print("TAKSIRAN       |            RENTANG NILAI            |")
print("=====================================================")
for i in range (0,5):
    print("      ke-"+str(i)+"     |    "+str(yy[i])+" - "+str(zz[i])+" | ")
    print("__________________________________________________")

#prediksi
print("jumlah data uji coba : "+ str(n))
for i in range (0,n) :
    a=round(ran.random(),4)
    xxx.append(a)
print("data uji : "+str(xxx))

#nilai
for i in range (0,n) :
    if xxx[i]<zz[0] :
        a=0
    elif xxx[i]<zz[1]:
        a=1
    elif xxx[i]<zz[2]:
        a=2
    elif xxx[i]<zz[3]:
        a=3
    elif xxx[i]<zz[4]:
        a=4
    yyy.append(a)
    aaa.append(a)

print("==============")
print("| KESIMPULAN |")
print("==============")
print("prediksi permintaan : "+str(yyy))

#nilai prediksi
for i in range(0,n):
    a= yyy[i]*2500000
    zzz.append(a)
print("prediksi biaya : "+str(zzz))

#total nilai
res=0
for i in range(0,n):
    res=res+yyy[i]
print("prediksi permintaan total : "+str(res))
ren=0
for i in range(0,n):
    ren=ren+zzz[i]
print("prediksi total biaya : "+str(ren))

a=np.arange(0.0,n)
plt.title("MONTECARLO")
plt.xlabel("Nilai")
plt.ylabel("Permintaan")
plt.plot(a, aaa, color ="blue")
plt.show()