import os
import unittest

from main import find_bugs


class TestFindBugs(unittest.TestCase):

    def test_default(self):
        self.assertEqual(
            find_bugs('test_files/default/bug.txt', 'test_files/default/landscape.txt'), 3
        )

    def test_corners(self):
        self.assertEqual(
            find_bugs('test_files/corners/bug.txt', 'test_files/corners/landscape.txt'), 4
        )

    def test_full(self):
        self.assertEqual(
            find_bugs('test_files/full/bug.txt', 'test_files/full/landscape.txt'), 1
        )

    def test_overlap(self):
        self.assertEqual(
            find_bugs('test_files/overlap/bug.txt', 'test_files/overlap/landscape.txt'), 4
        )

    def test_spider(self):
        self.assertEqual(
            find_bugs('test_files/spider/bug.txt', 'test_files/spider/landscape.txt'), 3
        )

    def test_worm(self):
        self.assertEqual(
            find_bugs('test_files/worm/bug.txt', 'test_files/worm/landscape.txt'), 3
        )

    def test_mixed_bugs(self):
        self.assertEqual(
            find_bugs('test_files/mixed_bugs/bug.txt', 'test_files/mixed_bugs/landscape.txt'), 2
        )

    def test_noisy(self):
        self.assertEqual(
            find_bugs('test_files/noisy/bug.txt', 'test_files/noisy/landscape.txt'), 2
        )

    def test_partial(self):
        self.assertEqual(
            find_bugs('test_files/partial/bug.txt', 'test_files/partial/landscape.txt'), 0
        )

    def test_empty(self):
        self.assertEqual(
            find_bugs('test_files/empty/bug.txt', 'test_files/empty/landscape.txt'), 0
        )

    def test_large(self):
        large_folder = os.path.join('test_files', 'large')
        if not os.path.exists(large_folder):
            os.mkdir(large_folder)

            # Large landscape
            landscape = open(os.path.join('test_files', 'default', 'landscape.txt'), 'r').read()
            with open(os.path.join(large_folder, 'landscape.txt'), 'w') as new_landscape:
                expand_factor = 1000000
                for idx in range(expand_factor):
                    new_landscape.write(landscape)

            # Same bug
            bug = open(os.path.join('test_files', 'default', 'bug.txt'), 'r').read()
            with open(os.path.join(large_folder, 'bug.txt'), 'w') as new_bug:
                new_bug.write(bug)
        self.assertEqual(
            find_bugs('test_files/large/bug.txt', 'test_files/large/landscape.txt'), 3 * expand_factor
        )

    def test_random_bug(self):
        self.assertEqual(
            find_bugs('test_files/random_bug/bug.txt', 'test_files/random_bug/landscape.txt'), 3
        )


if __name__ == '__main__':
    unittest.main()
