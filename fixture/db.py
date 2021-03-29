import pymysql.cursors
from model.group import Group
from model.contacts import Contacts

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, mobile, home, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address,email, email2, email3, mobile, home, phone2) = row
                list.append(Contacts(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                            email=email, email2=email2, email3=email3, mobile=mobile,
                                     home=home, phone2=phone2))
        finally:
            cursor.close()
        return list


    def get_contact_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                #list.append(Contacts(id=str(id)) + Group(id=str(group_id)))
                list.append(Group(id=str(group_id)))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()

