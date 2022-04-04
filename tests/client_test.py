import unittest
from znotify import Client


class TestClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Client.create("zxilly")
        pass

    def test_client_create(self):
        self.assertIsInstance(self.client, Client)
        pass

    def test_client_create_failed(self):
        with self.assertRaises(Exception) as context:
            Client.create("error")
        self.assertTrue("User ID not valid" in str(context.exception))
        pass

    def test_client_send_0(self):
        with self.assertRaises(Exception) as context:
            self.client.send("")
        self.assertTrue("Content is required" in str(context.exception))
        pass

    def test_client_send_1(self):
        self.assertEqual(self.client.send("test"), {
            "content": "test",
            "long": "",
            "title": "Notification"
        })
        pass

    def test_client_send_2(self):
        self.assertEqual(self.client.send("content", "title"), {
            "content": "content",
            "long": "",
            "title": "title"
        })
        pass

    def test_client_send_3(self):
        self.assertEqual(self.client.send("content", "title", "long"), {
            "content": "content",
            "long": "long",
            "title": "title"
        })


if __name__ == "__main__":
    unittest.main()
