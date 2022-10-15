"""Berilgan oraliqdagi tub sonlarni topadigan dastur
Tuzuvchi: Tuychiev Muxtorjon
Sana:31.08.2022"""
def tub_son_aniqla(son1,son2):
    tub_sonlar=[]
    while son1<son2:
        sonlar=[]
        while True:
            for i in range(2,son1):
                x=son1%i
                if x==0:
                    sonlar.append(i)
            if sonlar:
                break
            else:
                tub_sonlar.append(son1)
                break
        son1+=1
    return tub_sonlar

son1=int(input("1-sonni kiriting: "))
son2=int(input("2-sonni kiriting: "))
tub_sonlar=tub_son_aniqla(son1,son2)
print(f"{son1} va {son2} orasidagi tub sonlar quyidagilar: {tub_sonlar}")