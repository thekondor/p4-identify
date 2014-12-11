@echo off & setlocal enableextensions
@set _prefix=p4-identify::

@rem The MIT License (MIT)
@rem
@rem Copyright (c) 2014 (c) Andrew Sichevoi, http://thekondor.net
@rem
@rem Permission is hereby granted, free of charge, to any person obtaining a copy
@rem of this software and associated documentation files (the "Software"), to deal
@rem in the Software without restriction, including without limitation the rights
@rem to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
@rem copies of the Software, and to permit persons to whom the Software is
@rem furnished to do so, subject to the following conditions:
@rem
@rem The above copyright notice and this permission notice shall be included in
@rem all copies or substantial portions of the Software.
@rem
@rem THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
@rem IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
@rem FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
@rem AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
@rem LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
@rem OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
@rem THE SOFTWARE.

@if "%P4USER%" == "" goto error_missing_p4user

@if "%P4CLIENT%" == "" (
	@for /f "tokens=2 delims=\=" %%i  in ('p4-identify ^| findstr /i "result::workspace::name="') do (
		set P4CLIENT=%%i
	)

	@echo %_prefix%Workspace detected, exported to %%P4CLIENT%%
) else (
	@echo %_prefix%Use explicitly set workspace = %P4CLIENT%
)

goto run_p4

:error_missing_p4user
echo %_prefix%[error] P4USER environment variable must be set, cannot be empty
@exit /b 1

:run_p4
@p4 %*
@exit /b %errorlevel%
