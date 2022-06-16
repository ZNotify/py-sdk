import unittest
from znotify import Client


class TestClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Client.create("test")
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
        ret = self.client.send("test")
        self.assertEqual(ret, ret | {
            "content": "test",
            "long": "",
            "title": "Notification"
        })
        pass

    def test_client_send_2(self):
        ret = self.client.send("content", "title")
        self.assertEqual(ret, ret | {
            "content": "content",
            "long": "",
            "title": "title"
        })
        pass

    def test_client_send_3(self):
        ret = self.client.send("content", "title", "long")
        self.assertEqual(ret, ret | {
            "content": "content",
            "long": "long",
            "title": "title"
        })


if __name__ == "__main__":
    unittest.main()
