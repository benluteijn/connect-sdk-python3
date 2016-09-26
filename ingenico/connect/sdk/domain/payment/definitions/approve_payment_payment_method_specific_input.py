#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class ApprovePaymentPaymentMethodSpecificInput(DataObject):
    """
    Class ApprovePaymentPaymentMethodSpecificInput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_ApprovePaymentPaymentMethodSpecificInput
    
    Attributes:
        date_collect:  str
        token:         str
     """

    date_collect = None
    token = None

    def to_dictionary(self):
        dictionary = super(ApprovePaymentPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'dateCollect', self.date_collect)
        self._add_to_dictionary(dictionary, 'token', self.token)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApprovePaymentPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'dateCollect' in dictionary:
            self.date_collect = dictionary['dateCollect']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
