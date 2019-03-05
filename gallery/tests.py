from django.test import TestCase
from .models import Location, Category, Image

class ImageTestClass(TestCase):
    def setUp(self):
        self.new_lname=Location(lname="Kisumu")
        self.new_lname.save_location()
        self.new_cname= Category(cname="Sports")
        self.new_cname.save_category()
        self.new_image=Image(id=1 , name="athlete" , description="Record winner" , image_path="media/photos/athelete.jpg" , image_location=self.new_lname , image_category=self.new_cname)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_cname,Category))
        self.assertTrue(isinstance(self.new_lname,Location))

    def test_save_method(self):
        self.new_image.save_image()
        all_the_objects = Image.objects.all()
        self.assertTrue(len(all_the_objects)>0)

    def test_filter_by_location(self):
        self.new_image.save_image()
        get_specific_image = Location.objects.get(lname="Nairobi")
        self.assertTrue(get_specific_image.lname=="Nairobi")
