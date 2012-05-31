# Copyright 2009-2012 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''
Defines `TempValueSetter` and various useful subclasses of it.

See documentation of `TempValueSetter` for more details.
`TempWorkingDirectorySetter` and `TempRecursionLimitSetter` are useful
subclasses of it.
'''

from .temp_value_setter import TempValueSetter
from .temp_working_directory_setter import TempWorkingDirectorySetter
from .temp_recursion_limit_setter import TempRecursionLimitSetter
from .temp_import_hook_setter import TempImportHookSetter