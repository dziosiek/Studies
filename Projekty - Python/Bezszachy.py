import random
class Szachownica:
    def __init__(self):
        self.plansza =[8*["[ ]"],8*["[ ]"],8*["[ ]"],8*["[ ]"],8*["[ ]"],8*["[ ]"],8*["[ ]"],8*["[ ]"]]
    def wyswietl_plansze(self):
        print "=========================="
        for i in range(len(self.plansza)):
            plansza = ""
            for j in range(len(self.plansza[i])):
                plansza += self.plansza[i][j]
            print plansza
        print "=========================="
    def wyczysc_plansze(self):
        self.plansza =[8*["[ ]"],8*["[ ]"],8*["[ ]"],8*["[ ]"],8*["[ ]"],8*["[ ]"],8*["[ ]"],8*["[ ]"]]
    def rozmieszczenie_startowe(self,pionek):
        if pionek.kolor == "Bialy":
            if pionek.symbol == " W ":
                if self.plansza[7][0] == "[ ]":pionek.y = 7; pionek.x = 0; self.umiesc_pionek_startowo(pionek)
                else:pionek.y = 7; pionek.x = 7; self.umiesc_pionek_startowo(pionek)       
            elif pionek.symbol == " S ":
                if self.plansza[7][1] == "[ ]":pionek.y = 7; pionek.x = 1; self.umiesc_pionek_startowo(pionek)
                else:pionek.y = 7; pionek.x = 6; self.umiesc_pionek_startowo(pionek)
            elif pionek.symbol == " G ":
                if self.plansza[7][2] == "[ ]":pionek.y = 7; pionek.x = 2; self.umiesc_pionek_startowo(pionek)
                else:pionek.y = 7; pionek.x = 5; self.umiesc_pionek_startowo(pionek)
            elif pionek.symbol == " H ":
                if self.plansza[7][3] == "[ ]":pionek.y = 7; pionek.x = 3; self.umiesc_pionek_startowo(pionek)
            elif pionek.symbol == " K ":
                if self.plansza[7][4] == "[ ]":pionek.y = 7; pionek.x = 4; self.umiesc_pionek_startowo(pionek)
        elif pionek.kolor == "Czarny":
            if pionek.symbol == " W ":
                if self.plansza[0][0] == "[ ]":pionek.y = 0; pionek.x = 0; self.umiesc_pionek_startowo(pionek)
                else:pionek.y = 0; pionek.x = 7; self.umiesc_pionek_startowo(pionek)       
            elif pionek.symbol == " S ":
                if self.plansza[0][1] == "[ ]":pionek.y = 0; pionek.x = 1; self.umiesc_pionek_startowo(pionek)
                else:pionek.y = 0; pionek.x = 6; self.umiesc_pionek_startowo(pionek)
            elif pionek.symbol == " G ":
                if self.plansza[0][2] == "[ ]":pionek.y = 0; pionek.x = 2; self.umiesc_pionek_startowo(pionek)
                else:pionek.y = 0; pionek.x = 5; self.umiesc_pionek_startowo(pionek)
            elif pionek.symbol == " H ":
                if self.plansza[0][3] == "[ ]":pionek.y = 0; pionek.x = 3; self.umiesc_pionek_startowo(pionek)
            elif pionek.symbol == " K ":
                if self.plansza[0][4] == "[ ]":pionek.y = 0; pionek.x = 4; self.umiesc_pionek_startowo(pionek)
    def wyswietl_wspolrzedne(self,druzyna):
        lista_wspolrzednych = []
        for i in druzyna:
            lista_wspolrzednych.append((i.y,i.x))
        return lista_wspolrzednych
    def umiesc_pionek_startowo(self,pionek):
        """umieszcza pionek na danym polu - metoda startowa"""
        if pionek.y != None and pionek.x != None:
            self.plansza[pionek.y][pionek.x] = pionek.symbol 
    def umiesc_pionek(self,pionek,y,x):
        self.plansza[pionek.y][pionek.x] = "[ ]"
        pionek.y = y; pionek.x = x
        self.plansza[pionek.y][pionek.x] = pionek.symbol
    def koniec_gry(self,druzyna):
        licznik = 0
        for i in druzyna:
            if i.wartosc_x() == None and i.wartosc_y() == None:
                licznik += 1
        if licznik == 8:
            return True
                
class Pionek:
    def __init__(self,kolor):
        self.kolor = kolor
        self.x = None
        self.y = None
    def informacja_o_pionku(self):
        print "kolor:",self.kolor,"x:",self.x,"y:",self.y,"Symbol:",self.symbol
    def kolor(self):
        return self.kolor
    def wartosc_y(self):
        return self.y
    def wartosc_x(self):
        return self.x
    def xy_sojusznicy(self,szachownica):
        if self.kolor == "Bialy":
            return szachownica.wyswietl_wspolrzedne(biale)
        else:
            return szachownica.wyswietl_wspolrzedne(czarne)
    def xy_wrogowie(self,szachownica):
        if self.kolor == "Bialy":
            return szachownica.wyswietl_wspolrzedne(czarne)
        else:
            return szachownica.wyswietl_wspolrzedne(biale)
    def usun_pionek(self,y,x):
        for i in biale:
            if y == i.y and x == i.x:
                i.y = None
                i.x = None  
        for i in czarne:
            if y == i.y and x == i.x:
                i.y = None
                i.x = None
                
class Wieza(Pionek):
    def __init__(self,kolor):
        Pionek.__init__(self,kolor)
        self.symbol = " W "
    def zmien_pozycje_wieza(self,szachownica):
        """zmienia pozycje pionka wieza"""
        gora = self.y; dol = 7 - self.y; lewo = self.x; prawo = 7 - self.x
        print "Ruch wykonuje:",self.informacja_o_pionku()
        print "Sojusznicy: ",self.xy_sojusznicy(szachownica)
        print "Wrogowie: ",self.xy_wrogowie(szachownica)
        wykonany_ruch = False
        while wykonany_ruch == False:
            kierunek = random.choice(("gora","dol","lewo","prawo"))
            if kierunek == "gora" and gora > 0: 
                krok = random.randint(1,gora)
                for i in range(krok):
                    if (self.y-1, self.x) in self.xy_sojusznicy(szachownica):
                        break
                    elif (self.y-1, self.x) in self.xy_wrogowie(szachownica):
                        x = self.x; y = self.y-1
                        self.usun_pionek(y,x)
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
                        break
                    else:
                        x = self.x; y = self.y-1   
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
            elif kierunek == "dol" and dol > 0: 
                krok = random.randint(1,dol)
                for i in range(krok):
                    if (self.y+1, self.x) in self.xy_sojusznicy(szachownica):
                        break
                    elif (self.y+1, self.x) in self.xy_wrogowie(szachownica):
                        x = self.x; y = self.y+1
                        self.usun_pionek(y,x)
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
                        break
                    else:
                        x = self.x; y = self.y+1   
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
            elif kierunek == "lewo" and lewo > 0: 
                krok = random.randint(1,lewo)
                for i in range(krok):
                    if (self.y, self.x-1) in self.xy_sojusznicy(szachownica):
                        break
                    elif (self.y, self.x-1) in self.xy_wrogowie(szachownica):
                        x = self.x-1; y = self.y
                        self.usun_pionek(y,x)
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
                        break
                    else:
                        x = self.x-1; y = self.y   
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
            elif kierunek == "prawo" and prawo > 0: 
                krok = random.randint(1,prawo)
                for i in range(krok):
                    if (self.y, self.x+1) in self.xy_sojusznicy(szachownica):
                        break
                    elif (self.y, self.x+1) in self.xy_wrogowie(szachownica):
                        x = self.x+1; y = self.y
                        self.usun_pionek(y,x)
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
                        break
                    else:
                        x = self.x+1; y = self.y   
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
            
class Skoczek(Pionek):
    def __init__(self,kolor):
        Pionek.__init__(self,kolor)
        self.symbol = " S "
    def zmien_pozycje_skoczek(self,szachownica):
        wykonany_ruch = False
        print "Ruch wykonuje:",self.informacja_o_pionku()
        print "Sojusznicy: ",self.xy_sojusznicy(szachownica)
        print "Wrogowie: ",self.xy_wrogowie(szachownica)
        while wykonany_ruch == False:
            kierunek = random.choice(("1GL","2GL","1GP","2GP","1DP","2DP","1DL","2DL"))
            if kierunek == "1GL" and self.wartosc_y() -1 >= 0 and self.wartosc_x() - 2 >= 0:
                if (self.wartosc_y() - 1,self.wartosc_x() - 2) in self.xy_wrogowie(szachownica):
                    y = self.wartosc_y() - 1; x = self.wartosc_x() - 2
                    self.usun_pionek(y,x)
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
                elif (self.wartosc_y() - 1,self.wartosc_x() - 2) not in self.xy_sojusznicy(szachownica):
                    y = self.wartosc_y() - 1; x = self.wartosc_x() - 2
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
            elif kierunek == "2GL" and self.wartosc_y() -2 >= 0 and self.wartosc_x() - 1 >= 0:
                if (self.wartosc_y() - 2,self.wartosc_x() - 1) in self.xy_wrogowie(szachownica):
                    y = self.wartosc_y() - 2; x = self.wartosc_x() - 1
                    self.usun_pionek(y,x)
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
                elif (self.wartosc_y() - 2,self.wartosc_x() - 1) not in self.xy_sojusznicy(szachownica):
                    y = self.wartosc_y() - 2; x = self.wartosc_x() - 1
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
            elif kierunek == "1GP" and self.wartosc_y() -1 >= 0 and self.wartosc_x() + 2 <= 7:
                if (self.wartosc_y() -1,self.wartosc_x() + 2) in self.xy_wrogowie(szachownica):
                    y = self.wartosc_y() -1; x = self.wartosc_x() + 2
                    self.usun_pionek(y,x)
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
                elif (self.wartosc_y() -1,self.wartosc_x() + 2) not in self.xy_sojusznicy(szachownica):
                    y = self.wartosc_y() -1; x = self.wartosc_x() + 2
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
            elif kierunek == "2GP" and self.wartosc_y() -2 >= 0  and self.wartosc_x() + 1 <= 7:
                if (self.wartosc_y() -2,self.wartosc_x() + 1) in self.xy_wrogowie(szachownica):
                    y = self.wartosc_y() -2; x = self.wartosc_x() + 1
                    self.usun_pionek(y,x)
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
                elif (self.wartosc_y() -2,self.wartosc_x() + 1) not in self.xy_sojusznicy(szachownica):
                    y = self.wartosc_y() -2; x = self.wartosc_x() + 1
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
            elif kierunek == "1DP" and self.wartosc_y() +1 <= 7 and self.wartosc_x() + 2 <= 7:
                if (self.wartosc_y() +1, self.wartosc_x() + 2) in self.xy_wrogowie(szachownica):
                    y = self.wartosc_x() + 2; x = self.wartosc_x() + 1
                    self.usun_pionek(y,x)
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
                elif (self.wartosc_y() +1,self.wartosc_x() + 2) not in self.xy_sojusznicy(szachownica):
                    y = self.wartosc_y() +1; x = self.wartosc_x() + 2
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
            elif kierunek == "2DP" and self.wartosc_y() +2 <= 7 and self.wartosc_x() + 1 <= 7:
                if (self.wartosc_y() +2, self.wartosc_x() + 1) in self.xy_wrogowie(szachownica):
                    y = self.wartosc_y() + 2; x = self.wartosc_x() + 1
                    self.usun_pionek(y,x)
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
                elif (self.wartosc_y() +2,self.wartosc_x() + 1) not in self.xy_sojusznicy(szachownica):
                    y = self.wartosc_y() +2; x = self.wartosc_x() + 1
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
            elif kierunek == "1DL" and self.wartosc_y() +1 <= 7 and self.wartosc_x() - 2 >= 0:
                if (self.wartosc_y() +1, self.wartosc_x() - 2) in self.xy_wrogowie(szachownica):
                    y = self.wartosc_y() + 1; x = self.wartosc_x() - 2
                    self.usun_pionek(y,x)
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
                elif (self.wartosc_y() +1,self.wartosc_x() - 2) not in self.xy_sojusznicy(szachownica):
                    y = self.wartosc_y() +1; x = self.wartosc_x() - 2
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
            elif kierunek == "2DL" and self.wartosc_y() +2 <= 7 and self.wartosc_x() - 1 >= 0:
                if (self.wartosc_y() + 2, self.wartosc_x() - 1) in self.xy_wrogowie(szachownica):
                    y = self.wartosc_y() + 2; x = self.wartosc_x() - 1
                    self.usun_pionek(y,x)
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
                elif (self.wartosc_y() + 2,self.wartosc_x() - 1) not in self.xy_sojusznicy(szachownica):
                    y = self.wartosc_y() + 2; x = self.wartosc_x() - 1
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
                           
class Goniec(Pionek):
    def __init__(self,kolor):
        Pionek.__init__(self,kolor)
        self.symbol = " G "
    def zmien_pozycje_goniec(self,szachownica):
        pd = (7-self.wartosc_y(),7-self.wartosc_x())
        pg = (self.wartosc_y(),7-self.wartosc_x())
        ld = (7-self.wartosc_y(),self.wartosc_x())
        lg = (self.wartosc_y(),self.wartosc_x())
        print "Ruch wykonuje:",self.informacja_o_pionku()
        print "Sojusznicy: ",self.xy_sojusznicy(szachownica)
        print "Wrogowie: ",self.xy_wrogowie(szachownica)
        wykonany_ruch = False
        while wykonany_ruch == False:
            kierunek = random.choice(("lg","pg","pd","ld"))
            if kierunek == "lg" and min(lg) > 0:
                krok = random.randint(1,min(lg))
                for i in range(krok):
                    if (self.wartosc_y()-1,self.wartosc_x()-1) in self.xy_sojusznicy(szachownica):
                        break
                    elif(self.wartosc_y()-1,self.wartosc_x()-1) in self.xy_wrogowie(szachownica):
                        y = self.wartosc_y()-1; x = self.wartosc_x()-1
                        self.usun_pionek(y,x)
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
                    else:
                        y = self.wartosc_y()-1; x = self.wartosc_x()-1
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True  
            elif kierunek == "pg" and min(pg) > 0:
                krok = random.randint(1,min(pg))
                for i in range(krok):
                    if (self.wartosc_y()-1,self.wartosc_x()+1) in self.xy_sojusznicy(szachownica):
                        break
                    elif(self.wartosc_y()-1,self.wartosc_x()+1) in self.xy_wrogowie(szachownica):
                        y = self.wartosc_y()-1; x = self.wartosc_x()+1
                        self.usun_pionek(y,x)
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
                    else:
                        y = self.wartosc_y()-1; x = self.wartosc_x()+1
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
            elif kierunek == "pd" and min(pd) > 0:
                krok = random.randint(1,min(pd))
                for i in range(krok):
                    if (self.wartosc_y()+1,self.wartosc_x()+1) in self.xy_sojusznicy(szachownica):
                        break
                    elif(self.wartosc_y()+1,self.wartosc_x()+1) in self.xy_wrogowie(szachownica):
                        y = self.wartosc_y()+1; x = self.wartosc_x()+1
                        self.usun_pionek(y,x)
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
                    else:
                        y = self.wartosc_y()+1; x = self.wartosc_x()+1
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
            elif kierunek == "ld" and min(ld) > 0:
                krok = random.randint(1,min(ld))
                for i in range(krok):
                    if (self.wartosc_y()+1,self.wartosc_x()-1) in self.xy_sojusznicy(szachownica):
                        break
                    elif(self.wartosc_y()+1,self.wartosc_x()-1) in self.xy_wrogowie(szachownica):
                        y = self.wartosc_y()+1; x = self.wartosc_x()-1
                        self.usun_pionek(y,x)
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
                    else:
                        y = self.wartosc_y()+1; x = self.wartosc_x()-1
                        szachownica.umiesc_pionek(self,y,x)
                        wykonany_ruch = True
                 
class Hetman(Pionek, Goniec, Wieza):
    def __init__(self,kolor):
        Pionek.__init__(self,kolor)
        Goniec.__init__(self,kolor)
        Wieza.__init__(self,kolor)
        self.symbol = " H "
    def zmien_pozycje_hetman(self,szachownica):
        print "Ruch wykonuje:",self.informacja_o_pionku()
        print "Sojusznicy: ",self.xy_sojusznicy(szachownica)
        print "Wrogowie: ",self.xy_wrogowie(szachownica)
        ruch = random.choice(("Goniec","Wieza"))
        if ruch == "Goniec":
            self.zmien_pozycje_goniec(szachownica)
        elif ruch == "Wieza":
            self.zmien_pozycje_wieza(szachownica)
    
class Krol(Pionek):
    def __init__(self,kolor):
        Pionek.__init__(self,kolor)
        self.symbol = " K "
    def zmien_pozycje_krol(self,szachownica):
        print "Ruch wykonuje:",self.informacja_o_pionku()
        print "Sojusznicy: ",self.xy_sojusznicy(szachownica)
        print "Wrogowie: ",self.xy_wrogowie(szachownica)
        wykonany_ruch = False
        while wykonany_ruch == False:
            y = random.randint(-1,1)
            x = random.randint(-1,1)
            if (0 <= self.wartosc_y()+y <=7) and (0 <= self.wartosc_x()+x <=7): 
                if (self.wartosc_y()+y,self.wartosc_x()+x) in self.xy_wrogowie(szachownica):
                    y = self.wartosc_y()+y; x = self.wartosc_x()+x
                    self.usun_pionek(y,x)
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True
                elif (self.wartosc_y()+y,self.wartosc_x()+x) not in self.xy_sojusznicy(szachownica):
                    y = self.wartosc_y()+y; x = self.wartosc_x()+x
                    szachownica.umiesc_pionek(self,y,x)
                    wykonany_ruch = True

##################################################################
szachownica = Szachownica();  biale = [];  czarne = []
for i in range(8): biale.append(i); czarne.append(i)
biale[0] = Wieza("Bialy");biale[7] = Wieza("Bialy");biale[1] = Skoczek("Bialy");biale[6] = Skoczek("Bialy");
biale[2] = Goniec("Bialy");biale[5] = Goniec("Bialy");biale[3] = Hetman("Bialy");biale[4] = Krol("Bialy")
czarne[0] = Wieza("Czarny");czarne[7] = Wieza("Czarny");czarne[1] = Skoczek("Czarny");czarne[6] = Skoczek("Czarny");
czarne[2] = Goniec("Czarny");czarne[5] = Goniec("Czarny");czarne[3] = Hetman("Czarny");czarne[4] = Krol("Czarny")
for i in range(8):
    szachownica.rozmieszczenie_startowe(biale[i])
    szachownica.rozmieszczenie_startowe(czarne[i])
szachownica.wyswietl_plansze()
for i in range(1000):
    
     if szachownica.koniec_gry(biale) == True:
        print "wygraly CZARNE"
        break
     while True:
         numer = random.randint(0,7)
         if (biale[numer].wartosc_x() != None) and (biale[numer].wartosc_y() != None):
             if numer == 0 or numer == 7:biale[numer].zmien_pozycje_wieza(szachownica)
             if numer == 1 or numer == 6:biale[numer].zmien_pozycje_skoczek(szachownica)
             if numer == 2 or numer == 5:biale[numer].zmien_pozycje_goniec(szachownica)
             if numer == 3:biale[numer].zmien_pozycje_hetman(szachownica)
             if numer == 4:biale[numer].zmien_pozycje_krol(szachownica)
             szachownica.wyswietl_plansze()
             break
     if szachownica.koniec_gry(czarne) == True:
        print "wygraly BIALE"
        break
     while True:
         numer = random.randint(0,7)
         if (czarne[numer].wartosc_x() != None) and (czarne[numer].wartosc_y() != None):
             if numer == 0 or numer == 7:czarne[numer].zmien_pozycje_wieza(szachownica)
             if numer == 1 or numer == 6:czarne[numer].zmien_pozycje_skoczek(szachownica)
             if numer == 2 or numer == 5:czarne[numer].zmien_pozycje_goniec(szachownica)
             if numer == 3:czarne[numer].zmien_pozycje_hetman(szachownica)
             if numer == 4:czarne[numer].zmien_pozycje_krol(szachownica)
             szachownica.wyswietl_plansze()
             break
