import unittest
from metaclass import CustomClass


class TestMetaClass(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    # Class atr
    def test_class_atr_old_name_error(self):
        with self.assertRaises(AttributeError):
            CustomClass.x

    def test_class_atr_new_name_ok(self):
        self.assertEqual(CustomClass.custom_x, 50)

    # atr
    def test_atr_old_name_error(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.x

    def test_atr_new_name_ok(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)

    # self
    def test_self_value_old_name_error(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.val

    def test_self_value_new_name_ok(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_val, 99)

    # method
    def test_method_old_name_error(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.line()

    def test_method_new_name_ok(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_line(), 100)

    # str
    def test_str_ok(self):
        inst = CustomClass()
        self.assertEqual(str(inst), "Custom_by_metaclass")

    # non-exist-field
    def test_non_existent_field_error(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.yyy()

    # dynamic
    def test_dynamic_field_old_name_error(self):
        inst = CustomClass()
        inst.dynamic = "added later"
        with self.assertRaises(AttributeError):
            inst.dynamic()

    def test_dynamic_field_new_name_ok(self):
        inst = CustomClass()
        inst.dynamic = "added later"
        self.assertEqual(inst.custom_dynamic, "added later")

    # change value
    def test_change_value_ok(self):
        inst = CustomClass()
        inst.custom_val = 150
        self.assertEqual(inst.custom_val, 150)


if __name__ == "__main__":
    unittest.main()
