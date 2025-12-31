import pytest
from jar import Jar

def test_initial_capacity_and_size():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_deposit_valid():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(9)
    assert jar.size == 12

#def test_deposit_negative():
#    jar = Jar()
#    with pytest.raises(ValueError):
#       jar.deposit(-3)

#def test_deposit_over_capacity():
#    jar = Jar()
#    jar.deposit(10)
#    with pytest.raises(ValueError):
#        jar.deposit(5)  #would exceed jar capacity

def test_withdraw_valid():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(8)
    assert jar.size == 8
    jar.withdraw(3)
    assert jar.size == 5

#def test_withdraw_negative():
#    jar = Jar()
#    jar.deposit(4)
#    with pytest.raises(ValueError):
#        jar.withdrwa(-2)

#def test_withdraw_too_many():
#    jar = Jar()
#    jar.deposit(6)
#    with pytest.raises(ValueError):
#        jar.withdraw(10)

def test_str_representation():
    jar = Jar()
    assert str(jar) == 0
    jar.deposit(3)
    assert str(jar) == 3
    jar.deposit(9)
    assert str(jar) == 12
  