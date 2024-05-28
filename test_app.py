from app import add, sous, mult, div

def test_answer_add1():
     assert  add(0,5) == 5
def test_answer_add2():
     assert add(3,4) == 7
def test_answer_add3():
     assert add(-3,4) == 1

def test_answer_sous1():
     assert sous(5,4) == 1
def test_answer_sous2():
     assert sous(5,4) == 1
def test_answer_sous3():
     assert sous(5,4) == 1  

def test_answer_div1():
     assert div(2,2) == 1
def test_answer_div2():
     assert div(2,2) == 1
def test_answer_div3():
     assert div(2,2) == 1 
def test_answer_div3():
     assert div(2,2) == 1

def test_answer_mult1():
     assert mult(2,2) == 4
def test_answer_mult2():
     assert mult(2,0) == 0
def test_answer_mult3():
     assert mult(2,2) == 4