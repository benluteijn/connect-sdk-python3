#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.bank_account_iban import BankAccountIban


class RedirectPaymentProduct816SpecificInput(DataObject):
    """
    Class RedirectPaymentProduct816SpecificInput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RedirectPaymentProduct816SpecificInput
    
    Attributes:
        bank_account_iban:  :class:`BankAccountIban`
     """

    bank_account_iban = None

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct816SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bankAccountIban', self.bank_account_iban)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct816SpecificInput, self).from_dictionary(dictionary)
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        return self
