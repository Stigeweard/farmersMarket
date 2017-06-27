import register


def test_pos_check_appl():
    assert register.check_appl(['AP1', 'AP1', 'AP1', 'AP1', 'CH1']) == 'APPL'
def test_neg_check_appl():
    assert register.check_appl(['AP1', 'AP1', 'MK1']) == 'NA'

def test_pos_check_bogo():
    assert register.check_bogo(['CF1', 'CF1'], ['APPL', 'CHMK'])
def test_neg_check_bogo():
    assert register.check_bogo(['CF1', 'CF1'], ['APPL', 'BOGO'])
