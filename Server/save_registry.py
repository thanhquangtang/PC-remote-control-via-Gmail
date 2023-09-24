import winreg

def save_registry(registry_hkey, parent_key_path, new_key_name, values_dict):
    registry_handle = registry_hkey
    
    # Create the parent key if it doesn't exist
    try:
        parent_key_handle = winreg.OpenKey(registry_handle, parent_key_path)
    except FileNotFoundError:
        parent_key_handle = winreg.CreateKey(registry_handle, parent_key_path)
    
    new_key_handle = winreg.CreateKey(parent_key_handle, new_key_name)
    
    for value_name, value_data in values_dict.items():
        value_type = winreg.REG_SZ  # Default to REG_SZ type
        
        # Check the type of value_data and set the appropriate registry value type
        if isinstance(value_data, int):
            value_type = winreg.REG_DWORD
        elif isinstance(value_data, bytes):
            value_type = winreg.REG_BINARY
        elif isinstance(value_data, list):
            value_type = winreg.REG_MULTI_SZ
        elif isinstance(value_data, str) and "%" in value_data:
            value_type = winreg.REG_EXPAND_SZ
        
        winreg.SetValueEx(new_key_handle, value_name, 0, value_type, value_data)
        
    winreg.CloseKey(new_key_handle)
