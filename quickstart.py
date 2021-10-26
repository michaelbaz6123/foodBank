import gspread

class Food():
    def __init__(self, name, type, size, quan, expir, source):
        self.name = name
        self.type = type
        self.size = size
        self.quan = int(quan)
        self.expir = expir
        self.source = source
    def change_stock(self, n):
        self.quan = n
    def inc_stock(self, n):
        self.quan += n
    def dec_stock(self, n):
        self.quan -= n

class Pantry():
    def __init__(self):
        self.food = []
        self.api_length = 0
        self.download_pantry()
    def add_food(self, name, type, size, quan, expir, source):
        if name in self.food:
            return -1
        item = Food(name, type, size, quan, expir, source)
        self.food.append(item)
        return 0
    def rem_food(self, name):
        for food in self.food:
            if food.name == name: self.food.remove(food)
        return 0
    def __str__(self):
        string = str()
        for item in self.food:
            string += item.name + " | " + item.size + " | " + item.quan + " | " + item.expir + "\n"
        return string
    def get_food_list(self, row):
        item = self.food[row]
        return [[item.name, item.type, item.size, item.quan, item.expir, item.source]]
    def download_pantry(self):
        i = 2
        while True:
            res = worksheet.get("A"+str(i)+":F"+str(i))
            if not len(res): break
            item = res[0]
            self.add_food(item[0], item[1], item[2], item[3], item[4], item[5])
            i += 1
        self.api_length = i - 2
    def update_pantry(self):
        for i in range(len(self.food)):
            worksheet.update("A"+str(i+2)+":F"+str(i+2), self.get_food_list(i))
        if len(self.food) < self.api_length:
            worksheet.batch_clear(["A"+str(len(self.food)+2)+":F"+str(self.api_length+2)])
        self.api_length = len(self.food)
    def change_stock(self, item, n):
        for food in self.food:
            if food.name == item:
                food.change_stock(n)
    def inc_stock(self, item, n):
        for food in self.food:
            if food.name == item:
                food.inc_stock(n)
    def dec_stock(self, item, n):
        for food in self.food:
            if food.name == item:
                food.dec_stock(n)

    

if __name__ == '__main__':
    gc = gspread.service_account(filename='credentials.json')
    sh = gc.open_by_key('10jEPKdjmYInQ2g7aLouSQUMsjoO8VvZX-NNbvT1QLQo')
    worksheet = sh.sheet1

    P = Pantry()
    P.rem_food("Lion Raisins")
    P.rem_food("Duchess Carrots")
    P.rem_food("Fritos: Original")
    P.add_food("Halloween Candy", "single serving bar", "10 oz", "12", "05/22", "-")
    P.change_stock("Lakeside Beef", 6)
    P.update_pantry()
