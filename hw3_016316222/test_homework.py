import unittest
import io
import sys
import os
import shelve


# --- Custom Test Runner for Verbose, Clean Output ---

class CustomTestResult(unittest.TextTestResult):
    def startTest(self, test):
        super().startTest(test)
        self.stream.write(f"    [ RUNNING ] {test.shortDescription() or test.id()}\n")
        self.stream.flush()

    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write(f"    [  PASS   ] {test.shortDescription() or test.id()}\n")
        self.stream.flush()

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.write(f"    [  FAIL   ] {test.shortDescription() or test.id()}\n")
        self.stream.flush()

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.write(f"    [  ERROR  ] {test.shortDescription() or test.id()}\n")
        self.stream.flush()


class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult


# --- End of Custom Test Runner ---

# IMPORTANT: This allows the test runner to find your code.
sys.path.insert(0, './')

try:
    from banking.accounts import BankAccount, SavingAccount, CheckingAccount
    from banking.exceptions import InsufficientFundsError, InvalidAmountError
    from banking.persistence import Bank
except ImportError as e:
    print(f"ERROR: Could not import files. Make sure your directory structure is correct.")
    print(f"  - Details: {e}")


    # Define dummy classes and functions to prevent further errors during test collection.
    class BankAccount:
        pass


    class SavingAccount(BankAccount):
        pass


    class CheckingAccount(BankAccount):
        pass


    class InsufficientFundsError(Exception):
        pass


    class InvalidAmountError(Exception):
        pass


    class Bank:
        pass


class TestAccountClasses(unittest.TestCase):
    """Tests for Account Classes (accounts.py)"""

    def test_01_bank_account_creation(self):
        """Account: Should create a BankAccount with correct owner and balance"""
        acc = BankAccount("Alice", 100.0)
        self.assertEqual(acc.owner_name, "Alice")
        self.assertEqual(acc.balance, 100.0)

    def test_02_deposit_valid_amount(self):
        """Account: Should handle valid deposits correctly"""
        acc = BankAccount("Bob", 50.0)
        acc.deposit(50.0)
        self.assertEqual(acc.balance, 100.0)

    def test_03_deposit_invalid_amount(self):
        """Account: Should raise InvalidAmountError for negative/zero deposits"""
        acc = BankAccount("Charlie", 100.0)
        with self.assertRaises(InvalidAmountError):
            acc.deposit(-50.0)
        with self.assertRaises(InvalidAmountError):
            acc.deposit(0)

    def test_04_base_class_withdraw_not_implemented(self):
        """Account: Base BankAccount withdraw should raise NotImplementedError"""
        acc = BankAccount("David", 200.0)
        with self.assertRaises(NotImplementedError):
            acc.withdraw(50.0)

    def test_05_account_str_representation(self):
        """Account: __str__ should return correctly formatted string"""
        acc = BankAccount("Eve", 150.756)
        # Balance should be rounded to 2 decimal places
        self.assertEqual(str(acc), "Account Owner: Eve, Balance: $150.76")
        acc2 = BankAccount("Frank", 200)
        self.assertEqual(str(acc2), "Account Owner: Frank, Balance: $200.00")


class TestSavingAccount(unittest.TestCase):
    """Tests for SavingAccount specific functionality"""

    def test_01_saving_withdraw_valid(self):
        """SavingAccount: Should withdraw correctly, including $2 fee"""
        acc = SavingAccount("Grace", 100.0)
        acc.withdraw(50.0)
        # 100 - 50 (amount) - 2 (fee) = 48
        self.assertEqual(acc.balance, 48.0)

    def test_02_saving_withdraw_insufficient_funds(self):
        """SavingAccount: Should raise InsufficientFundsError correctly"""
        acc = SavingAccount("Heidi", 50.0)
        # Cannot withdraw 50, because 50 (amount) + 2 (fee) > 50 (balance)
        with self.assertRaises(InsufficientFundsError):
            acc.withdraw(50.0)

    def test_03_saving_withdraw_invalid_amount(self):
        """SavingAccount: Should raise InvalidAmountError for negative withdrawal"""
        acc = SavingAccount("Ivan", 100.0)
        with self.assertRaises(InvalidAmountError):
            acc.withdraw(-50.0)


class TestCheckingAccount(unittest.TestCase):
    """Tests for CheckingAccount specific functionality"""

    def test_01_checking_withdraw_valid(self):
        """CheckingAccount: Should withdraw correctly, including $1 fee"""
        acc = CheckingAccount("Judy", 100.0)
        acc.withdraw(50.0)
        # 100 - 50 (amount) - 1 (fee) = 49
        self.assertEqual(acc.balance, 49.0)

    def test_02_checking_withdraw_insufficient_funds(self):
        """CheckingAccount: Should raise InsufficientFundsError correctly"""
        acc = CheckingAccount("Mallory", 50.0)
        # Cannot withdraw 50, because 50 (amount) + 1 (fee) > 50 (balance)
        with self.assertRaises(InsufficientFundsError):
            acc.withdraw(50.0)

    def test_03_checking_withdraw_invalid_amount(self):
        """CheckingAccount: Should raise InvalidAmountError for negative withdrawal"""
        acc = CheckingAccount("Mike", 100.0)
        with self.assertRaises(InvalidAmountError):
            acc.withdraw(-50.0)


class TestBankPersistence(unittest.TestCase):
    """Tests for the Bank class and data persistence"""

    def setUp(self):
        """Create a temporary db file path for each test."""
        self.db_path = "test_bank_data.db"

    def tearDown(self):
        """Clean up the temporary db file after each test."""
        # The shelve module can create multiple files (.bak, .dat, .dir)
        for ext in ['.bak', '.dat', '.dir']:
            if os.path.exists(self.db_path + ext):
                os.remove(self.db_path + ext)

    def test_01_bank_create_accounts(self):
        """Bank: Should create and store different account types"""
        bank = Bank(self.db_path)
        bank.create_account("saving", "Niaj", 100.0)
        bank.create_account("checking", "Olivia", 200.0)

        self.assertIsInstance(bank.get_account("Niaj"), SavingAccount)
        self.assertIsInstance(bank.get_account("Olivia"), CheckingAccount)
        self.assertEqual(bank.get_account("Niaj").balance, 100.0)

    def test_02_bank_get_nonexistent_account(self):
        """Bank: Should return None for a non-existent account"""
        bank = Bank(self.db_path)
        self.assertIsNone(bank.get_account("Peggy"))

    def test_03_bank_save_and_load_data(self):
        """Bank: Should save and load account data correctly"""
        # First bank instance
        bank1 = Bank(self.db_path)
        bank1.create_account("saving", "Quentin", 500.0)
        bank1.get_account("Quentin").deposit(50.0)
        bank1.save_data()

        # Second bank instance, should load the data
        bank2 = Bank(self.db_path)
        bank2.load_data()

        loaded_account = bank2.get_account("Quentin")
        self.assertIsNotNone(loaded_account)
        self.assertIsInstance(loaded_account, SavingAccount)
        self.assertEqual(loaded_account.balance, 550.0)

    def test_04_load_from_nonexistent_file(self):
        """Bank: load_data should handle a non-existent file gracefully"""
        bank = Bank("nonexistent_file.db")
        bank.load_data()  # Should not raise an error
        self.assertEqual(bank.accounts, {})


if __name__ == '__main__':
    print("=====================================")
    print("  RUNNING HOMEWORK 3 UNIT TESTS")
    print("=====================================")
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAccountClasses))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSavingAccount))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCheckingAccount))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBankPersistence))

    runner = CustomTestRunner(verbosity=0)  # Verbosity is handled by our custom class
    result = runner.run(suite)

    print("------------------------------------")
    if result.wasSuccessful():
        print("All tests passed successfully! Great job!")
    else:
        print("Some tests failed. Please review the output above.")

