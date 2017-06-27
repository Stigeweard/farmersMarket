import register


def test_pos_check_appl():
    assert register.check_appl(['AP1', 'AP1', 'AP1', 'AP1', 'CH1']) == 'APPL'
def test_neg_check_appl():
    assert register.check_appl(['AP1', 'AP1', 'MK1']) == 'NA'

def test_pos_check_bogo():
    assert register.check_bogo(['CF1', 'CF1'], ['APPL', 'CHMK']) == 'BOGO'
def test_neg_check_bogo():
    assert register.check_bogo(['CF1', 'CF1'], ['APPL', 'BOGO']) == 'NA'

def test_pos_check_chmk():
    assert register.check_chmk(['CH1', 'CF1', 'MK1'], ['APPL', 'BOGO']) == 'CHMK'
def test_neg_check_chmk():
    assert register.check_chmk(['CH1', 'MK1', 'CH1', 'MK1'], ['CHMK', 'BOGO']) == 'NA'

# testing that the lengths and sorted lists are equal
def test_build_promo_list():
    func_test = register.build_promo_list(['AP1', 'AP1', 'CH1', 'AP1'])
    should_be = ['APPL', 'APPL', 'NA', 'APPL']
    length_equal = len(func_test) == len(should_be)
    sorted_equal = sorted(func_test) == sorted(should_be)
    assert length_equal and sorted_equal

# four test specs from challenge document
def test_calc_total_sum_one():
    basket = ['CH1', 'AP1', 'CF1', 'MK1']
    promo_list = register.build_promo_list(basket)
    assert register.calculate_final_sum(basket, promo_list) == 20.34
def test_calc_total_sum_two():
    basket = ['MK1', 'AP1']
    promo_list = register.build_promo_list(basket)
    assert register.calculate_final_sum(basket, promo_list) == 10.75
def test_calc_total_sum_three():
    basket = ['CF1', 'CF1']
    promo_list = register.build_promo_list(basket)
    assert register.calculate_final_sum(basket, promo_list) == 11.23
def test_calc_total_sum_four():
    basket = ['AP1', 'AP1', 'CH1', 'AP1']
    promo_list = register.build_promo_list(basket)
    assert register.calculate_final_sum(basket, promo_list) == 16.61
