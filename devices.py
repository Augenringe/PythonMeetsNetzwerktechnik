import json 

class Devices: 

    def __init__(self, simulation: bool, filename: str): 

        self.simulation = simulation 

        self.filename = filename  

        self.device_list = [] # list of dictionaries 

    def __len__(self): 

        return len(self.device_list) 

     

    def load_data(self): 

        """ returns tuple of (Message:str, successful: bool) """ 

        rc: str = "Netzwerkkomponenten erfolgreich aus Datei " + self.filename  + " geladen." 

        rc_ok: bool = True 

        try: 

            with open(self.filename) as file_handle: 

                roh_daten = json.load(file_handle) 

            stub_device_list = roh_daten["devices"] # beseitige die höchste Hierarchiestufe 

            for data in stub_device_list[:]: 

                print(data) 

        except FileNotFoundError: 

            rc ="!!!!!!!!!!!! Fehler: Datei zum Laden der Netzwerkkomponenten wurde nicht gefunden: " + self.filename  + " !!!!!!!!!!!!!!" 

            rc_ok = False 

        return rc, rc_ok 

     

    def get_device_count(self)->int: 

        return len(self.device_list) 

     

    def get_host(self, index:int)->str: 

        if index >= len(self.device_list): 

            return "" 

        return self.device_list[index]["host"] 

    def get_host_name(self, index:int)->str: 

        if index >= len(self.device_list): 

            return "" 

        return self.device_list[index]["hostname"] 

        

    def get_user(self, index:int)->str: 

        if index >= len(self.device_list): 

            return "" 

        return self.device_list[index]["username"] 

    def get_type(self, index:int)->str: 

        if index >= len(self.device_list): 

            return "" 

        return self.device_list[index]["device_type"] 

     

    def get_password(self, index:int)->str: 

        if index >= len(self.device_list): 

            return "" 

        return self.device_list[index]["password"] 

       

    def get_device(self, index: int): 

        """ returns host, hostname, type user, pw in a dictionary""" 

        data = self.device_list[index] 

        return (data) 

    def get_device_data(self, index: int): 

        """ returns host, hostname, type user, pw in a tuple""" 

        data = self.device_list[index] 

        return (data["host"], data["hostname"], data["device_type"], data["username"],["password"]) 

     

    def get_device_data_as_str(self, index: int)-> str: 

        """ returns host, hostname, type (no user/PW) in a string""" 

        data = self.device_list[index] 

        component_string = data["host"] + "/" + data["hostname"] + "/" + data["device_type"]  

        print(component_string) 

         

        return component_string 