import price_info

print("Test_price_info")

def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    test = 46.75

    assert (test == result)

def test_cost_of_fruits():
    result = price_info.cost_of_fruits('watermelon', 6)
    test = 39

    assert (test == result)