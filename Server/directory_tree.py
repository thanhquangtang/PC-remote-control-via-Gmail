import os

def list_directory_tree(startpath, savefile):
    result_file = open(savefile, "a")
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        #print('{}{}/'.format(indent, os.path.basename(root)))
        str_test = '{}{}/'.format(indent, os.path.basename(root)) + '\n'
        result_file.write(str_test)
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            #print('{}{}'.format(subindent, f))
            str_test = '{}{}'.format(subindent, f) + '\n'
            result_file.write(str_test)

    result_file.close()