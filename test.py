'''Importar unittest'''
import unittest

from main import Membership, run

class TestGymMembership(unittest.TestCase):
    '''Class'''
    def test_basic_membership_no_features(self):
        '''Función para test'''
        m = Membership(type='Basic', members=1)
        self.assertEqual(m.calculate_cost(), 50)

    def test_premium_membership_with_features(self):
        '''Función para test'''
        m = Membership(type='Premium', features=['Group Classes', 'Personal Training'], members=1)
        self.assertEqual(m.calculate_cost(), 160)

    def test_family_membership_with_group_discount(self):
        '''Función para test'''
        m = Membership(type='Family', features=['Group Classes'], members=2)
        self.assertEqual(m.calculate_cost(), 162)

    def test_special_discount(self):
        '''Función para test'''
        m = Membership(type='Family', features=['Group Classes', 'Personal Training'], members=2)
        self.assertEqual(m.calculate_cost(), 196)

    def test_premium_features_with_surcharge(self):
        '''Función para test'''
        m = Membership(type='Premium', premium_features=['Exclusive Gym Access'], members=1)
        self.assertEqual(m.calculate_cost(), 196)

if __name__ == "_main_":
    run()
    unittest.main()
