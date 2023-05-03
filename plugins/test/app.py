import plugin_manager

class Identity(plugin_manager.Plugin):
    """
    This plugin is just the identity function: it returns the argument
    """
    def __init__(self):
        super().__init__()
        self.description = 'test'
        self.version = '1.0.0'

    def main(self, arg,cs,info):
        """
        The actual implementation of the identity plugin is to just return the
        argument
        """
        if "tedd" in arg:
            
            print(info)
        else:
            print("145")