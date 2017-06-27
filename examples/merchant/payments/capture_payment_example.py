#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.payment.capture_payment_request import CapturePaymentRequest


class CapturePaymentExample(object):

    def example(self):
        with self.__get_client() as client:
            body = CapturePaymentRequest()
            body.amount = 2980

            response = client.merchant("merchantId").payments().capture("paymentId", body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
