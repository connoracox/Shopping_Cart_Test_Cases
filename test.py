from main import Cart, Shop, Item
import unittest

class ShoppingCartTest(unittest.TestCase):
    def test_add_item(self):
        test_book = Cart()
        test_book.add('Bananas', '4', '15')
        
        # Make sure there is now one and only one contact
        self.assertEqual(len(test_book.items), 1)

        # Make sure the item in the list is actually an item
        self.assertIsInstance(test_book.items['Bananas'], Item)

    def test_item_instantiation(self):
        test_item = Item('Bananas', '4', '15')

        self.assertEqual(test_item.name, 'Bananas')
        self.assertEqual(test_item.quantity, '4')
        self.assertEqual(test_item.price, '15')

    def test_delete_item(self):
        delete_test = Cart()
        delete_test.add('Bananas', '4', '15')
    
        delete_test.delete('Bananas')

        self.assertEqual(len(delete_test.items), 0)

        delete_test.add('Bananas', '4', '15')
        delete_test.add('Eggs', '12', '100')
        delete_test.delete('Bananas')
        
        self.assertEqual(len(delete_test.items), 1)
        self.assertEqual(delete_test.items['Eggs'].name, 'Eggs')

unittest.main()