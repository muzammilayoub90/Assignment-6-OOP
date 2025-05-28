class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

user1 = Bank
user2 = Bank

print("Before changing bank name:")
print(f"User1's bank name: {user1.bank_name}")
print(f"user2's bank name: {user2.bank_name}")

Bank.change_bank_name("XYZ Bank")

print(f"\nAfter changing bank name:")
print(f"user1's bank name: {user2.bank_name}")
print(f"user2's bank name: {user2.bank_name}")
