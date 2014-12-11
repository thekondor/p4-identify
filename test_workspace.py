### The MIT License (MIT)
###
### Copyright (c) 2014 (c) Andrew Sichevoi, http://thekondor.net
###
### Permission is hereby granted, free of charge, to any person obtaining a copy
### of this software and associated documentation files (the "Software"), to deal
### in the Software without restriction, including without limitation the rights
### to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
### copies of the Software, and to permit persons to whom the Software is
### furnished to do so, subject to the following conditions:
###
### The above copyright notice and this permission notice shall be included in
### all copies or substantial portions of the Software.
###
### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
### IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
### FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
### AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
### LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
### OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
### THE SOFTWARE.

import unittest
import workspace as sut

class BrokenInputFromSingleString(unittest.TestCase):
    def test_throws_onEmptyClientspecString(self):
        with self.assertRaisesRegexp(sut.Error, "Empty or undefined clientspec string"):
            sut.fromString("")

    def test_throws_onNoneClientspecString(self):
        with self.assertRaisesRegexp(sut.Error, "Empty or undefined clientspec string"):
            sut.fromString(None)

    def test_throws_onInvalidClientspecComponentsSize(self):
        with self.assertRaisesRegexp(sut.Error, "Clientspec string consists of not expected amount of components, got"):
            sut.fromString(r"Client delivery-project root D:\Projects\delivery")

    def test_throws_onInvalidClientspecComponentsName_wrongRootComponent(self):
        with self.assertRaisesRegexp(sut.Error, "Clientspec string does not have 'root' component, got"):
            sut.fromString(r"Client delivery-project 2014/03/17 loc D:\Projects\delivery ''")

    def test_throws_onInvalidClientspecComponentsName_wrongClientComponent(self):
        with self.assertRaisesRegexp(sut.Error, "Clientspec string does not have 'Client' component, got"):
            sut.fromString(r"Project delivery-project 2014/03/17 root D:\Projects\delivery ''")

class ParsingFromSingleString(unittest.TestCase):
    def test_isCreated_withNonEmptyComment(self):
        workspace = sut.fromString(r"Client delivery-project 2014/03/17 root D:\Projects\delivery 'Created by me.'")
        self.assertEqual(r"delivery-project", workspace.name)
        self.assertEqual(r"D:\Projects\delivery", workspace.root)

    def test_isCreated_withEmptyComment(self):
        workspace = sut.fromString(r"Client delivery-project 2014/03/17 root D:\Projects\delivery ''")
        self.assertEqual(r"delivery-project", workspace.name)
        self.assertEqual(r"D:\Projects\delivery", workspace.root)

class ParsingFromMultiString(unittest.TestCase):
    firstOf = lambda cls, workspaces: workspaces[0]
    secondOf = lambda cls, workspaces: workspaces[1]

    def test_isCreated_withNonEmptyComment(self):
        workspaces = sut.fromMultiString(
        r"""Client delivery-project 2014/03/17 root D:\Projects\delivery 'Created by me.'
        Client delivery-custom 2013/02/18 root D:\Projects\delivery-custom 'Created by crontab.'""")

        self.assertEquals(2, len(workspaces))
        self.assertEquals(r"delivery-project", self.firstOf(workspaces).name)
        self.assertEquals(r"D:\Projects\delivery", self.firstOf(workspaces).root)

        self.assertEquals(r"delivery-custom", self.secondOf(workspaces).name)
        self.assertEquals(r"D:\Projects\delivery-custom", self.secondOf(workspaces).root)


if "__main__" == __name__:
    unittest.run(verbosity = 2)