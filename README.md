# p4-identify

A tool to detect a currently used Perforce workspace by a current directory (= cwd). Allows to set _**P4CLIENT**_ environment variable based on your location.

## Motivation

**p4** command-line client requires a mandatorily set _**P4CLIENT**_ environment variable for a correct usage. In the case when there are several frequently used Perforce workspaces, such requirement makes the usage of **p4** a bit tedious. There is a way to detect a current workspace automatically.

## The idea

Comparation of roots of workspaces with a current directory allows to find a corresponding workspace.

## Usage as is

_Note_: due to the author's work environment the tool currently has been tested on Windows only. Should work in Linux also.

The following call:
```
p4-identify
```
or
```
p4-identify.cmd
```
leads to the following output.
Either
```
result=unknown workspace
```
in the case of non-workspace directory or:
```
result::workspace::name=thekondor-delivery-dev
result::workspace::root=D:\Projects\delivery-dev
```
in the case of success.

## Usage in wrapper

Standard **p4** command-line **Perforce** client could be wrapped a more convenient tool which setups _**P4CLIENT**_ environment variable first and then delegates all arguments to **p4**. Here is a working sample of such wrapper called **xp4** (= eXtended p4).

E.g.:
```
xp4 edit filename.c
```
will checkout *filename.c* in the current workspace without any tedious pre-setup.

## Setup

The following pre-conditions should be satisfied:

* **p4** available in %PATH%
* set _**P4USER**_ environment variable
* set _**P4PORT**_ environment varialble
* **python** available in %PATH%

## FAQ

### Why so many lines of code?

* POSIX shell and core-utils will allow to make the code shorter and cleaner. Not all of the actual users (= my colleagues) have Cygwin installed;
* The shared source is a part of my another hobby/side project related with Perforce; simple re-use.

## License

MIT License.
