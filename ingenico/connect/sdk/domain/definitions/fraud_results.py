#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class FraudResults(DataObject):
    """
    Class FraudResults
    See also https://developer.globalcollect.com/documentation/api/server/#schema_FraudResults
    
    Attributes:
        fraud_service_result:  str
     """

    fraud_service_result = None

    def to_dictionary(self):
        dictionary = super(FraudResults, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'fraudServiceResult', self.fraud_service_result)
        return dictionary

    def from_dictionary(self, dictionary):
        super(FraudResults, self).from_dictionary(dictionary)
        if 'fraudServiceResult' in dictionary:
            self.fraud_service_result = dictionary['fraudServiceResult']
        return self
