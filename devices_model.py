import json

def load_data(self)->str:
    rc: str = "Komponentendatei erfolgreich geladen."
    try:
        with open(self.filename) as file_handle:
            roh_daten = json.load(file_handle)
        self.device_list = roh_daten["devices"] # beseitige die höchste Hierarchiestufe
        print("Geräteliste gelesen:")
        for data in self.device_list:
            print(data)
    except FileNotFoundError:
        rc ="!!!!!!!!!!!! Fehler: Datei zum Laden der Netzwerkkomponenten wurde nicht gefunden: " + self.filename  + " !!!!!!!!!!!!!!"
    return rc

def get_device_count(self)->int:
    return len(self.device_list)

def get_host(self, index:int)->str:
    return self.device_list[index]["host"]

def get_host_name(self, index:int)->str:
    return self.device_list[index]["hostname"]

def get_user(self, index:int)->str:
    return self.device_list[index]["username"]

def get_type(self, index:int)->str:
    return self.device_list[index]["device_type"]