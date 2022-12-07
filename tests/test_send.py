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
        ret = send("test", "test")
        self.assertEqual(ret, ret | {
            "content": "test",
            "long": "",
            "title": "Notification"
        })
        pass

    def test_send_2(self):
        ret = send("test", "content", "title")
        self.assertEqual(ret, ret | {
            "content": "content",
            "long": "",
            "title": "title"
        })
        pass

    def test_send_3(self):
        ret = send("test", "content", "title", "long")
        self.assertEqual(ret, ret | {
            "content": "content",
            "long": "long",
            "title": "title"
        })
        pass


if __name__ == "__main__":
    unittest.main()
