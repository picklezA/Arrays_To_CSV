def A_1D_to_CSV(fn, a):
    ash = str(a)
    ash = ash.replace("[","")
    ash = ash.replace("]","")
    ash = ash.replace(", ","\n")
    ash = ash.replace("'","")
    nf = open(fn+".csv","w")
    nf.write(ash)
    nf.close()
    
def A_2D_to_CSV(fn, a):
    ash = str(a)
    ash = ash.replace("], ","\n")
    ash = ash.replace("]","")
    ash = ash.replace("[","")
    ash = ash.replace("'","")
    nf = open(fn+".csv","w")
    nf.write(ash)
    nf.close()