import pytest
from main import count_slangwords, tokenise_corpus, put_slangwords_in_list


def test_count_slangwords():
    assert count_slangwords(['test','tree','test']) == [('test', 2), ('tree', 1)]
    assert count_slangwords(['yes', 'yes', 'yes','no']) == [('yes', 3), ('no', 1)]


def test_tokenise_corpus():
    assert tokenise_corpus(['This is a test']) == ['This', 'is', 'a', 'test']
    assert tokenise_corpus(['Yet another sentence']) == ['Yet','another', 'sentence']


def test_put_slangwords_in_list():
    assert put_slangwords_in_list(['this', 'arvo', 'I', 'will', 'sleep'], ['arvo']) == ['arvo']
    assert put_slangwords_in_list(['She', 'holds', 'a', 'stubbie'], ['she', 'stubbie','sun']) == ['she', 'stubbie']





