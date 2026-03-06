import CSP_6_02_reading_files as HW

def test_longest_line():
    assert HW.longestLine("longestfile.txt")=="12345\n"


def test_to_binary():
    assert HW.toBinary("Binarytext.txt")== ["01010110","01001101","00100101","0110"]
