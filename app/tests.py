from django.test import TestCase
from app import models 

# Create your tests here.

class TestFriend(TestCase):
    def test_can_create_friend(self):
        friend = models.create_friend(
            "Janet",
            "janet@example.com",
            "1234567890",
            True,
        )

        self.assertEqual(friend.id, 1)
        self.assertEqual(friend.name, "Janet")
        self.assertEqual(friend.email, "janet@example.com")
        self.assertTrue(friend.is_favorite)

    def test_can_view_all_friends_at_once(self):
        friends_data = [
            {
                "name": "Elias",
                "email": "elias.laurila@example.com",
                "phone": "07-854-839",
                "is_favorite": True,
            },
            {
                "name": "Martin",
                "email": "martin.dasilva@example.com",
                "phone": "01-42-13-81-18",
                "is_favorite": False,
            },
            {
                "name": "Alma",
                "email": "alma.johansen@example.com",
                "phone": "15165801",
                "is_favorite": True,
            },
        ]

        for friend_data in friends_data:
            models.create_friend(
                friend_data["name"],
                friend_data["email"],
                friend_data["phone"],
                friend_data["is_favorite"],
            )

        friends = models.all_friends()

        self.assertEqual(len(friends), len(friends_data))

        friends_data = sorted(friends_data, key=lambda c: c["name"])
        friends = sorted(friends, key=lambda c: c.name)

        for data, friend in zip(friends_data, friends):
            self.assertEqual(data["name"], friend.name)
            self.assertEqual(data["email"], friend.email)
            self.assertEqual(data["phone"], friend.phone)
            self.assertEqual(data["is_favorite"], friend.is_favorite)

    def test_can_search_by_name(self):
        friends_data = [
            {
                "name": "Elias",
                "email": "elias.laurila@example.com",
                "phone": "07-854-839",
                "is_favorite": True,
            },
            {
                "name": "Martin",
                "email": "martin.dasilva@example.com",
                "phone": "01-42-13-81-18",
                "is_favorite": False,
            },
            {
                "name": "Alma",
                "email": "alma.johansen@example.com",
                "phone": "15165801",
                "is_favorite": True,
            },
        ]

        for friend_data in friends_data:
            models.create_friend(
                friend_data["name"],
                friend_data["email"],
                friend_data["phone"],
                friend_data["is_favorite"],
            )

        self.assertIsNone(models.find_friend_by_name("aousnth"))

        friend = models.find_friend_by_name("Alma")

        self.assertIsNotNone(friend)
        self.assertEqual(friend.email, "alma.johansen@example.com")

    def test_can_view_favorites(self):
        friends_data = [
            {
                "name": "Elias",
                "email": "elias.laurila@example.com",
                "phone": "07-854-839",
                "is_favorite": True,
            },
            {
                "name": "Martin",
                "email": "martin.dasilva@example.com",
                "phone": "01-42-13-81-18",
                "is_favorite": False,
            },
            {
                "name": "Alma",
                "email": "alma.johansen@example.com",
                "phone": "15165801",
                "is_favorite": True,
            },
        ]

        for friend_data in friends_data:
            models.create_friend(
                friend_data["name"],
                friend_data["email"],
                friend_data["phone"],
                friend_data["is_favorite"],
            )

        self.assertEqual(len(models.favorite_friends()), 2)

    def test_can_update_friends_email(self):
        friends_data = [
            {
                "name": "Elias",
                "email": "elias.laurila@example.com",
                "phone": "07-854-839",
                "is_favorite": True,
            },
            {
                "name": "Martin",
                "email": "martin.dasilva@example.com",
                "phone": "01-42-13-81-18",
                "is_favorite": False,
            },
            {
                "name": "Alma",
                "email": "alma.johansen@example.com",
                "phone": "15165801",
                "is_favorite": True,
            },
        ]

        for friend_data in friends_data:
            models.create_friend(
                friend_data["name"],
                friend_data["email"],
                friend_data["phone"],
                friend_data["is_favorite"],
            )

        models.update_friend_email("Elias", "big.e@example.com")

        self.assertEqual(
            models.find_friend_by_name("Elias").email, "big.e@example.com"
        )

    def test_can_delete_friend(self):
        friends_data = [
            {
                "name": "Elias",
                "email": "elias.laurila@example.com",
                "phone": "07-854-839",
                "is_favorite": True,
            },
            {
                "name": "Martin",
                "email": "martin.dasilva@example.com",
                "phone": "01-42-13-81-18",
                "is_favorite": False,
            },
            {
                "name": "Alma",
                "email": "alma.johansen@example.com",
                "phone": "15165801",
                "is_favorite": True,
            },
        ]

        for friend_data in friends_data:
            models.create_friend(
                friend_data["name"],
                friend_data["email"],
                friend_data["phone"],
                friend_data["is_favorite"],
            )

        models.delete_friend("Martin")

        self.assertEqual(len(models.all_friends()), 2)
