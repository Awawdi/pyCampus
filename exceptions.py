NON_EXISTING_FILE = 'c:\\python\\nofilehere.txt'
EXISTING_FILE = 'c:\\python\\parties.txt'


def get_file_lines(path):
    try:
        print("__CONTENT_START__")
        f = open(path)
    except IOError as ex:
        print("__NO_SUCH_FILE__")
    else:
        print("This is the content from the file!")
        f.close()
    finally:
        print("__CONTENT_END__")


def sneaky(arg1):
    try:
        print("A" + arg1)
        return
    except:
        print("B")
    else:
        print("C")
    finally:
        print("D")


get_file_lines(NON_EXISTING_FILE)
get_file_lines(EXISTING_FILE)
sneaky(0)
