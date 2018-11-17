from ..inventory import *
import pytest

def test_too_many_items():
    inv = Inventory()
    inv.wear_item('head', 'helmet')
    inv.wear_item('head', 'scarf')
    with pytest.raises(NoMoreWear):
        inv.wear_item('head', 'helmet')

def test_unwear():
    inv = Inventory()
    inv.wear_item('head', 'helmet')
    inv.wear_item('head', 'scarf')
    inv.unwear_item('head', 'scarf')
    print(inv.head)