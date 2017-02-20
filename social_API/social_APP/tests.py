from django.test import TestCase, Client


class GeoEndpointTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/social/geo/")
        self.assertEqual(response.status_code, 200)

    def test_post_request_sends_201(self):
        response = self.c.post("/social/geo/")
        self.assertEqual(response.status_code, 201)


