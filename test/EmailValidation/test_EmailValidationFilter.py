import src.ValidatingEmailAddresses.util as util

def test_fun_valid():
    assert util.fun("lara@hackerrank.com") is True
    assert util.fun("brian-23@hackerrank.com") is True
    assert util.fun("britts_54@hackerrank.com") is True


def test_fun_invalid():
    assert util.fun("abc@.com") is False
    assert util.fun("abc@hackerrank.c123") is False
    assert util.fun("abc#123@hackerrank.com") is False
    assert util.fun("abc@hackerrank.comm") is False


def test_filter_mail():
    emails = [
        "abc@hackerrank.com",
        "abc#123@hackerrank.com",
        "john-doe@google.in",
        "xyz@website.comm",
        "user_1@test.org"
    ]

    expected = [
        "abc@hackerrank.com",
        "john-doe@google.in",
        "user_1@test.org"
    ]

    assert util.filter_mail(emails) == expected
