from unittest import TestCase, mock

from segment.http_client_practice import ExchangeRateClient


class TestExchangeRateClient(TestCase):

    @mock.patch(segment.http_client_practice.ExchangeRateClient.requests.get,"")
    def test_get_rate(self):
        date = "2017-01-02"
        base = "USD"
        symbols = ["EUR", "GBP"]

        client = ExchangeRateClient()
        client.get_rate(date, base, symbols)
        client.get_rate(date, base, symbols)


        self.fail()
