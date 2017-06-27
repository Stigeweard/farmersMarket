# Refactored register
# this time I tried using some of the style principles I found on https://www.python.org/dev/peps/pep-0008/

# instead of the class approach, I wanted to try isolating more logic in functions and add a promotion
# that corresponds to every item, NA being no special price that isn't printed. This way the output will look
# more like the example and the logic should be easier to follow.
# Downside is now there is no 'generic' way of defining new promotions - however in the last version it constrained
# what a promotion could offer (i.e: no umbrella discount or percentage discount on all items)

_prices = {'CH1': 3.11, 'AP1': 6.00, 'CF1': 11.23, 'MK1': 4.75, 'OM1': 3.69}
_promotions = {'BOGO': -11.23, 'APPL': -1.50, 'CHMK': -4.75, 'NA': 0}

# generic for getting code count of either promotions or prices
def get_code_count(codes, all_codes):
    code_count = {}
    for code in all_codes:
        code_count[code] = 0
    for code in codes:
        code_count[code] += 1
    return code_count

# the following 3 functions are called on final basket items and return appropriate promo code to apply or 'NA'
# checks if at least 3 apples
def check_appl(basket):
    appl_count = get_code_count(basket, _prices.keys())
    if appl_count['AP1'] > 2:
        return 'APPL'
    else:
        return 'NA'

# checks if more than one coffee has been bought, adds promo on even occurences
def check_bogo(basket, promos):
    code_count = get_code_count(basket, _prices.keys())
    promo_count = get_code_count(promos, _promotions.keys())
    if code_count['CF1']/2 > promo_count['BOGO']:
        return 'BOGO'
    else:
        return 'NA'

# checks for milk promo if chai has been bought, only returns CHMK if it isn't in promo count (limit 1)
def check_chmk(basket, promos):
    code_count = get_code_count(basket, _prices.keys())
    promo_count = get_code_count(promos, _promotions.keys())
    if code_count['CH1'] > 0 and promo_count['CHMK'] == 0:
        return 'CHMK'
    else:
        return 'NA'

# sums up everything in basket and promos
def calculate_final_sum(basket, promos):
    total = 0
    for code in basket:
        total += _prices[code]
    for code in promos:
        total += _promotions[code]
    return total

# neat output string formatting to correct decimal places, using idx as the index corresponding to item position
# so that the applicable promo will print out below the item it applies to
def print_register(basket, promo, final_sum):
    print('{l: <10}{r: >25}'.format(l='Item', r='Price'))
    print('{l: <10}{r: >25}'.format(l='----', r='-----'))
    for idx, item in enumerate(basket):
        # print item and price
        print('{l: <10}{r: >25.2f}'.format(l=item, r=_prices[item]))
        if promo[idx] is not 'NA': # don't bother to print an NA promotion
            # print applicable promotion
            print('{l: >15}{r: >20.2f}'.format(l=promo[idx], r=_promotions[promo[idx]]))
    print('{:-^35}'.format('-'))
    print('{r: >35.2f}'.format(r=final_sum))

# initialize basket and promo as lists so that order is retained and index can be used in function above
# Basket: CH1, AP1, CF1, MK1
# Total price expected: $20.34
# NOTE: Here is where you can change the contents of the basket
_basket = []
_basket.append('CH1')
_basket.append('AP1')
_basket.append('CF1')
_basket.append('MK1')
_promo = []

for item in _basket:
    if item is 'AP1':
        _promo.append(check_appl(_basket))
    elif item is 'CF1':
        _promo.append(check_bogo(_basket, _promo))
    elif item is 'MK1':
        _promo.append(check_chmk(_basket, _promo))
    else:
        _promo.append('NA')
print_register(_basket, _promo, calculate_final_sum(_basket, _promo))
