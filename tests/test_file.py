# Third-party Libraries
from unittest import TestCase

# Own's Libraries
from src.filemanagerutil.file import File



class AbspathPropertyTest(TestCase):

    def test_Given_PathInConstructor_When_PathHasTrailingSlash_Then_ReturnFormattedPath(self):
        file_obj = File(
            "file.txt",
            "/Users/datos/"
        )

        self.assertEqual(file_obj.abspath, "/Users/datos/file.txt")

    def test_Given_PathInConstructor_When_IsNone_Then_ReturnRelativePath(self):
        file_obj = File(
            "file.txt"
        )



# "copias.txt"

# "/data/files"
# "/data/files/"

# "/data/files/copias.txt"

# path_obj.parts