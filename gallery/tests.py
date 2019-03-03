# from django.test import TestCase
# from .models import Location, Category, Image

# class LocationTestClass(TestCase):
#     def setUp(self):
#          self.test_lname=Location(lname="Kisumu")

#     def test_instance(self):
#         self.assertTrue(isinstance(self.test_lname,Location))

# class CategoryTestClass(TestCase):
#     def setUp(self):
#          self.test_cname=Category(cname="travel")

#     def test_instance(self):
#         self.assertTrue(isinstance(self.test_cname,Category))

# class ImageTestClass(TestCase):
#     def setUp(self):
#         self.test_lname=Location(lname="Kisumu")
#         self.test_lname.save()

#         self.test_cname=Category(cname="travel")
#         self.test_cname.save()

#         self.test_image=Image(id=6, name="male.jpg",description="cool_guy",image="image",location=self.test_lname)
#         self.test_image.save()
#         # self.test_image.category.add(self.test_category)

#     def test_save_the_image(self):
#         self.test_image.save_image()
#         images = Image.objects.all()
#         self.assertTrue(len(images) > 0)

