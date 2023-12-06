import unittest
from descriptor import BankAccount


class TestPredictMessageMood(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    # phone_number
    def test_phone_number_not_str_error(self):
        phone_number = 88005553535
        password = "@n1g1l9t0r#"
        balance = 300
        with self.assertRaises(TypeError):
            BankAccount(phone_number, password, balance)

    def test_phone_number_wrong_error(self):
        phone_number = "88005553535"
        password = "@n1g1l9t0r#"
        balance = 300
        with self.assertRaises(ValueError):
            BankAccount(phone_number, password, balance)

    def test_phone_number_ok(self):
        phone_number = "+7(912)215-12-76"
        password = "@n1g1l9t0r#"
        balance = 300
        account = BankAccount(phone_number, password, balance)
        self.assertEqual(account.phone_number, "+7(912)215-12-76")

    # password
    def test_password_short_error(self):
        phone_number = "+7(800)555-35-35"
        password = "1234567"
        balance = 300
        with self.assertRaises(ValueError):
            BankAccount(phone_number, password, balance)

    def test_password_long_error(self):
        phone_number = "+7(800)555-35-35"
        password = "0123456789ABCDEFG"
        balance = 300
        with self.assertRaises(ValueError):
            BankAccount(phone_number, password, balance)

    def test_password_not_str_error(self):
        phone_number = "+7(800)555-35-35"
        password = 123456789
        balance = 300
        with self.assertRaises(TypeError):
            BankAccount(phone_number, password, balance)

    def test_password_without_letters_error(self):
        phone_number = "+7(800)555-35-35"
        password = "123456789!"
        balance = 300
        with self.assertRaises(ValueError):
            BankAccount(phone_number, password, balance)

    def test_password_without_digits_error(self):
        phone_number = "+7(800)555-35-35"
        password = "!TopPassword!"
        balance = 300
        with self.assertRaises(ValueError):
            BankAccount(phone_number, password, balance)

    def test_password_without_symbols_error(self):
        phone_number = "+7(800)555-35-35"
        password = "PasswordNum1"
        balance = 300
        with self.assertRaises(ValueError):
            BankAccount(phone_number, password, balance)

    def test_password_ok(self):
        phone_number = "+7(800)555-35-35"
        password = "Passw0rd!"
        balance = 300
        account = BankAccount(phone_number, password, balance)
        self.assertEqual(account.password, "Passw0rd!")

    # login
    def test_balance_str_error(self):
        phone_number = "+7(800)555-35-35"
        password = "@n1g1l9t0r#"
        balance = "300"
        with self.assertRaises(TypeError):
            BankAccount(phone_number, password, balance)

    def test_balance_negative_error(self):
        phone_number = "+7(800)555-35-35"
        password = "@n1g1l9t0r#"
        balance = -300
        with self.assertRaises(ValueError):
            BankAccount(phone_number, password, balance)

    def test_balance_int_ok(self):
        phone_number = "+7(800)555-35-35"
        password = "@n1g1l9t0r#"
        balance = 300
        account = BankAccount(phone_number, password, balance)
        self.assertEqual(account.balance, 300)

    def test_balance_float_ok(self):
        phone_number = "+7(800)555-35-35"
        password = "@n1g1l9t0r#"
        balance = 299.99
        account = BankAccount(phone_number, password, balance)
        self.assertEqual(account.balance, 299.99)

    def test_balance_zero_ok(self):
        phone_number = "+7(800)555-35-35"
        password = "@n1g1l9t0r#"
        balance = 0
        account = BankAccount(phone_number, password, balance)
        self.assertEqual(account.balance, 0)

    # get None
    def test_login_get_none(self):
        self.assertIsNone(BankAccount.balance)

    def test_password_get_none(self):
        self.assertIsNone(BankAccount.password)

    def test_phone_number_get_none(self):
        self.assertIsNone(BankAccount.phone_number)

    def test_balance_rewrite(self):
        phone_number = "+7(800)555-35-35"
        password = "@n1g1l9t0r#"
        balance = 0
        account = BankAccount(phone_number, password, balance)

        account.balance = 1
        self.assertEqual(account.balance, 1)

        account.password = "@fsakfas16"
        self.assertEqual(account.password, "@fsakfas16")

        account.phone_number = "+7(977)666-13-37"
        self.assertEqual(account.phone_number, "+7(977)666-13-37")

    def test_balance_rewrite_err(self):
        phone_number = "+7(800)555-35-35"
        password = "@n1g1l9t0r#"
        balance = 0
        account = BankAccount(phone_number, password, balance)
        with self.assertRaises(ValueError):
            account.balance = -1
        with self.assertRaises(ValueError):
            account.phone_number = "sumsung"
        with self.assertRaises(ValueError):
            account.password = "qwerty123"

        self.assertEqual(account.balance, 0)
        self.assertEqual(account.phone_number, "+7(800)555-35-35")
        self.assertEqual(account.password, "@n1g1l9t0r#")


if __name__ == "__main__":
    unittest.main()
