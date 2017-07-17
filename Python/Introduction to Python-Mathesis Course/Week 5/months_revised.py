# Μάθημα 17.3: Αρχεία
import calendar
import math

while True:
    year = input("Έτος(enter για έξοδο) :")
    if year == '':
        break
    try:
        year = int(year)
    except ValueError:
        continue
    my_year = calendar.calendar(year)
    my_year = my_year.replace("Mo Tu We Th Fr Sa Su", "Δε Τρ Τε Πε Πα Σα Κυ")
    #en_gr = {}
    filename = str(year)+'.txt'
    with open(filename, "w", encoding="utf-8") as newfile:
        with open("months.csv", "r", encoding="utf-8") as months_file:
            for line in months_file:
                new_line = line.strip()
                new_line = new_line.split(",")
                en_m = new_line[0]
                gr_m = new_line[1]
                #en_gr [en_m] = gr_m

                if len(gr_m)>len(en_m):
                    dif_len=len(gr_m)-len(en_m)
                    dif_len_l=math.ceil(dif_len/2)
                    dif_len_r=dif_len-dif_len_l

                    if not (' '*dif_len_l+en_m+' '*dif_len_r) in my_year:
                        en_m=' '*dif_len_l+en_m
                    else:
                        en_m=' '*dif_len_l+en_m+' '*dif_len_r
                else:
                    dif_len=len(en_m)-len(gr_m)
                    dif_len_l=math.ceil(dif_len/2)
                    dif_len_r=dif_len-dif_len_l
                    gr_m=' '*dif_len_l+gr_m

                my_year = my_year.replace(en_m, gr_m)
    my_year.replace(str(year), "Hμερολόγιο του "+ str(year))
    print(my_year)
    with open(str(year)+".txt", "w", encoding="utf-8") as f:
        f.write(my_year)
