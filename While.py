# problema Ex: masina merge cat timp are inca benzina

litri_benzina =10
while litri_benzina > 0:
    #acceleram
    print('Vrum Vrum')
    #scadem benzina
    litri_benzina =litri_benzina -1
    #daca benzina este 3 litrii sau sub 3 litri se aprinde becul rosu
    if (litri_benzina <= 3):
        print('Se aprinde becul rosu')
#stop nu mai avem benzina
print("Stop! nu mai avem benzina")