#!/usr/bin/env python
__author__= 'juandisay'

import os
from printable import *

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
        self.table()
    def table(self):
        pass#enger

def main():
    menus=['input data','sorting','search']
    print
    print '++++menus++++'
    for num,menu in enumerate(menus):
        print num+1,menu
    print '+++++++++++++'
    try:
        x=input('input choice menus (usage:number 1-3): ')
        if x == 1:
            a=raw_input('name          : ')
            b=raw_input('address [city]: ')
            c=raw_input('phone         : ')
            os.system('clear')
            datainput(a,b,c)
        else:
            print 'please Try input [choice]!'
    except NameError, SyntaxError:
        print 'please usage ordinal not capital!'

if __name__ == '__main__':
    main()
