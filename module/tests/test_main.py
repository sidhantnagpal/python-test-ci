from ..main import adder, maxima

def test_adder_maxima_unpack():
	seq = [1, 2, 3, 4]

	assert adder(*seq) == 10
	assert maxima(*seq) == 4

def test_adder_maxima_explicit():
	assert adder(8, 9) == 17
	assert maxima(9) == 9
	assert maxima(-5, -6, 0, 5, 6) == 6
	assert adder(7) == 7
