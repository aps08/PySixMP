import Constants as C

class FileOperations:
    def __init__(self) -> None:
        self.PATH = C.FILE_PATH
        self.KEY_PATH = C.SECRET_KEY_PATH
        self.create_key()
        
    def create_key(self):
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
        with open(self.PATH, mode="r") as ReadFile:
            data = C.json.load(ReadFile)
            ReadFile.close()
            return (True if website in data.keys() else False), data
                
    def save_data(self, website: str, email: str, password: str ) -> bool:
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
        existing_data.update(user_data)
        with open(C.FILE_PATH, mode="w") as WriteFile:
             C.json.dump(existing_data, WriteFile, indent=3)
             WriteFile.close()
             
    def encrypt_data(self, string: str) -> str:
        encrypted_data = self.F.encrypt(bytes(string, encoding='utf-8'))
        return str(encrypted_data)
    
    def decrypt_data(self, string: bytes) -> str:
        decrypted_data = self.F.decrypt(bytes(string, encoding='utf-8'))
        return str(decrypted_data)