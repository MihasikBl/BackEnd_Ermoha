class flowers():
    """описание цветов"""
    def __init__(self,color,price,kind):
        """свойства цветов"""
        self.color = color
        self.price = price
        self.kind = kind

    def buying_flowers(self):
        """покупка цветов"""
        print("Покупатель купил цветы, которые имеют цвет: " + self.color + " .Относятся к виду: " + self.kind + " .Их цена составляет: ", self.price,"руб.")

    def total_price(self,TPrice):
        """Подсчет общей стоимости цветов"""
        TPrice = 0
        TPrice+=self.price


Flowers1 = flowers("КРАСНЫЙ",1200,"РОЗЫ")
Flowers2 = flowers("БЕЛЫЙ",1250,"РОЗЫ")
Flowers3 = flowers("ЖЕЛТЫЙ",1050,"ТЮЛЬПАНЫ")
Flowers4 = flowers("РОЗОВЫЙ",1020,"ТЮЛЬПАНЫ")
Flowers5 = flowers("КРАСНЫЙ",2700,"ПИОНЫ")

print(Flowers1.buying_flowers())
