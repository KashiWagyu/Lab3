import price_info

input_price = {'Apple': 0.75, 'Banana': 0.50, 'Orange': 0.60, 'Grape': 3, 'Strawberry': 2.50 }
input_quantity = {'Apple': 20, 'Banana': 15, 'Orange': 12, 'Grape': 2, 'Strawberry': 3 }

def test_total_cost_shopping():
    
    test_total = 43.20

    result = price_info.total_cost_shopping(input_price, input_quantity)
     
    assert (result == test_total)

def test_cost_of_fruit():

    test_fruit = 'Apple'
    test_quantity = 20
    test_cost = 15.0

    result = price_info.cost_of_fruits(test_fruit, test_quantity, input_price)

    assert (result == test_cost)
    
