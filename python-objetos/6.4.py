class TV:
    def __init__(self, volume=0, canal=1):
        self.volume = 0
        self.canal = 1
        self.mudaCanal(canal)
        self.mudaVolume(volume)

    def mudaCanal(self, canal):
        if canal < 0:
            self.canal = 0
        elif canal > 100:
            self.canal = 100
        else:
            self.canal = canal

    def mostraCanal(self):
        return self.canal

    def mudaVolume(self, volume):
        if volume < 0:
            self.volume = 0
        elif volume > 100:
            self.volume = 100
        else:
            self.volume = volume

    def mostraVolume(self):
        return self.volume

    def aumentaVolume(self):
        self.mudaVolume(self.volume+1)

    def diminuiVolume(self):
        self.mudaVolume(self.volume-1)