import unittest
from parameters import Parameters


class TestParameters(unittest.TestCase):
    def test_print_params(self):
        of = 'delme_test/'
        P = Parameters(output_folder=of)
        for k, v in P.items():
            self.assertTrue(P[k] == v)
        # TODO: cleanup, delete everything created by the tests of, maybe in constructor?

    def test_load_parameters(self):
        pass


if __name__ == '__main__':
    unittest.main()
