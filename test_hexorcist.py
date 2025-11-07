from functs import *
import pytest

def test_base_out_of_range():
    assert to_decimal("111", 1) == "range"
    assert to_decimal("111", 55) == "range"

def test_to_decimal_base2():
    assert to_decimal("101", 2) == 5

def test_to_decimal_base3():
    assert to_decimal("12", 3) == 5

def test_to_decimal_base4():
    assert to_decimal("11", 4) == 5

def test_to_decimal_base5():
    assert to_decimal("10", 5) == 5

def test_to_decimal_base6():
    assert to_decimal("145", 6) == 65

def test_to_decimal_base7():
    assert to_decimal("33", 7) == 24

def test_to_decimal_base8():
    assert to_decimal("67", 8) == 55

def test_to_decimal_base9():
    assert to_decimal("65", 9) == 59

def test_to_decimal_base10():
    assert to_decimal("5", 10) == 5

def test_to_decimal_base11():
    assert to_decimal("4A", 11) == 54
    assert to_decimal("4a", 11) == 54

def test_to_decimal_base12():
    assert to_decimal("63", 12) == 75

def test_to_decimal_base13():
    assert to_decimal("274", 13) == 433

def test_to_decimal_base14():
    assert to_decimal("2B8", 14) == 554
    assert to_decimal("2b8", 14) == 554

def test_to_decimal_base15():
    assert to_decimal("400D", 15) == 13513
    assert to_decimal("400d", 15) == 13513

def test_to_decimal_base16():
    assert to_decimal("4D2", 16) == 1234
    assert to_decimal("4d2", 16) == 1234

def test_to_decimal_base17():
    assert to_decimal("800", 17) == 2312

def test_to_decimal_base18():
    assert to_decimal("A5F", 18) == 3345
    assert to_decimal("a5f", 18) == 3345

def test_to_decimal_base19():
    assert to_decimal("B64II", 19) == 1476489
    assert to_decimal("b64ii", 19) == 1476489

def test_to_decimal_base20():
    assert to_decimal("1BGD7", 20) == 254667
    assert to_decimal("1bgd7", 20) == 254667

def test_to_decimal_base21():
    assert to_decimal("388G", 21) == 31495
    assert to_decimal("388g", 21) == 31495
   
def test_to_decimal_base22():
    assert to_decimal("3D09", 22) == 38245
    assert to_decimal("3d09", 22) == 38245

def test_to_decimal_base23():
    assert to_decimal("15AC5", 23) == 346247
    assert to_decimal("15ac5", 23) == 346247

def test_to_decimal_base24():
    assert to_decimal("3215", 24) == 42653

def test_to_decimal_base25():
    assert to_decimal("G8MJK", 25) == 6389245
    assert to_decimal("g8mjk", 25) == 6389245

def test_to_decimal_base26():
    assert to_decimal("3IOF", 26) == 65535
    assert to_decimal("3iof", 26) == 65535

def test_to_decimal_base27():
    assert to_decimal("4CG", 27) == 3256
    assert to_decimal("4cg", 27) == 3256

def test_to_decimal_base28():
    assert to_decimal("5QP", 28) == 4673
    assert to_decimal("5qp", 28) == 4673

def test_to_decimal_base29():
    assert to_decimal("3F0", 29) == 2958
    assert to_decimal("3f0", 29) == 2958

def test_to_decimal_base30():
    assert to_decimal("3FL4", 30) == 95134
    assert to_decimal("3fl4", 30) == 95134

def test_to_decimal_base31():
    assert to_decimal("U0H9", 31) == 894266
    assert to_decimal("u0h9", 31) == 894266

def test_to_decimal_base32():
    assert to_decimal("UH0H", 32) == 1000465
    assert to_decimal("uh0h", 32) == 1000465

def test_to_decimal_base33():
    assert to_decimal("2T2A1", 33) == 3416524
    assert to_decimal("2t2a1", 33) == 3416524

def test_to_decimal_base34():
    assert to_decimal("1BLD", 34) == 52747
    assert to_decimal("1bld", 34) == 52747

def test_to_decimal_base35():
    assert to_decimal("moss", 35) == 973658
    assert to_decimal("MOSS", 35) == 973658

def test_to_decimal_base36():
    assert to_decimal("I6TK9", 36) == 30551337
    assert to_decimal("i6tk9", 36) == 30551337

def test_invalid():
    assert to_decimal("$$", 10) == "no"