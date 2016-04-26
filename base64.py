alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="


def to_bin_repr(s):
    """
    Represent each character of a string into a binary number.
    The result will be in a form of a joint strings
    "aa" -> "11000011100001"
    :param s: The input string
    :return: A binary array
    """
    return ''.join(format(ord(x), '08b') for x in s)


def encode_base64(inp):
    """
    Encode an input string in base64.
    :param inp: The input string
    :return: Encoded base64 string
    """
    # TODO: Optimize the algorithm using binary operations on numbers; skip using strings -> performance gain

    bin_repr = to_bin_repr(inp)
    out = ''

    i = len(bin_repr) % 24
    bin_repr += i * '0'

    for a in xrange(0, len(bin_repr), 6):
        # This is the binary string converted in pair of 6 bits
        pair = bin_repr[a:a+6]
        out += alphabet[int(pair, 2)]

    # If the encoded part has a length multiple by 24 bits / 4 character symbols , so it should have no padding

    if i == 8:
        out = out[:len(out) - 1] + '=='
    if i == 16:
        out = out[:len(out) - 3] + '='
    return out


def test_functions():
    """
    This function is supposed to test the functionality of the functionst provided inside this
     project.
    """

    # Test to_bin_repr()
    assert to_bin_repr('aa')    == '0110000101100001'
    assert to_bin_repr('5')     == '00110101'
    assert to_bin_repr('')      == ''

    # Test encode()
    assert encode_base64('M')                       == 'TQ=='
    assert encode_base64('Ma')                      == 'TWE='
    assert encode_base64('pleasure.') == 'cGxlYXN1cmUu'
    assert encode_base64('any carnal pleas')        == 'YW55IGNhcm5hbCBwbGVhcw=='
    assert encode_base64('any carnal pleasu')       == 'YW55IGNhcm5hbCBwbGVhc3U='
    assert encode_base64('any carnal pleasur')      == 'YW55IGNhcm5hbCBwbGVhc3Vy'
    assert encode_base64('any carnal pleasure')     == 'YW55IGNhcm5hbCBwbGVhc3VyZQ=='
    assert encode_base64('any carnal pleasure.')    == 'YW55IGNhcm5hbCBwbGVhc3VyZS4='
    text = """Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure."""
    encoded_text = """TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="""
    assert encode_base64(text) == encoded_text

    print "Tests: Successful."

test_functions()