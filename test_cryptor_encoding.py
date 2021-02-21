import rot13_encode
import rot47_encode


def test_rot13_will_it_encode_given_word_kacper_to_xnpcre_correct():
    assert rot13_encode.ROT13().encode_rot13(test=True, test_word='kacper') == 'xnpcre'


def test_rot13_will_it_encode_given_word_github_to_tvguho_correct():
    assert rot13_encode.ROT13().encode_rot13(test=True, test_word='github') == 'tvguho'


def test_rot47_will_it_encode_given_word_test_to_e6d6_correct():
    assert rot47_encode.ROT47().encode_rot47(characters_from_user='test', is_encrypted=None, tests=True) == 'E6DE'


def test_rot47_will_it_encode_given_word_chess_to_496dd_correct():
    assert rot47_encode.ROT47().encode_rot47(characters_from_user='chess', is_encrypted=None, tests=True) == '496DD'
