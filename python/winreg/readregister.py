import winreg


## Resolves enum RegType to string
#  @param  t  Type to be resolved
def ResolveType( t ):
    if t == winreg.REG_BINARY:
        return 'REG_BINARY'
    if t == winreg.REG_DWORD:
        return 'REG_DWORD'
    if t == winreg.REG_DWORD_LITTLE_ENDIAN:
        return 'REG_DWORD_LITTLE_ENDIAN'
    if t == winreg.REG_DWORD_BIG_ENDIAN:
        return 'REG_DWORD_BIG_ENDIAN'
    if t == winreg.REG_EXPAND_SZ:
        return 'REG_EXPAND_SZ'
    if t == winreg.REG_LINK:
        return 'REG_LINK'
    if t == winreg.REG_MULTI_SZ:
        return 'REG_MULTI_SZ'
    if t == winreg.REG_NONE:
        return 'REG_NONE'
    if t == winreg.REG_RESOURCE_LIST:
        return 'REG_RESOURCE_LIST'
    if t == winreg.REG_SZ:
        return 'REG_SZ'
    # If nonte, return Unknown
    return 'Unknown type'

# ---------------------------------------------------------------------------- #

# Read all values in HKEY_CURRENT_USER\Console
# (sam is an integer that specifies an access mask that describes the desired security access for the key)
console = winreg.OpenKey( winreg.HKEY_CURRENT_USER, r'Console', sam = winreg.KEY_READ )
try:
    i = 0
    while True:
        try:
            name, value, rType = winreg.EnumValue( console, i )
            print( name, '-', value, f'({rType})' )
            i += 1
        except WindowsError:
            break
finally:
    winreg.CloseKey( console )


# Read one specific value (HKEY_CURRENT_USER\Console\ColorTable01)
# (sam is an integer that specifies an access mask that describes the desired security access for the key)
console = winreg.OpenKey( winreg.HKEY_CURRENT_USER, r'Console', sam = winreg.KEY_READ )
try:
    value, rType = winreg.QueryValueEx( console, 'ColorTable01' )
    resolvedType = ResolveType( rType )
    print( f'The value of ColorTable01 is {value} of type {rType} ({resolvedType}).')
except WindowsError as we:
    print( f'Exception occurred when trying to QueryValue ColorTable01. ({we})' )
finally:
    winreg.CloseKey( console )