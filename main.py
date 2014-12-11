#!/usr/bin/python

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

import os

import p4client
import workspace

def identifyCurrentWorkspace(user, path):
    try:
        rawWorkspaces = p4client.listClients(user)
        workspaces = workspace.fromMultiString(rawWorkspaces)
        if not workspaces:
            return None

        return workspace.identify(path, workspaces)

    except Exception, e:
        raise Exception("Workspace identification failed <- {}".format(str(e)))

def printWorkspaceIdentification(workspace):
    if not workspace:
        print "result=unknown workspace"
    else:
        print "result::workspace::name={}".format(workspace.name)
        print "result::workspace::root={}".format(workspace.root)

def main():
    user = os.environ.get("P4USER", None)
    if not user:
        raise Exception("%P4USER% environment variable is not set.")

    cwd = os.getcwd()
    workspace = identifyCurrentWorkspace(user, cwd)
    printWorkspaceIdentification(workspace)

if "__main__" == __name__:
    # print "[p4-identify], bug reports to Andrew Sichevoi <http://thekondor.net>"
    isDebugMode = os.environ.get("P4_IDENTIFY_DEBUG", None)
    try:
        main()
    except Exception, e:
        print "[Error]", str(e)
        if isDebugMode:
            raise
