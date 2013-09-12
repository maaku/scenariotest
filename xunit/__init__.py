# -*- coding: utf-8 -*-
# Copyright © 2013 by its contributors. See AUTHORS for details.
# Distributed under the MIT/X11 software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.

import unittest2 as unittest

from scenariotest import *

## Unit of code to test ##

def is_numeric(value_in):
    try:
        float(value_in)
        return True
    except Exception:
        return False

## Test Case ##

class TestIsNumeric(unittest.TestCase):
    __metaclass__ = ScenarioMeta

    class is_numeric_basic(ScenarioTest):
        scenarios = [
            dict(val="1", expected=True),
            dict(val="-1", expected=True),
            dict(val=unicode("123" * 3), expected=True),
            dict(val="Bad String", expected=False),
            dict(val="Speaks Volumes", expected=False)
        ]
        scenarios += [(dict(val=unicode(x), expected=True),
                       "check_unicode_%s" % x) for x in range(-2, 3)]

        def __test__(self, val, expected):
            actual = is_numeric(val)
            if expected:
                self.assertTrue(actual)
            else:
                self.assertFalse(actual)
