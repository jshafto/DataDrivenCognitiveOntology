"""Tests for the IO functions from erpsc.core."""

from py.test import raises

from erpsc.core.io import *
from erpsc.count import Count
from erpsc.words import Words
from erpsc.core.errors import InconsistentDataError
from erpsc.tests.utils import TestDB as TDB

##################################################################################
##################################################################################
##################################################################################

def test_save_pickle_obj():
    """Test the save_pickle_obj function."""

    tdb = TDB()

    count_obj = Count()
    words_obj = Words()

    save_pickle_obj(count_obj, 'test', db=tdb)
    save_pickle_obj(words_obj, 'test', db=tdb)

    assert True

    # Test error checking
    with raises(InconsistentDataError):
        save_pickle_obj(['bad dat'], 'test_bad', db=tdb)

def test_load_pickle_obj():
    """Test the load_pickle_obj function."""

    tdb = TDB()

    count_obj = load_pickle_obj('test_counts', db=tdb)
    assert count_obj

    words_obj = load_pickle_obj('test_words', db=tdb)
    assert words_obj

    # Test error checking
    with raises(InconsistentDataError):
        load_pickle_obj('bad_name', db=tdb)
