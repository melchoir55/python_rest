from tests.integration.base_case import BaseTestCase
from app.model.user import User
import json


class TestProvider(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.email = 'user@email.com'
        self.new_user = User(email=self.email)
        self.db.session.add(self.new_user)
        self.db.session.commit()

    def test_get_list(self):
        response = self.client.get("/v1/user/", headers=self.headers)
        self.assertEqual(response.status_code, 200, response.data)
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['result'][0]['email'], self.email)

    def test_get_detail(self):
        response = self.client.get(f"/v1/user/{self.new_user.id}/", headers=self.headers)
        self.assertEqual(response.status_code, 200, response.data)
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['result'][0]['email'], self.email)
