class Sportlane:
    def __init__(self, nimi, kaal) -> None:
        self.sportlase_nimi = nimi
        self.kaaluke = kaal


    def __str__(self) -> str:
        return f"Nimi: {self.sportlase_nimi}, kaal: {self.kaaluke} kg"

    
class Maadleja(Sportlane):
    def __init__(self, nimi, kaal) -> None:
        super().__init__(nimi, kaal)
        if kaal <= 55:
            self.kaalukategooria = "kärbeskaal"
        elif kaal <= 66:
            self.kaalukategooria = "kergekaal"
        elif kaal <= 84:
            self.kaalukategooria = "keskkaal"
        elif kaal <= 96:
            self.kaalukategooria = "poolraskekaal"
        elif kaal > 96:
            self.kaalukategooria = "raskekaal"
        
    
    def muuda_kaalu(self, uus_kaal):
        self.kaaluke = uus_kaal
        if uus_kaal <= 55:
            self.kaalukategooria = "kärbeskaal"
        elif uus_kaal <= 66:
            self.kaalukategooria = "kergekaal"
        elif uus_kaal <= 84:
            self.kaalukategooria = "keskkaal"
        elif uus_kaal <= 96:
            self.kaalukategooria = "poolraskekaal"
        else:
            self.kaalukategooria = "raskekaal"  


    def __str__(self) -> str:
        return f"Nimi: {self.sportlase_nimi}, kaal: {self.kaaluke} kg, kaalukategooria: {self.kaalukategooria}"
    
indrek = Sportlane("Indrek", 105)
georg = Maadleja("Georg", 83)
kristjan = Maadleja("Kristjan", 115)

print(indrek)
print(georg)
print(kristjan)
kristjan.muuda_kaalu(95)
print(kristjan)