from datetime import datetime 
i = str(input('date:'))
# formateo el valor del txt para volverlo un datatime y con formato que quiero

dt_start = datetime.strptime(i, "%d/%m/%Y").strftime("%d/%m/%Y")

print(dt_start)
