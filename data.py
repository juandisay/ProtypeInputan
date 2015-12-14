#!/usr/bin/env python

class datainput:
    _name = []
    _address = []
    _phone = []
    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone
        self._ngelist()
    def _ngelist(self):
        self._name.append(self.name)
        self._address.append(self.address)
        self._phone.append(self.phone)
        self.update_data()
    def update_data(self):
        if self._name == self._address and self.phone:
            self._name.append(self.name)
            self._address.append(self.address)
            self._phone.append(self.phone)
        self.unpack()
    def unpack(self):
        pass
            
if __name__ == '__main__':
    while True:
        input_name=raw_input('input name: ')
        input_address=raw_input('input address: ')
        input_phone=raw_input('input phone: ')
        datainput(input_name,input_address,input_phone)
