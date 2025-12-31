class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return f"Jar with {self._cookies} cookies (capacity {self._capacity})"

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self._cookies + n > self._capacity:
            raise ValueError("Too many cookies! Jar is full.")
        self._cookies += n
        print(f"Deposited {n} cookies. Total now: {self._cookies}")

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Number of cookies must be greater than 0.")
        if n > self._cookies:
            raise ValueError("Not enough cookies to withdraw.")
        self._cookies -= n
        print(f"Withdrew {n} cookies. Total now: {self._cookies}")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
