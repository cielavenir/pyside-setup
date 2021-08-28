#############################################################################
##
## Copyright (C) 2016 The Qt Company Ltd.
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

'''Test cases for qInstallMsgHandler'''

import os
import sys
import unittest

from pathlib import Path
sys.path.append(os.fspath(Path(__file__).resolve().parents[1]))
from init_paths import init_test_paths
init_test_paths(False)

from PySide6.QtCore import (QLibraryInfo, QtCriticalMsg, QtDebugMsg, QtInfoMsg,
                            QMessageLogContext,
                            QtWarningMsg, qCritical, qFormatLogMessage, qDebug,
                            qInstallMessageHandler, qWarning)


param = []


def handler(msgt, ctx, msg):
    global param
    param = [msgt, ctx, msg.strip()]


def handleruseless(msgt, ctx, msg):
    pass


class QInstallMsgHandlerTest(unittest.TestCase):

    def tearDown(self):
        # Ensure that next test will have a clear environment
        qInstallMessageHandler(None)

    def testNone(self):
        ret = qInstallMessageHandler(None)
        self.assertEqual(ret, None)

    @unittest.skipUnless(hasattr(sys, "getrefcount"), f"{sys.implementation.name} has no refcount")
    def testRet(self):
        ret = qInstallMessageHandler(None)
        self.assertEqual(ret, None)
        refcount = sys.getrefcount(handleruseless)
        retNone = qInstallMessageHandler(handleruseless)
        self.assertEqual(sys.getrefcount(handleruseless), refcount + 1)
        rethandler = qInstallMessageHandler(None)
        self.assertEqual(rethandler, handleruseless)
        del rethandler
        self.assertEqual(sys.getrefcount(handleruseless), refcount)

    def testHandler(self):
        rethandler = qInstallMessageHandler(handler)
        if QLibraryInfo.isDebugBuild():
            qDebug("Test Debug")
            self.assertEqual(param[0], QtDebugMsg)
            self.assertEqual(param[2], "Test Debug")
        qWarning("Test Warning")
        self.assertEqual(param[0], QtWarningMsg)
        self.assertEqual(param[2], "Test Warning")
        qCritical("Test Critical")
        self.assertEqual(param[0], QtCriticalMsg)
        self.assertEqual(param[2], "Test Critical")

    def testFormat(self):
        ctx = QMessageLogContext()
        s = qFormatLogMessage(QtInfoMsg, ctx, 'bla')
        self.assertTrue(s)


if __name__ == '__main__':
    unittest.main()

