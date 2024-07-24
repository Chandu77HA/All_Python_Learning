# Encapsulation

"""
Hiding Internal Details:

In object-oriented programming, an object is a self-contained unit that represents 
a real-world entity. This object has attributes (data) and methods (functions) 
associated with it. Encapsulation allows you to bundle these attributes and 
methods together within a class, forming a cohesive and logical unit.

The internal details of an object, such as its data members and the specific 
implementation of methods, are encapsulated within the class. This means that 
the inner workings of the object are hidden from external entities, 
including other parts of the program.

By hiding the internal details, you create a clear separation between the 
implementation and the external interface, reducing the complexity and making 
it easier to manage and maintain the code.

Exposing Only What is Necessary:

Encapsulation also involves selectively exposing only the essential 
features of an object to the outside world. The external interface, 
which includes public methods and properties, provides a controlled 
and well-defined way for other parts of the program to interact with 
the object.

The idea is to provide a set of methods that allow external entities to 
perform necessary operations on the object without revealing the underlying complexity. 
This promotes a level of abstraction, allowing users of the class to work with the 
object at a higher, more intuitive level.

By exposing only what is necessary, you maintain a level of control over the object's 
state and behavior. This control prevents unintended misuse and ensures that interactions 
with the object adhere to the intended design.

"""


class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder  # Internal detail
        self._balance = balance                # Internal detail

    def get_balance(self):
        return self._balance  # Exposed method

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount  # Internal detail

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount  # Internal detail


# Creating an instance of BankAccount
account = BankAccount("Alice", 1000)

# Using the external interface
print(account.get_balance())  # Exposing balance
account.deposit(500)           # Exposing deposit method
account.withdraw(200)          # Exposing withdraw method


"""
In this example, the internal details (attributes _account_holder and _balance) 
are hidden from external entities. The external interface consists of methods 
like get_balance, deposit, and withdraw, which expose only the necessary functionality 
for interacting with the BankAccount object. This encapsulation helps manage the 
complexity of the object and provides a clear and controlled way to work with it.
"""
