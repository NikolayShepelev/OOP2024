import re
import json

class ClientBase:


    def __init__(self, client_id: int = None, name: str = '', phone: str = ''):
        self.client_id = client_id
        self.name = name
        self.phone = phone

    @staticmethod
    def validate_client_id(client_id: int) -> bool:
        return isinstance(client_id, int) and client_id > 0

    @staticmethod
    def validate_name(name: str) -> bool:
        return bool(name and re.match(r"^[a-zA-Zа-яА-ЯёЁ\s-]+$", name))

    @staticmethod
    def validate_phone(phone: str) -> bool:
        pattern = re.compile(r"^8 \(\d{3}\) \d{3}-\d{2}-\d{2}$")
        return bool(phone and pattern.match(phone))

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value: int):
        if not self.validate_client_id(value):
            raise ValueError("Invalid client ID.")
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
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number.")
        self.__phone = value

    @classmethod
    def create_new_client(cls, client_id: int, name: str, phone: str):
        return cls(client_id=client_id, name=name, phone=phone)

    @staticmethod
    def from_string(client_str: str):
        parts = client_str.split(',')
        if len(parts) != 3:
            raise ValueError("The string must contain 3 comma-separated elements.")
        client_id = int(parts[0].strip())
        name, phone = map(str.strip, parts[1:])
        return ClientBase(client_id, name, phone)

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls(
            client_id=data.get('client_id'),
            name=data['name'],
            phone=data['phone']
        )

    def to_json(self) -> str:
        return json.dumps({
            'client_id': self.client_id,
            'name': self.name,
            'phone': self.phone
        }, ensure_ascii=False, indent=4)

    def to_dict(self) -> dict:
        return {
            'client_id': self.client_id,
            'name': self.name,
            'phone': self.phone
        }

    def __str__(self):
        return (f"Client {self.name}, ID: {self.client_id}, Phone: {self.phone}")

    def __eq__(self, other):
        if not isinstance(other, ClientBase):
            return False
        return self.phone == other.phone


class Client(ClientBase):

    def __init__(self, client_id: int = None, name: str = '', ownership_type: str = '',
                 address: str = '', phone: str = ''):
        super().__init__(client_id, name, phone)
        self.ownership_type = ownership_type
        self.address = address

    @staticmethod
    def validate_ownership_type(ownership_type: str) -> bool:
        return bool(ownership_type and re.match(r"^[a-zA-Zа-яА-ЯёЁ\s-]+$", ownership_type))

    @staticmethod
    def validate_address(address: str) -> bool:
        return bool(address and isinstance(address, str))

    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value: str):
        if not self.validate_ownership_type(value):
            raise ValueError("Invalid ownership type.")
        self.__ownership_type = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        if not self.validate_address(value):
            raise ValueError("Invalid address.")
        self.__address = value

    def __str__(self):
        return (f"Client {self.name}, ID: {self.client_id}, Ownership Type: {self.ownership_type}, "
                f"Address: {self.address}, Phone: {self.phone}")

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return (self.client_id == other.client_id and
                self.name == other.name and
                self.phone == other.phone and
                self.ownership_type == other.ownership_type and
                self.address == other.address)

if __name__ == "__main__":
    client = Client(
        client_id=1,
        name="ООО Ромашка",
        ownership_type="ООО",
        address="г. Москва, ул. Ленина, д.10",
        phone="8 (123) 456-78-90",
    )

    print(client)

    client_brief = ClientBrief.from_client(client)
    print(client_brief)