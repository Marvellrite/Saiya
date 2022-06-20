import pickle

def bwrite(file_name, list_of_no):
     
     file = open(file_name, "wb")
     pickle.dump(list_of_no,file)
     file.close()
     

list_of_no = [2,5,7,3,5]
file_name = "Selina.dat"
bwrite("Selina.dat", list_of_no)