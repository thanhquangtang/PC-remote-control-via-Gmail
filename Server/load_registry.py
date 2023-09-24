import winreg

def load_registry(registry_hkey, key_path):
    registry_handle = registry_hkey
    key_handle = winreg.OpenKey(registry_handle, key_path)
    values = {}
    try:
        i = 0
        while True:
            name, value, value_type = winreg.EnumValue(key_handle, i)
            if value_type == winreg.REG_BINARY:
                # binary data is returned as bytes, so we convert it to a hex string for readability
                values[name] = value.hex()
            if value_type == winreg.REG_QWORD:
                values[name] = str(value)
            if value_type == winreg.REG_DWORD or value_type == winreg.REG_DWORD_LITTLE_ENDIAN:
                values[name] = str(value)
            if value_type == winreg.REG_MULTI_SZ:
                value_list = []
                try:
                    j = 0
                    while True:
                        value_part = winreg.EnumValue(key_handle, i)[1]
                        if j < len(value_part):
                            v = value_part[j]
                            if isinstance(v, str):
                                value_list.append(v)
                            else:
                                value_list.extend(v)
                        else: 
                            break
                        j += 1
                except WindowsError:
                    pass
                values[name] = value_list
            if value_type == winreg.REG_EXPAND_SZ:
                values[name] = winreg.ExpandEnvironmentStrings(value)
            if value_type == winreg.REG_SZ:
                values[name] = value
            i += 1
    except WindowsError:
        pass
    winreg.CloseKey(key_handle)
    return values





