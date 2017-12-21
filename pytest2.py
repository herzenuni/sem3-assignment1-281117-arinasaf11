import pytest
import function2

def test_2():
    assert function2.func() == [14, 28, 29, 35, 41, 53, 67, 76, 82, 92]
    
def test_22():
  list=[]
  for i in range(10, 100):
    if function(i) % 17 == 0:
      list.append(i)
	assert(list == [14, 28, 29, 35, 41, 53, 67, 76, 82, 92])
