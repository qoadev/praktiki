class Fruits:
    def __init__(self, weight,price,name,date_payment,typeofpayment,sale):
        self.name = weight
        self.price = price
        self.name = name
        self.date_payment = date_payment
        self.typeofpayment = typeofpayment
        self.sale = sale
    def purchase(self):
        if self.typeofpayment == 'cash':
            self.sale = self.sale*0.95
        else:
            self.sale = self.price
        return self.sale

banana = Fruits(30,300,'banana','01.01.2001','cash',5)
orange = Fruits(40,500,'orange','01.01.2001','cash',6)
apple= Fruits(20,500,'apple','01.01.2001','cash',3)
waterlemon = Fruits(60,3900,'waterlemon','01.01.2001','cash',15)
print(banana.purchase(),orange.purchase(),apple.purchase(),waterlemon.purchase())


