import re
import json

class ClientBase:

    def __init__(self, client_id: int = None, name: str = '', ownership_type: str = '', address: str = '', phone: str = ''):
        self.client_id = client_id
        self.name = name
        self.ownership_type = ownership_type
        self.address = address
        self.phone = phone

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value: int):
        if not self.validate_client_id(value):
            raise ValueError("Неподходящий ID")
        self.__client_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not self.validate_name(value):
            raise ValueError("Invalid name.")
        self.__name = value

    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value: str):
        if not self.validate_ownership_type(value):
            raise ValueError("")
        self.__ownership_type = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        if not self.validate_address(value):
            raise ValueError("Invalid address.")
        self.__address = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number.")
        self.__phone = value


# Example usage
if __name__ == "__main__":
    client = ClientBase(
        client_id=1,
        name="ООО Ромашка",
        ownership_type="ООО",
        address="г. Москва, ул. Ленина, д.10",
        phone="8 (123) 456-78-90"
    )

    print(ClientBase.validate_name("wwww"))
