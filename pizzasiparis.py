#pizza sipariş uygulaması
import tkinter as tk

#panel oluşturucusu
form = tk.Tk()
form.geometry("500x500+400+100")
form.title("Pizza Sipariş Programı")
#panel baslığı
baslik=tk.Label(text="Pizza Sipariş Programına Hoşgeldiniz",fg="gray",font="times 17 bold").pack()

entr = tk.StringVar()#kullanıcıdan ad bilgisi 
entr1 = tk.StringVar()#kullanıcıdan adres bilgisi

#kullanıcıdan aldığımız bilgiler kısmı
lbl_ad=tk.Label(form,text="Ad-Soyad:",fg="gray",font="times 12 bold").place(x=10,y=40)
lbl_boyut=tk.Label(form,text="Boyut:",fg="gray",font="times 12 bold").place(x=10,y=70)
lbl_icindekiler=tk.Label(form,text="İçindekiler:",fg="gray",font="times 12 bold").place(x=10,y=100)
lbl_adres=tk.Label(form,text="Adres:",fg="gray",font="times 12 bold").place(x=10,y=130)
entry_ad =tk.Entry(textvariable=entr).place(x=100,y=40)
entry_adres = tk.Entry(textvariable=entr1).place(x=100,y=130)

boyut = tk.StringVar()#pizzanın boyutu 

#pizza nın boyutunun olduğu kısım
radiobuton_küçük =tk.Radiobutton(form,text="Küçük Boy",activebackground="green",value="Küçük Boy",variable=boyut).place(x=100,y=70)
radiobuton_orta =tk.Radiobutton(form,text="Orta Boy",activebackground="green",value="Orta Boy",variable=boyut).place(x=180,y=70)
radiobuton_büyük =tk.Radiobutton(form,text="Büyük Boy",activebackground="green",value="Büyük Boy",variable=boyut).place(x=250,y=70)

#pizzanın malzemelerine atanan değişken
deger1=tk.StringVar()
deger2=tk.StringVar()
deger3=tk.StringVar()

#pizzada hangi malzemeler olmalı 
check1 = tk.Checkbutton(form,text="Sucuklu",activebackground="green",variable=deger1,onvalue="-Sucuklu-").place(x=100,y=100)
check1 = tk.Checkbutton(form,text="Mısır",activebackground="green",variable=deger2,onvalue="-Mısır-").place(x=177,y=100)
check1 = tk.Checkbutton(form,text="Acılı Sos",activebackground="green",variable=deger3,onvalue="-Acılı Sos-").place(x=240,y=100)

#siparis ver e atanmış fonksiyon kodları
def siparisver():
    label_bilgi=tk.Label(form,text="Sipariş Bilgileri",fg="gray",font="times 16 bold").place(x=50,y=240)
    lbl_ad=tk.Label(form,text="Ad-Soyad:",fg="gray",font="times 12 bold").place(x=10,y=270)
    lbl_boyut=tk.Label(form,text="Boyut:",fg="gray",font="times 12 bold").place(x=10,y=300)
    lbl_icindekiler=tk.Label(form,text="İçindekiler:",fg="gray",font="times 12 bold").place(x=10,y=330)
    lbl_adres=tk.Label(form,text="Adres:",fg="gray",font="times 12 bold").place(x=10,y=360)

    lbl_ad1=tk.Label(form,text=entr.get(),fg="gray",font="times 12 bold").place(x=100,y=270)
    lbl_boyu1t=tk.Label(form,text=boyut.get(),fg="gray",font="times 12 bold").place(x=100,y=300)
    lbl_icindekiler1=tk.Label(form,text=deger1.get()+deger2.get()+deger3.get(),fg="gray",font="times 12 bold").place(x=100,y=330)
    lbl_adres1=tk.Label(form,text=entr1.get(),fg="gray",font="times 12 bold").place(x=100,y=360)
#iptal et'e atanmış fonksiyon
def iptaletl():
    form.quit()

#sipariş ver  ve iptal et butonları
siparis =tk.Button(form,text="Sipariş Ver",activebackground="green",command=siparisver).place(x=100,y=160)
iptal =tk.Button(form,text="İptal Et",activebackground="red",command=iptaletl).place(x=200,y=160)


#Sipariş bilgileri geleceği kısım
label_bilgi=tk.Label(form,text="Sipariş Bilgileri",fg="gray",font="times 16 bold").place(x=50,y=240)

form.mainloop()