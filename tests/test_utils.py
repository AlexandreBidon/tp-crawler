import unittest
import crawler.utils as utils

class TestUtils(unittest.TestCase):

    def test_flatten(self):
        # GIVEN
        list_a = [[1,2,3],[4,5,6],[7],[8,9]]

        # WHEN
        list_b = utils.flatten(list_a)

        #THEN
        self.assertEqual(
            list_b
            ,[1,2,3,4,5,6,7,8,9]
        )

    def test_url_to_main(self):
        # GIVEN
        url_a = "https://ensai.fr/ceci_est_un_test/page.html"
        url_b = "https://help.twitter.com/test/test/home.html"

        # WHEN
        url_home_a = utils.url_to_main(url_a)
        url_home_b = utils.url_to_main(url_b)

        # THEN
        self.assertEqual(url_home_a, "https://ensai.fr")
        self.assertEqual(url_home_b, "https://help.twitter.com")

if __name__ == '__main__':
    unittest.main()