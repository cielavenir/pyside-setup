/****************************************************************************
**
** Copyright (C) 2021 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of Qt for Python.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or (at your option) the GNU General
** Public license version 3 or any later version approved by the KDE Free
** Qt Foundation. The licenses are as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-2.0.html and
** https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef PYSIDEUTILS_H
#define PYSIDEUTILS_H

#include <sbkpython.h>

#include <pysidemacros.h>

#include <QtCore/QtGlobal>

QT_FORWARD_DECLARE_CLASS(QString)
QT_FORWARD_DECLARE_CLASS(QStringView)

namespace PySide
{

/// Check if self inherits from class_name
/// \param self Python object
/// \param class_name strict with the class name
/// \return Returns true if self object inherits from class_name, otherwise returns false
PYSIDE_API bool inherits(PyTypeObject *self, const char *class_name);

/// Given A PyObject representing Unicode data, returns an equivalent QString.
PYSIDE_API QString pyUnicodeToQString(PyObject *str);

/// Given a QString, return the PyObject repeesenting Unicode data.
PYSIDE_API PyObject *qStringToPyUnicode(QStringView s);

/// Given A PyObject representing ASCII or Unicode data, returns an equivalent QString.
PYSIDE_API QString pyStringToQString(PyObject *str);

/// Provide an efficient, correct PathLike interface.
PYSIDE_API QString pyPathToQString(PyObject *path);

PYSIDE_API bool isCompiledMethod(PyObject *callback);

} //namespace PySide

#endif // PYSIDESTRING_H