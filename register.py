class Product(object):
    """Product for sale at the Farmer's Market."""
    def __init__(self, code, name, price):
        super(Product, self).__init__()
        self.code = code
        self.name = name
        self.price = price

# instantiating and naming product variables by their code
CH1 = Product('CH1', 'Chai', 3.11)
AP1 = Product('AP1', 'Apples', 6.00)
CF1 = Product('CF1', 'Coffee', 11.23)
MK1 = Product('MK1', 'Milk', 4.75)
OM1 = Product('OM1', 'Oatmeal', 3.69)

class Promotion(object):
    """Defining promotion logic."""
    def __init__(self, name, product, productQuantity, benefitProduct, benefitQuantity, priceReduction, limit=float('inf')):
        super(Promotion, self).__init__()
        self.name = name
        self.product = product
        self.productQuantity = productQuantity
        self.benefitProduct = benefitProduct
        self.benefitQuantity = benefitQuantity
        self.priceReduction = priceReduction
        self.limit = limit

# instantiating and naming promotions by their code
BOGO = Promotion('BOGO', CF1, 1, CF1, 1, CF1.price)
# 0 for quantity if it should be applied to all existing items
APPL = Promotion('APPL', AP1, 3, AP1, float('inf'), 1.5)
CHMK = Promotion('CHMK', CH1, 1, MK1, 1, MK1.price, 1)

class Register(object):
    """docstring for Register."""
    def __init__(self, basketDict={}, promotions=[], balance=0.0):
        super(Register, self).__init__()
        self.basketDict = basketDict
        self.balance = balance
        self.promotions = promotions
        self.promoItems = []
        self.affectedItems = []
        for promo in promotions:
            self.promoItems.append(promo.product.code)

    def applyPromotion(self, promotion):
        self.promotions.append(promotion)
        self.promoItems.append(promotion.product.code)
        print 'Applied new promotion: ' + promotion.name

    def addItem(self, item, quantity=1):
        # if item already exists in basket, add to quantity. otherwise add to basket with given quantity
        if item.code in self.basketDict:
            self.basketDict[item.code]['quantity'] += quantity
        else:
            self.basketDict[item.code] = {}
            self.basketDict[item.code]['quantity'] = quantity
            self.basketDict[item.code]['itemObj'] = item

    def total(self):
        self.balance = 0
        print '{:20} {:^20} {:>20}'.format('item', 'promotion', 'price')
        print '{:20} {:^20} {:>20}'.format('----', '---------', '-----')
        for item in self.basketDict:
            for promo in self.promotions:
                if promo.product.name == item and promo.limit > 0 and promo.benefitQuantity > 0 and self.basketDict[item]['quantity'] >= promo.productQuantity:
                    # this needs to append as many items as allows considering limit, benefitQuantity, and productQuantity
                    self.affectedItems.append(item)
                    promo.limit -= 1
                    promo.benefitQuantity -= 1



        print '--------------------------------------------------------------'
        print 'Current total: $' + str(self.balance)
        # # loop over items in basket
        # for item in self.basketDict:
        #     timesToPrint = self.basketDict[item]['quantity']
        #     while timesToPrint > 0:
        #         print '{:20} {:>40}'.format(item, str(self.basketDict[item]['itemObj'].price))
        #         timesToPrint -= 1
        #     # check if current item exists in affectedItems
        #     for promo in self.promotions:
        #         # see if current item in basket has a possible applicable promotion
        #         if item == promo.product.code:
        #             # check to see if promotion requirements are met
        #             if promo.limit > 0:
        #                 # add affected item to list of affected items
        #                 print promo.productQuantity
        #                 if self.basketDict[item]['quantity'] >= promo.productQuantity:
        #                     self.affectedItems.append(item)
        #                     promo.limit -= 1
        #             else:
        #                 pass
        #     if item in self.affectedItems:
        #         print 'lol'
        #     self.balance += self.basketDict[item]['itemObj'].price * self.basketDict[item]['quantity']

test = Register()
test.applyPromotion(BOGO)
test.addItem(OM1)
test.addItem(CF1)
test.addItem(CF1)
test.total()
