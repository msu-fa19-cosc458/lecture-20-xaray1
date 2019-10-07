import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("!! add 2 2")
        print(response)
        self.assertEquals(response,22)

if __name__ == '__main__':
    unittest.main()