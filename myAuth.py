class MyAuth:
    username = "default"
    email = "default"
    password = "default"

    # public func
    def addingInfo(self, username, email,password):
        self.username = username
        self.email = email
        self.password = password

        self.usernameAuth()
        self.emailAuth()
        self.passwordAuth()

    # private fun
    
    def usernameAuth(self):
        if self.minChar(5, self.username) and self.maxChar(12, self.username):
            print("""Your username was authenticated !!!
Everything is fine.
                  """)
            return 
        else:
            print("""Username authentication failed !!!
Username must have:
min: 5 characters
max: 12 characters
                """)   
            
    
    def emailAuth(self):
        if self.minChar(14, self.email) and self.maxChar(30, self.email) and "@" not in self.email and "." not in self.email :
            print("""Your email was authenticated !!!
Everything is fine.
                  """)
            return    
        else:
            print("""Email authentication failed !!!
Email must have:
min: 14 characters
max: 30 characters
contain: @ and .
                  """)   
            
    
    def passwordAuth(self):
        if self.minChar(8, self.password) and self.maxChar(12, self.password):
            print("""Your password was authenticated !!!
Everything is fine.
                  """)
            return    
        else:
            print("""Password authentication failed !!!
Password must have:
min: 6 characters
max: 12 characters
                  """)   
            

    def minChar(self, num, value):
        if len(value) < num:
            print(f"Value must be min {num} character long")
            return False
        else:
            return True 

    def maxChar(self, num, value):
        if len(value) > num:
            print(f"Value can be max {num} long")
            return False
        else:
            return True
        