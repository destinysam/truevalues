from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import UserModel
from .views import UserView
# Create your tests here.

class UserTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = UserModel(first_name="ahmada",
            last_name="ratherd",
            company_name= "bqed",
            age= 20,
            city= "srinagard",
            state="kashmir",
            pincode= 192233,
            email= "ahmad@gmail.com",
            web= "www.ahmad.com")

    def test_the_get(self):
        
        """This method is getting list of users"""

        request = self.factory.get("http://localhost:8000/api/Users/")
        view = UserView.as_view({'get': 'list'})
        response = view(request)
        self.assertEquals(response.status_code,200)
    def test_the_post(self):    
        
        """This method is used to post user """

        request=self.factory.post("http://localhost:8000/api/Users/",{
            "first_name": "ahmad",
            "last_name": "rather",
            "company_name": "bqe",
            "age": 20,
            "city": "srinagar",
            "state": "kashmir",
            "pincode": 192233,
            "email": "ahmad@gmail.com",
            "web": "www.ahmad.com"
        })
        view = UserView.as_view({'post': 'create'})
        response = view(request)
        self.assertEquals(response.status_code,201)
    def test_the_put(self):
        
        """This method is used update the user"""

        request = self.factory.put("http://localhost:8000/api/Users/",{
            "first_name": "ahmad",
            "last_name": "rather",
            "company_name": "bqe",
            "age": 32,
            "city": "srinagar",
            "state": "kashmir",
            "pincode": 192232,
            "email": "ahmad@gmail.com",
            "web": "www.ahmad.com"
        })
        view = UserView.as_view({'put': 'update'})
        response = view(request,pk="502")
        self.assertEquals(response.status_code,200)
        # self.assertDictEqual(response,data)
    def test_the_delete(self):
        
        """This method is used to delete the user """

        request = self.factory.delete("http://localhost:8000/api/Users/")
        view = UserView.as_view({'delete': 'destroy'})
        response = view(request,pk=self.user.pk)
        self.assertEquals(response.status_code,200)
        # self.assertDictEqual(response,data)
        
