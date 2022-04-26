#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#############################################################################
##
## Copyright (C) 2022 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of the test suite of Qt for Python.
##
## $QT_BEGIN_LICENSE:GPL-EXCEPT$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 as published by the Free Software
## Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

import gc
import os
import sys
import unittest

from pathlib import Path
sys.path.append(os.fspath(Path(__file__).resolve().parents[1]))
from shiboken_paths import init_paths
init_paths()
from smart import Integer, StdSharedPtrTestBench, std


def call_func_on_ptr(ptr):
    ptr.printInteger()


class StdSharedPtrTests(unittest.TestCase):
    def testInteger(self):
        p = StdSharedPtrTestBench.createInteger()
        StdSharedPtrTestBench.printInteger(p)
        self.assertTrue(p)
        call_func_on_ptr(p)

        np = StdSharedPtrTestBench.createNullInteger()
        StdSharedPtrTestBench.printInteger(np)
        self.assertFalse(np)
        self.assertRaises(AttributeError, call_func_on_ptr, np)

        iv = Integer()
        iv.setValue(42)
        np = std.shared_ptr_Integer(iv)
        self.assertEqual(np.value(), 42)

    def testInt(self):
        np = StdSharedPtrTestBench.createNullInt()
        StdSharedPtrTestBench.printInt(np)
        self.assertFalse(np)
        p = StdSharedPtrTestBench.createInt()
        StdSharedPtrTestBench.printInt(p)


if __name__ == '__main__':
    unittest.main()