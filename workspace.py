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

__all__ = ['fromString', 'fromMultiString']

class Workspace(object):
    class Error(Exception): pass

    def __init__(self, name, root):
        self.__name = name
        self.__root = root

    @property
    def name(self):
        return self.__name

    @property
    def root(self):
        return self.__root

Error = Workspace.Error

def withoutEmptyLines(lines):
	return filter(lambda line: 0 != len(line.strip()), lines)

def withoutSideSpaces(lines):
    return map(lambda line: line.strip(), lines)

def splitByNewLine(line):
    return line.split("\n")

def fromString(clientspecString):
    """Parses P4's raw workspace representation to a property structure."""
    if not clientspecString:
        raise Error("Empty or undefined clientspec string")

    components = clientspecString.split(" ", 5)
    if 6 != len(components):
        raise Error("Clientspec string consists of not expected amount of components, got: {}".format(len(components)))

    if 'Client' != components[0]:
        raise Error("Clientspec string does not have 'Client' component, got: {}".format(components[0]))

    if 'root' != components[3]:
        raise Error("Clientspec string does not have 'root' component, got: {}".format(components[3]))

    return Workspace(name = components[1], root = components[4])

def fromMultiString(clientspecStrings):
    """Parses P4's raw workspaces representation split by \\n to a list of property structures."""
    return map(fromString, withoutEmptyLines(withoutSideSpaces(splitByNewLine(clientspecStrings))))

def identify(path, workspaces):
    if not workspaces:
        return None

    path = path.replace("/", "\\").replace("\\\\", "\\")
    # TODO: ignore case

    candidate, candidateRootLength = None, -1

    for workspace in workspaces:
        if not path.startswith(workspace.root):
            continue

        if (len(workspace.root) > candidateRootLength):
            candidate = workspace
            candidateRootLength = len(workspace.root)

    return candidate
