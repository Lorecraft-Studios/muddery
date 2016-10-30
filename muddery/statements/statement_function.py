"""
Base statement function.
"""


class StatementFunction(object):
    """
    This is the base statement function class.

    Args:
        args[0]: statement function's args

    Returns:
        return value
    """

    # the function's key
    key = "statement_function"

    # if this function may change the caller's status, const is False
    # only const functions can be used in conditions
    const = False

    def __init__(self):
        self.caller = None
        self.obj = None
        self.args = None

    def set(self, caller, obj, args):
        self.caller = caller
        self.obj = obj
        self.args = args

    def func(self):
        """
        Implement the function.
        """
        pass