import unittest

def replace_GvR(line):
    if not isinstance(line, str):
        raise TypeError("Invalid parameter!")
    line = line.split()
    prepare_result_string = []
    for word in line:
        prepare_result_string.append(word.replace("GvR", "Guido van Rossum"))
    return " ".join(prepare_result_string)

class TestReplaceGvR(unittest.TestCase):
    def test_upper_GVR(self):
        self.assertEqual(replace_GvR("..aaGVRbb.."), ("..aaGVRbb.."))

    def test_lower_gvr(self):
        self.assertEqual(replace_GvR("aa gvr bb"), ("aa gvr bb"))

    def test_GvR(self):
        self.assertEqual(replace_GvR("Only GvR here!"), ("Only Guido van Rossum here!"))
        self.assertEqual(replace_GvR("Not onlyGvRhere!"), ("Not onlyGuido van Rossumhere!"))

    def test_incorrect_data(self):
        with self.assertRaises(TypeError):
            replace_GvR(587)


if __name__ == "__main__":
    unittest.main()