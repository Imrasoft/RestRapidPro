from django.test import TestCase
from django.core.urlresolvers import reverse
from apprest.models import Group

class ContactsInGroupTest(TestCase):
    def creating_groups(self, group_name="test group", number_of_contacts=1):
        Group.object.create(name=group_name, contacts=number_of_contacts)

    def test_creating_groups(self):
        group1= self.creating_groups()
        self.assertEqual()

        
        
#STILL WORKING ON THIS        
