import wmi

def get_running_processes():
    # Initializing the wmi constructor
    f = wmi.WMI()

    # List to hold the process information
    process_list = []

    # Iterating through all the running processes
    for process in f.Win32_Process():

        # Adding the process information to the list
        process_list.append({
            'id': process.ProcessId,
            'name': process.Name
        })

    # Returning the list of process information
    return process_list
