import random
blood_type_dict = {
            "AA": "A",
            "AB": "AB",
            "AO": "A",
            "BB": "B",
            "BO": "B",
            "OO": "O"
        }
class Father:
    def __init__(self, Alel):
        self.Alel=Alel
        self.Btype = self.F_Btype()
        
    def F_Btype(self):
        return blood_type_dict.get(self.Alel, "Unknown")
        
class Mother:
    def __init__(self, Alel):
        self.Alel=Alel
        self.Btype = self.M_Btype()
        
    def M_Btype(self):
        return blood_type_dict.get(self.Alel, "Unknown")
        
class Child:
    def __init__(self,F_alel,M_alel):
        self.F_alel=random.choice([F_alel.Alel[0],F_alel.Alel[1]])
        self.M_alel=random.choice([M_alel.Alel[0],M_alel.Alel[1]])
        self.Alel = self.child_alel()
        self.Btype = self.child_BT()
    
    def child_alel(self):
        C_alel=[self.F_alel, self.M_alel]
        C_alel.sort()
        return ''.join(C_alel)
    
    def child_BT(self):
        return blood_type_dict.get(self.Alel, "Unknown")
        
# Main Program
Alel_tuple={'A','B','O'}
# print ({'C'} not in Alel_tuple)
#input alel ayah
Father_Alel = input("Masukkan Alel Ayah : ")
Father_Alel = Father_Alel.upper()#membuat huruf jadi kapital
#Memastikan input benar
while len(Father_Alel)!=2 or Father_Alel[0] not in Alel_tuple or Father_Alel[1] not in Alel_tuple:
    print("Masukkan 2 Alel valid !")
    Father_Alel = input("Masukkan Alel Ayah :")
    Father_Alel = Father_Alel.upper()
#mengurutkan string
Father_Alel = [Father_Alel[0],Father_Alel[1]]
Father_Alel.sort()
Father_Alel = ''.join(Father_Alel)



#input alel ayah
Mother_Alel = input("Masukkan Alel Ibu : ")
Mother_Alel =Mother_Alel.upper()#membuat huruf jadi kapital
#Memastikan input benar
while len(Mother_Alel)!=2 or Mother_Alel[0] not in Alel_tuple or Mother_Alel[1] not in Alel_tuple:
    print("Masukkan 2 Alel valid !")
    Mother_Alel = input("Masukkan Alel Ibu :")
    Mother_Alel = Mother_Alel.upper()
#mengurutkan string
Mother_Alel = [Mother_Alel[0],Mother_Alel[1]]
Mother_Alel.sort()
Mother_Alel = ''.join(Mother_Alel)


#Parent object
father = Father(Father_Alel)
mother = Mother(Mother_Alel)
# child object
child = Child(father,mother)

#printout
print("=======================================")
print(f"Golongan darah Ayah,  (Alel) : {father.Btype}, ({father.Alel})")
print(f"Golongan darah Ibu,   (Alel) : {mother.Btype}, ({mother.Alel})")
print("=======================================")
print(f"Golongan darah Anak,  (Alel) : {child.Btype}, ({child.Alel})")
print("=======================================")
        
