# import unittest

# from my_lambdata.assignment_w_inherit import MyFrame

# class InheritTest(unittest.TestCase):
#     def test_construct(self):
#         my_frame = MyFrame({"abbrevs": ["CA", "CO", "CT", "DC", "TX"]})
#         self.assertTrue(isinstance(my_frame, MyFrame))
#     def test_add_state_names(self):
#         my_frame = MyFrame({"abbrevs": ["CA", "CO", "CT", "DC", "TX"]})
#         # test there is no state_name col
#         cols = my_frame.columns.tolist()
#         self.assertIn("abbrevs", cols)
#         self.assertNotIn("state_name", cols)
#         # test that our function added the proper column
#         my_frame.add_state_names()
#         cols = my_frame.columns.tolist()
#         self.assertIn("state_name", cols)
# if __name__ == '__main__':
#     unittest.main()