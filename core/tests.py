import unittest

from django.http import HttpResponse
from django.test import TestCase
from django.urls import resolve, reverse

from .views import AboutView, FeedbackCreateView, HomeView, ShopView


# comman
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse("core:home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class AboutTests(TestCase):
    def test_about_view_status_code(self):
        url = reverse("core:about")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @classmethod
    def create(cls):
        
        print("setUpTestData")

    def about_test_method(self):
       
        print("test_my_first_method")
        self.assertTrue(True)


class FeedbackCreateTest(TestCase):
    def test_Feedbackcreate_view_status_code(self):
        url = reverse("core:feedback_create")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @classmethod
    def feedback_create_method(self):
        print("feedback_create")
        self.assertTrue(True)


class ShopTest(TestCase):
    def test_FeedbackCreate_view_status_code(self):
        url = reverse("core:shop")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


# user
class ProfileCreateTest(TestCase):
    def test_ProfileCreate_view_status_code(self):
        url = reverse("core:profile_create")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    @classmethod
    def profile_create(cls):
        print("profile_create")


class ProfileDetailTest(TestCase):
    def test_ProfileDetail_view_status_code(self):
        url = reverse("core:profile_update", kwargs={"pk": 0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


class ProfileUpdateTest(TestCase):
    def test_ProfileUpdate_view_status_code(self):
        url = reverse("core:profile_detail", kwargs={"pk": 0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def profile_update(self):
        print("profile_update")
        self.assertTrue(True)


class AddressCreateTest(TestCase):
    def test_AddressCreate_view_status_code(self):
        url = reverse("core:address_create", kwargs={"pk": 0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    @classmethod
    def address_create(cls):
        print("address_create")

    def address_update(self):
        print("address_update")
        self.assertTrue(True)


class DashboardViewTest(TestCase):
    def test_DashboardView_view_status_code(self):
        url = reverse("core:dashboard")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


# Registration
class RegistrationTest(TestCase):
    def test_RegistrationView_view_status_code(self):
        url = reverse("core:signup")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @classmethod
    def registration_done(cls):

        print("registration_done")


class LoginTest(TestCase):
    def test_LoginView_view_status_code(self):
        url = reverse("core:login")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class LogoutTest(TestCase):
    def test_LogoutView_view_status_code(self):
        url = reverse("core:logout")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


class PasswordResetTest(TestCase):
    def test_PasswordReset_view_status_code(self):
        url = reverse("core:password_reset")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class PasswordResetDoneTest(TestCase):
    def test_PasswordResetDone_view_status_code(self):
        url = reverse("core:password_reset_done")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


"""class PasswordResetConfirmTest(TestCase):
    def test_PasswordResetDoneV_view_status_code(self):
        url = reverse('core:password_reset_confirm', kwargs={"pk":1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)"""

# product


class ProductCreateTest(TestCase):
    def test_ProductCreate_view_status_code(self):
        url = reverse("core:product_create")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


class ProductListTest(TestCase):
    def test_ProductList_view_status_code(self):
        url = reverse("core:product_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @classmethod
    def product_add(cls):
        print("product_add")

    def product_update(self):
        print("product_update")

    def product_delete(self):
        print("product_delete")
        self.assertTrue(True)


class ProductDetailTest(TestCase):
    def test_ProductDetail_view_status_code(self):
        url = reverse("core:product_detail", kwargs={"pk": 0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)


class CategoryListTest(TestCase):
    def test_CategoryList_view_status_code(self):
        url = reverse("core:category_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class ProductListByCategoryTest(TestCase):
    def test_ProductListByCategory_view_status_code(self):
        url = reverse("core:product_by_category", kwargs={"pk": 0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @classmethod
    def product_add_by_catrgory(cls):
        print("product_add_by_catrgory")

    def product_update_by_catrgory(self):
        print("product_update_by_catrgory")

    def product_delete_by_catrgory(self):
        print("product_delete_by_catrgory")
        self.assertTrue(True)


class ProductReviewAdd(TestCase):
    def test_ProductReview_view_status_code(self):
        url = reverse("core:add_product_review", kwargs={"pk": 0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    @classmethod
    def Product_Review_Add(cls):
        print("Product_Review_Add")

    def Product_Review_update(self):
        print("Product_Review_update")

    def Product_Review_delete(self):
        print("Product_Review_delete")
        self.assertTrue(True)


# cart
"""class CartTest(TestCase):
    def test_Cart_view_status_code(self):
        url = reverse('core:cart', kwargs={"pk":0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)"""


class AddToCartTest(TestCase):
    def test_AddToCart_view_status_code(self):
        url = reverse("core:cart_add", kwargs={"pk": 0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    @classmethod
    def add_cart(cls):
        print("add_cart")


class CheckoutTest(TestCase):
    def test_Checkout_view_status_code(self):
        url = reverse("core:checkout")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


# order
class OrderTest(TestCase):
    def test_Order_view_status_code(self):
        url = reverse("core:order")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    @classmethod
    def order(cls):
        print("order")


class OrderDetailTest(TestCase):
    def test_OrderDetail_view_status_code(self):
        url = reverse("core:order_detail", kwargs={"pk": 0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


class OrderHistoryTest(TestCase):
    def test_OrderHistory_view_status_code(self):
        url = reverse(
            "core:order_history",
        )
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


# wishlist

"""class WishlistListTest(TestCase):
    def test_WishlistList_view_status_code(self):
        url = reverse('core:wishlist_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)"""


class WishlistCreateTest(TestCase):
    def test_WishlistCreate_view_status_code(self):
        url = reverse("core:wishlist_create")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @classmethod
    def create(cls):
        print("setUpTestData")

    def setUp(self):
        print("setUp")

    def test_my_first_method(self):
        print("test_my_first_method")
        self.assertTrue(True)


class WishlistDetailTest(TestCase):
    def test_WishlistDetail_view_status_code(self):
        url = reverse("core:wishlist_detail", kwargs={"pk": 0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)


"""class AddToWishlistTest(TestCase):
    def test_AddToWishlistl_view_status_code(self):
        url = reverse('core:add_to_wishlist', kwargs={"pk":0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)


class AddToWishlistTest(TestCase):
    def test_removeToWishlistl_view_status_code(self):
        url = reverse('core:remove_from_wishlist', kwargs={"pk":0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)"""


class PaymentTest(TestCase):
    def test_Payment_view_status_code(self):
        url = reverse("core:payment")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    @classmethod
    def payment_done(cls):
        print("payment_done")


class PaymentListTest(TestCase):
    def test_PaymentList_view_status_code(self):
        url = reverse("core:payment_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


class payment_handlerTest(TestCase):
    def test_payment_handler_view_status_code(self):
        url = reverse("core:payment_handler")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
