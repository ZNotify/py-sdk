import unittest
from znotify.send import send


class TestSend(unittest.TestCase):

    def test_send_create_failed(self):
        with self.assertRaises(Exception) as context:
            send("error", "error")
        self.assertTrue("User ID not valid" in str(context.exception))
        pass

    def test_send_0(self):
        with self.assertRaises(Exception) as context:
            send("zxilly", "")
        self.assertTrue("Content is required" in str(context.exception))
        pass

    def test_send_1(self):
        self.assertEqual(send("zxilly", "test"), {
            "content": "test",
            "long": "",
            "title": "Notification"
        })
        pass

    def test_send_2(self):
        self.assertEqual(send("zxilly", "content", "title"), {
            "content": "content",
            "long": "",
            "title": "title"
        })
        pass

    def test_send_3(self):
        self.assertEqual(send("zxilly", "content", "title", "long"), {
            "content": "content",
            "long": "long",
            "title": "title"
        })


if __name__ == "__main__":
    unittest.main()
