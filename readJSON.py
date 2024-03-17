ulkeler =["Name","Phone","iso3","Currency","Contionent"]
with open ("boy_kilo.csv","w",newline="") as dosya:
    csv_writer=csv.DictWriter(dosya,fieldnames=ulkeler)
    csv_writer.writeheader()    
    csv_writer.writerow({"Name":"names.json","Kilo":64})
    