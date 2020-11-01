#util file for assignment checking


def check_out(expected, received):
    """checks the received data type against the expected one, and returns True if it matches, False otherwise. checks the contents of the output against the received"""
    if type(expected) == list or type(expected) == tuple:
        if len(expected) == len(received):
            listval=[]
            for a1, b1 in zip(expected, received):
                val=check_out(a1, b1)
                listval.append(val)
            return all(listval)
        else:
            return False

    elif type(expected) == int or type(expected) == str:
        return expected == received

    elif expected is None and received is None:
        return True

    elif expected is None and received is not None:
        return False

def assert_all_tests(expected, received):
    assert(check_out(expected,received)), "Expected value does not match received"
