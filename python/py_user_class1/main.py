class User:
    
    def __init__(self, username, password, account_info):
        """ (User, str, str, str) -> NoneType
        
        Initialize the user with username, password, and account_info.
        
        >>> new_user = User('xyz', 'password1', "Bob's Online Banking")
        >>> new_user.username
        'xyz'
        >>> new_user.password
        'password1'
        >>> new_user.account_info
        "Bob's Online Banking"
        """
        self.username = username
        self.password = password
        self.account_info = account_info
        
    def login(self, entered_password):
        """ (User, str) -> bool
        
        Return True iff the user's password matches entered_password.
        
        >>> new_user = User('xyz', 'password1', "Bob's Online Banking")
        >>> new_user.login('password1')
        True
        >>> new_user.login('1234')
        False
        """
        return self.password == entered_password

    def update_account(self, entered_password, new_info):
        """ (User, str, str) -> NoneType
        
        Modify the user's account_info to be new_info if the user's password
        matches entered_password.
        
        >>> new_user = User('xyz', 'password1', "Bob's Online Banking")
        >>> new_user.update_account('1234', 'B.O.B.')
        >>> new_user.account_info
        "Bob's Online Banking"
        >>> new_user.update_account('password1', 'B.O.B.')
        >>> new_user.account_info
        'B.O.B.'
        """