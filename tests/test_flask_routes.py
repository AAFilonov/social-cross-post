import unittest
from app import flask_app

class Test_Flask_Routes(unittest.TestCase):
    def setUp(self):
        self.ctx = flask_app.app_context()
        self.ctx.push()
        self.client = flask_app.test_client() 
        
    def tearDown(self):
        self.ctx.pop()
                   
    
    def test_ping(self):
        print("Test ping")
        response = self.client.get("/ping")
        assert response.status_code == 200
        self.assertEqual("pong!",response.get_data(as_text=True),msg="Ping failed")
        
if __name__ == "__main__":
    unittest.main()