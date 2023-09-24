import time
from read_mail import *
from send_mail import *
from mac_address import *
from live_screen import *
from logout import *
from shutdown import *
from save_registry import *
from load_registry import *
from app_process import *
from directory_tree import *

if temp_dict['Subject']=="MAC address":
	MACresult=getMACaddress()
	sendMACResult(MACresult)

if temp_dict['Subject']=="Shutdown":
	sendShutdownResult()
	time.sleep(5)
	shutdown()

if temp_dict['Subject']=="Logout":
	sendLogoutResult()
	time.sleep(5)
	logout()

if temp_dict['Subject']=="Livescreen":
	screenshot=getLiveScreen()
	sendLiveScreenResult(screenshot)

if temp_dict['Subject']=="Load registry":
	mail_snippet = temp_dict['Snippet']
	parts = mail_snippet.split(' ')
	registry_hkey_string = parts[0]
	key_path = ' '.join(parts[1:])

	registry_keys = {
    "HKEY_CLASSES_ROOT": winreg.HKEY_CLASSES_ROOT,
    "HKEY_CURRENT_USER": winreg.HKEY_CURRENT_USER,
    "HKEY_LOCAL_MACHINE": winreg.HKEY_LOCAL_MACHINE,
    "HKEY_USERS": winreg.HKEY_USERS,
    "HKEY_CURRENT_CONFIG": winreg.HKEY_CURRENT_CONFIG
	}
	registry_hkey = registry_keys[registry_hkey_string]

	values = load_registry(registry_hkey, key_path)
	sendLoadRegistryResult(values)

if temp_dict['Subject']=="Save registry":
	registry_hkey = winreg.HKEY_CURRENT_USER
	parent_key_path = "Software\MyApplication"
	new_key_name = "Settings"
	values_dict = {
		"Username": "myusername",
		"Password": "mypassword",
		"Port": 1234,
		"ServerList": ["server1", "server2", "server3"],
	}

	save_registry(registry_hkey, parent_key_path, new_key_name, values_dict)
	sendSaveRegistryResult()

if temp_dict['Subject']=="App process":
	process_list=get_running_processes()
	sendAppProcessResult(process_list)

if temp_dict['Subject']=="Directory tree":
	requested_tree = temp_dict['Snippet']
	temp_file = "temp_tree.txt"
	list_directory_tree(requested_tree, temp_file)
	sendDirectoryTreeResult(temp_file)

	


