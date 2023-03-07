# version: 1.0
# author: picklez

def A_1D_to_CSV(file_name, array):
    array_str = str(array)
    array_str = array_str.replace("[","")
    array_str = array_str.replace("]","")
    array_str = array_str.replace(", ","\n")
    array_str = array_str.replace("'","")
    new_file = open(file_name+".csv","w")
    new_file.write(array_str)
    new_file.close()
    
def A_2D_to_CSV(file_name, array):
    array_str = str(array)
    array_str = array_str.replace("], ","\n")
    array_str = array_str.replace("]","")
    array_str = array_str.replace("[","")
    array_str = array_str.replace("'","")
    new_file = open(file_name+".csv","w")
    new_file.write(array_str)
    new_file.close()
