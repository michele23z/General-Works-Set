import random

import numpy as np


# initialization of class Scacchiera
class Scacchiera:

    def __init__(self, lato = 8):
        if 0 < lato < 15 and lato != 2 and lato != 3:
            self.lato = lato
        else:
            self.lato = 8
            print("il valore del lato non è tollerato, è stato impostato il valore di default, 8")
        self.n_caselle = self.lato * self.lato
        return


    def print(self):
        print(f"Scacchiera lato {self.lato}")

# check if position is diagonal
    def diagonale(self, x, y, lista):
        x = x, y
        for el in lista:
            if abs(x[0] - el[0]) == abs(x[1] - el[1]):
                return True
            else:
                pass
        return False

# if solution is new, write it on file
    def archivio(self, s, l):
        soluzione = f"soluzione 8 Regine per scacchiera lato  {l} --->  {s} "
        archivio= open("archivio.txt", "r", encoding="utf-8")
        doc = archivio.readlines()
        flag = False
        for riga in doc:
            riga = riga.strip("\n")
            if riga == soluzione:
                archivio.close()
                flag = True
        if flag == True:
            return
        else:
            archivio = open("archivio.txt", "a", encoding="utf-8")
            archivio.write(soluzione)
            archivio.write("\n")
            archivio.close()
            return

# calculates the position of the queens on the board so that they cannot eat each other on the first move
# if found solution write it on file and create matrix, if not repeat
    def otto_regine(self):
        n =  self.lato
        regine = []
        caselle_x_no = []
        caselle_y_no = []
        regina = tuple([random.randint(0,n-1 ), random.randint(0,n-1)])
        regine.append(regina)
        caselle_x_no.append(regina[0])
        caselle_y_no.append(regina[1])
        for riga in range(self.lato):
            for colonna in range(self.lato):
                if riga in caselle_x_no or colonna in caselle_y_no:
                    pass
                elif self.diagonale(riga,colonna,regine):
                    pass
                else:
                    regina = (riga, colonna)
                    regine.append(regina)
                    caselle_x_no.append(riga)
                    caselle_y_no.append(colonna)

        if len(regine) == self.lato:
            print(regine)
            return self.archivio(regine, self.lato), self.matrice(self.lato, regine)
        else:
            print(f"sono riusto a trovare solo {len(regine)} posizionamenti {regine}")
            self.otto_regine()

# create matrix with numpy
    def matrice(self,l, r):
        mat = np.zeros((l,l))
        for el in r:
            mat[el]= 1
        print(mat)


# proof of work
dd= Scacchiera(6)
dd.otto_regine()


