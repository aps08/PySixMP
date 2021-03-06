import Constants as C

class FileOperations:
    """This class is responsibel for all the fileoperation which happend in the Password Manager Prorgam. 
    """
    def __init__(self) -> None:
        """ __init__() --> This is a constructor which is responsible for creating some initial member veriables
                            and running the write_key function.
        """ 
        self.PATH = C.FILE_PATH
        self.KEY_PATH = C.SECRET_KEY_PATH
        self.create_key()
        
    def create_key(self):
        """ create_key() -> This function is repsonsible for creating the secret key file to store
                            the value generated by the fernet object, if the file doesn't exists.
                            otherwise read the secret key from the file. 
                            if also runs the create_json_file function.
        """
        if not C.os.path.exists(self.KEY_PATH):
            self.key = C.Fernet.generate_key()
            with open(self.KEY_PATH, mode="wb") as WriteFile:
                WriteFile.write(self.key)
                WriteFile.close()
        else:
            with open(self.KEY_PATH, mode="rb") as ReadFile:
                self.key = ReadFile.read()
                ReadFile.close()
        self.F = C.Fernet(self.key)
        self.create_json_file()
                
    def create_json_file(self):
        """create_json_file() --> This function is repsonsible for creating the json file,
                                if it doesn't exists at the location.
        """
        if not C.os.path.exists(self.PATH):
            with open(C.FILE_PATH, mode="w") as newfile:
                password = self.encrypt_data("defaultpassword")
                data = {
                        "defaultdomain.com": {
                        "email": C.DEFAULT_EMAIL,
                        "password": password
                        }}
                C.json.dump(data, newfile, indent=3)
                newfile.close()
            
                
    def search_data(self, website: str) -> C.Union[ bool , str] :
        """ search_data() --> This function is repsonsible for searching data from the json file.

        Args:
            website (str): stores website name

        Returns:
            C.Union[ bool , str]: return True with data if website exsits in the json file. 
        """
        with open(self.PATH, mode="r") as ReadFile:
            data = C.json.load(ReadFile)
            try:
                Exists, email, password = True, data[website]["email"], data[website]["password"]
            except:
                Exists, email, password = False, "",""
            ReadFile.close()
            password = self.decrypt_data(password)
            return Exists, email, password
            
    def already_exists(self, website: str) -> C.Union[bool, dict]:
        """ already_exists() --> This function is repsonsible for checking if the website name already exists in the 
                                json file or not.

        Args:
            website (str): stores website name

        Returns:
            C.Union[bool, dict]: return True if json has the website already otherwise False, together with json data.
        """
        with open(self.PATH, mode="r") as ReadFile:
            data = C.json.load(ReadFile)
            ReadFile.close()
            return (True if website in data.keys() else False), data
                
    def save_data(self, website: str, email: str, password: str ) -> bool:
        """ save_data() --> This function is responsible for saving the data entered by the user.

        Args:
            website (str): stores website name
            email (str): stores user email
            password (str): stores password for the website.

        Returns:
            bool: returns False if website already exists in the json file, otherwise writes data to json and returns True 
        """
        user_data = { website : {
                    "email": email,
                    "password": self.encrypt_data(password)
                }}
        key_exist, existing_data = self.already_exists(website)
        if key_exist:
           return False
        else:
            self.write_data(existing_data, user_data)
            return True
    
    def write_data(self, existing_data: dict, user_data: dict) -> None:
        """ write_data() --> This function is responsible for adding data to the json file, which
                            stored user information. The password in the json is always encrypted.  

        Args:
            existing_data (dict): stores previously stored data.
            user_data (dict): stores ew data which need to be appended.
        """
        existing_data.update(user_data)
        with open(C.FILE_PATH, mode="w") as WriteFile:
             C.json.dump(existing_data, WriteFile, indent=3)
             WriteFile.close()
             
    def encrypt_data(self, string: str) -> str:
        """ encrypt_data() --> This function is responsible encrpting the plain text.

        Args:
            string (str): stores plain text password

        Returns:
            str: return encrypted password as string.
        """
        encrypted_data = self.F.encrypt(bytes(string, encoding='utf-8'))
        return encrypted_data.decode('utf-8')
    
    def decrypt_data(self, string: str) -> str:
        """ decrypt_data() --> This function is responsible for decrypting the encrypted password.

        Args:
            string (str): stores encrypted password as string.

        Returns:
            str: return password as string/plain text.
        """
        decrypted_data = self.F.decrypt(bytes(string, encoding='utf-8'))
        return str(decrypted_data)