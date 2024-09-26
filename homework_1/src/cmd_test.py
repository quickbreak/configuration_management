import unittest
from Cmd import Cmd
import zipfile


class MyTestCase(unittest.TestCase):

    def test_ls_ok(self):
        with zipfile.ZipFile("archive_test.zip", 'r') as arch:
            manipulator = Cmd(arch)
            self.assertEqual(manipulator.ls('/folder2'), ['file4.txt', 'subfolder4'])  # add assertion here

    def test_ls_fail(self):
        with zipfile.ZipFile("archive_test.zip", 'r') as arch:
            manipulator = Cmd(arch)
            self.assertEqual(manipulator.ls('/abracadabra2'), 1)

    def test_ls_empty(self):
        with zipfile.ZipFile("archive_test.zip", 'r') as arch:
            manipulator = Cmd(arch)
            self.assertEqual(manipulator.ls('/folder3/subfolder5'), [])

    def test_cd(self):
        with zipfile.ZipFile("archive_test.zip", 'r') as arch:
            manipulator = Cmd(arch)
            self.assertEqual(manipulator.cd('.'), 0)
            self.assertEqual(manipulator.cd('./folder1/subfolder1'), 0)
            self.assertEqual(manipulator.cd('/'), 0)
            self.assertEqual(manipulator.cd('abracadabra'), 1)

    def test_wc(self):
        with zipfile.ZipFile("archive_test.zip", 'r') as arch:
            manipulator = Cmd(arch)
            self.assertEqual(manipulator.wc('/folder2/file4.txt'), [2, 2, 8])

    def test_find(self):
        with zipfile.ZipFile("archive_test.zip", 'r') as arch:
            manipulator = Cmd(arch)
            self.assertEqual(manipulator.find('/folder1/subfolder1', '.txt'),
                             ['/folder1/subfolder1/file1.txt',
                              '/folder1/subfolder1/file2.txt',
                              '/folder1/subfolder1/file3.txt'])
            self.assertEqual(manipulator.find('/folder2', '.txt'),
                             ['/folder2/file4.txt'])
            self.assertEqual(manipulator.find('/ .svg'), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
