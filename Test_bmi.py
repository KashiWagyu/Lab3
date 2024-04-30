import Lab2.bmi as bmi

print("Test Lab 2")

def test_bmi_normal_weight():
    input_weight = 65
    input_height = 1.78
    test_bmi = 0

    result = bmi.calculate_bmi(input_height,input_weight)

    assert(result == test_bmi)


def test_bmi_over_weight():
    input_weight = 98
    input_height = 1.78
    test_bmi = 1

    result = bmi.calculate_bmi(input_height,input_weight)

    assert(result == test_bmi)

def test_bmi_under_weight():
    input_weight = 50
    input_height = 1.78
    test_bmi = -1

    result = bmi.calculate_bmi(input_height,input_weight)

    assert(result == test_bmi)