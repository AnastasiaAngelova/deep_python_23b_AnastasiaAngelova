import unittest
from custom_list import CustomList


def is_custom_list_eq(first, second):
    if len(first) != len(second):
        return False
    for el_first, el_second in zip(first, second):
        if el_first != el_second:
            return False
    return True


class TestCustomList(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    # Custom + Custom
    def test_custom_add_custom_left_low(self):
        cl1 = CustomList([8, 5, -10])
        cl2 = CustomList([-7, 0, 6, 10])
        self.assertEqual(is_custom_list_eq(cl1 + cl2,
                                           CustomList([1, 5, -4, 10])), True)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([8, 5, -10])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-7, 0, 6, 10])), True)

    def test_custom_add_custom_e(self):
        cl1 = CustomList([1, -3, 4])
        cl2 = CustomList([2, 1, -4])
        self.assertEqual(cl1 + cl2,
                         CustomList([3, -2, 0]))
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([1, -3, 4])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([2, 1, -4])), True)

    def test_custom_add_custom_left_more(self):
        cl1 = CustomList([4, -9, -3, 7])
        cl2 = CustomList([3, -2, -1])
        self.assertEqual(cl1 + cl2,
                         CustomList([7, -11, -4, 7]))
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([4, -9, -3, 7])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([3, -2, -1])), True)

    # Custom - Custom
    def test_custom_sub_custom_left_low(self):
        cl1 = CustomList([-5, -8, 6])
        cl2 = CustomList([10, 1, -10, 5])
        self.assertEqual(cl1 - cl2,
                         CustomList([-15, -9, 16, -5]))
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-5, -8, 6])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([10, 1, -10, 5])), True)

    def test_custom_sub_custom_e(self):
        cl1 = CustomList([-10, 0, -10])
        cl2 = CustomList([-5, 3, 3])
        self.assertEqual(cl1 - cl2,
                         CustomList([-5, -3, -13]))
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-10, 0, -10])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-5, 3, 3])), True)

    def test_custom_sub_custom_left_more(self):
        cl1 = CustomList([-4, 9, 1, 6])
        cl2 = CustomList([9, 0, -1])
        self.assertEqual(cl1 - cl2,
                         CustomList([-13, 9, 2, 6]))
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-4, 9, 1, 6])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([9, 0, -1])), True)

    # Custom + list
    def test_custom_add_list_left_low(self):
        cl = CustomList([1, 3, 5])
        usual_list = [5, -6, 1, 2]
        self.assertEqual(cl + usual_list,
                         CustomList([6, -3, 6, 2]))
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([1, 3, 5])), True)
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [5, -6, 1, 2]), True)

    def test_custom_add_list_e(self):
        cl = CustomList([-8, 2, 7])
        usual_list = [10, -9, -2]
        self.assertEqual(cl + usual_list,
                         CustomList([2, -7, 5]))
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([-8, 2, 7])), True)
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [10, -9, -2]), True)

    def test_custom_add_list_left_more(self):
        cl = CustomList([-3, -3, 7, 4])
        usual_list = [-4, 4, 5]
        self.assertEqual(cl + usual_list,
                         CustomList([-7, 1, 12, 4]))
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([-3, -3, 7, 4])), True)
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [-4, 4, 5]), True)

    # Custom - list
    def test_custom_sub_list_left_low(self):
        cl = CustomList([6, -8, 9])
        usual_list = [-9, 5, 4, -10]
        self.assertEqual(cl - usual_list,
                         CustomList([15, -13, 5, 10]))
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([6, -8, 9])), True)
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [-9, 5, 4, -10]), True)

    def test_custom_sub_list_e(self):
        cl = CustomList([-8, 2, 7])
        usual_list = [10, -9, -2]
        self.assertEqual(cl - usual_list,
                         CustomList([-18, 11, 9]))
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([-8, 2, 7])), True)
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [10, -9, -2]), True)

    def test_custom_sub_list_left_more(self):
        cl = CustomList([-3, -3, 7, 4])
        usual_list = [-4, 4, 5]
        self.assertEqual(cl - usual_list,
                         CustomList([1, -7, 2, 4]))
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([-3, -3, 7, 4])), True)
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [-4, 4, 5]), True)

    # list + Custom
    def test_list_add_custom_left_low(self):
        usual_list = [-10, 8, -7]
        cl = CustomList([2, -10, 0, 4])
        self.assertEqual(usual_list + cl,
                         CustomList([-8, -2, -7, 4]))
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [-10, 8, -7]), True)
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([2, -10, 0, 4])), True)

    def test_list_add_custom_e(self):
        usual_list = [8, 0, 2]
        cl = CustomList([-7, -9, -7])
        self.assertEqual(usual_list + cl,
                         CustomList([1, -9, -5]))
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [8, 0, 2]), True)
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([-7, -9, -7])), True)

    def test_list_add_custom_left_more(self):
        usual_list = [9, -10, 6, -10]
        cl = CustomList([7, 1, 6])
        self.assertEqual(usual_list + cl,
                         CustomList([16, -9, 12, -10]))
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [9, -10, 6, -10]), True)
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([7, 1, 6])), True)

    # list - Custom
    def test_list_sub_custom_left_low(self):
        usual_list = [-9, -10, -7]
        cl = CustomList([7, 8, 8, 5])
        self.assertEqual(usual_list - cl,
                         CustomList([-16, -18, -15, -5]))
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [-9, -10, -7]), True)
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([7, 8, 8, 5])), True)

    def test_list_sub_custom_e(self):
        usual_list = [-5, 1, 8]
        cl = CustomList([1, 1, 10])
        self.assertEqual(usual_list - cl,
                         CustomList([-6, 0, -2]))
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [-5, 1, 8]), True)
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([1, 1, 10])), True)

    def test_list_sub_custom_left_more(self):
        usual_list = [10, 9, 4, 8]
        cl = CustomList([1, 4, 5])
        self.assertEqual(usual_list - cl,
                         CustomList([9, 5, -1, 8]))
        self.assertEqual(is_custom_list_eq(usual_list,
                                           [10, 9, 4, 8]), True)
        self.assertEqual(is_custom_list_eq(cl,
                                           CustomList([1, 4, 5])), True)

    # Custom > Custom
    def test_custom_gt_custom_dif_true(self):
        cl1 = CustomList([0, -9, -9])
        cl2 = CustomList([-4, -10, -7])
        self.assertEqual(cl1 > cl2, True)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([0, -9, -9])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-4, -10, -7])), True)

    def test_custom_gt_custom_dif_false(self):
        cl1 = CustomList([-5, -5, -8])
        cl2 = CustomList([9, -10, 5])
        self.assertEqual(cl1 > cl2, False)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-5, -5, -8])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([9, -10, 5])), True)

    def test_custom_gt_custom_e_false(self):
        cl1 = CustomList([-5, -5, -4])
        cl2 = CustomList([-5, -5, -4])
        self.assertEqual(cl1 > cl2, False)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-5, -5, -4])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-5, -5, -4])), True)

    # Custom >= Custom
    def test_custom_ge_custom_dif_true(self):
        cl1 = CustomList([0, -9, -9])
        cl2 = CustomList([-4, -10, -7])
        self.assertEqual(cl1 >= cl2, True)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([0, -9, -9])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-4, -10, -7])), True)

    def test_custom_ge_custom_dif_false(self):
        cl1 = CustomList([-5, -5, -8])
        cl2 = CustomList([9, -10, 5])
        self.assertEqual(cl1 >= cl2, False)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-5, -5, -8])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([9, -10, 5])), True)

    def test_custom_ge_custom_e_false(self):
        cl1 = CustomList([-5, -5, -4])
        cl2 = CustomList([-5, -5, -4])
        self.assertEqual(cl1 >= cl2, True)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-5, -5, -4])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-5, -5, -4])), True)

    # Custom < custom
    def test_custom_lt_custom_dif_true(self):
        cl1 = CustomList([-4, -10, -7])
        cl2 = CustomList([0, -9, -9])
        self.assertEqual(cl1 < cl2, True)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-4, -10, -7])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([0, -9, -9])), True)

    def test_custom_lt_custom_dif_false(self):
        cl1 = CustomList([9, -10, 5])
        cl2 = CustomList([-5, -5, -8])
        self.assertEqual(cl1 < cl2, False)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([9, -10, 5])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-5, -5, -8])), True)

    def test_custom_lt_custom_e_false(self):
        cl1 = CustomList([-5, -5, -4])
        cl2 = CustomList([-5, -5, -4])
        self.assertEqual(cl1 < cl2, False)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-5, -5, -4])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-5, -5, -4])), True)

    # Custom <= custom
    def test_custom_le_custom_dif_true(self):
        cl1 = CustomList([-4, -10, -7])
        cl2 = CustomList([0, -9, -9])
        self.assertEqual(cl1 <= cl2, True)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-4, -10, -7])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([0, -9, -9])), True)

    def test_custom_le_custom_dif_false(self):
        cl1 = CustomList([9, -10, 5])
        cl2 = CustomList([-5, -5, -8])
        self.assertEqual(cl1 <= cl2, False)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([9, -10, 5])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-5, -5, -8])), True)

    def test_custom_le_custom_e_false(self):
        cl1 = CustomList([-5, -5, -4])
        cl2 = CustomList([-5, -5, -4])
        self.assertEqual(cl1 <= cl2, True)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-5, -5, -4])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-5, -5, -4])), True)

    # Custom == custom
    def test_custom_eq_custom_dif_true(self):
        cl1 = CustomList([-5, -5, -4])
        cl2 = CustomList([-8, 0, -6])
        self.assertEqual(cl1 == cl2, True)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-5, -5, -4])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-8, 0, -6])), True)

    def test_custom_eq_custom_dif_false(self):
        cl1 = CustomList([3, 3, 2])
        cl2 = CustomList([4, -9, -9])
        self.assertEqual(cl1 == cl2, False)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([3, 3, 2])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([4, -9, -9])), True)

    def test_custom_eq_custom_e_true(self):
        cl1 = CustomList([-5, -5, -4])
        cl2 = CustomList([-5, -5, -4])
        self.assertEqual(cl1 == cl2, True)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-5, -5, -4])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-5, -5, -4])), True)

    # Custom != custom
    def test_custom_ne_custom_dif_true(self):
        cl1 = CustomList([3, 3, 2])
        cl2 = CustomList([4, -9, -9])
        self.assertEqual(cl1 != cl2, True)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([3, 3, 2])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([4, -9, -9])), True)

    def test_custom_ne_custom_dif_false(self):
        cl1 = CustomList([-5, -5, -4])
        cl2 = CustomList([-8, 0, -6])
        self.assertEqual(cl1 != cl2, False)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-5, -5, -4])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-8, 0, -6])), True)

    def test_customcustomcustom_e_false(self):
        cl1 = CustomList([-5, -5, -4])
        cl2 = CustomList([-5, -5, -4])
        self.assertEqual(cl1 != cl2, False)
        self.assertEqual(is_custom_list_eq(cl1,
                                           CustomList([-5, -5, -4])), True)
        self.assertEqual(is_custom_list_eq(cl2,
                                           CustomList([-5, -5, -4])), True)

    def test_custom_str(self):
        cl = CustomList([-5, 9, -4])
        expected = "-5 9 -4 sum=0"
        self.assertEqual(str(cl), expected)

    def test_custom_str_empty(self):
        cl = CustomList()
        expected = " sum=0"
        self.assertEqual(str(cl), expected)

    def test_custom_str_1_element(self):
        cl = CustomList([5])
        expected = "5 sum=5"
        self.assertEqual(str(cl), expected)


if __name__ == "__main__":
    unittest.main()
