# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.mandates.definitions.mandate_customer import MandateCustomer


class MandateResponse(DataObject):

    __customer = None
    __customer_reference = None
    __recurrence_type = None
    __status = None
    __unique_mandate_reference = None

    @property
    def customer(self):
        """
        | Customer object containing customer specific inputs
        
        Type: :class:`ingenico.connect.sdk.domain.mandates.definitions.mandate_customer.MandateCustomer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def customer_reference(self):
        """
        | The unique identifier of the customer to which this mandate is applicable
        
        Type: str
        """
        return self.__customer_reference

    @customer_reference.setter
    def customer_reference(self, value):
        self.__customer_reference = value

    @property
    def recurrence_type(self):
        """
        | Specifieds whether the mandate is for one-off or recurring payments.
        
        Type: str
        """
        return self.__recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, value):
        self.__recurrence_type = value

    @property
    def status(self):
        """
        | The status of the mandate. Possible values are:
        
        * ACTIVE
        * EXPIRED
        * CREATED
        * REVOKED
        * WAITING_FOR_REFERENCE
        * BLOCKED
        * USED
        
        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def unique_mandate_reference(self):
        """
        | The unique identifier of the mandate
        
        Type: str
        """
        return self.__unique_mandate_reference

    @unique_mandate_reference.setter
    def unique_mandate_reference(self, value):
        self.__unique_mandate_reference = value

    def to_dictionary(self):
        dictionary = super(MandateResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customer', self.customer)
        self._add_to_dictionary(dictionary, 'customerReference', self.customer_reference)
        self._add_to_dictionary(dictionary, 'recurrenceType', self.recurrence_type)
        self._add_to_dictionary(dictionary, 'status', self.status)
        self._add_to_dictionary(dictionary, 'uniqueMandateReference', self.unique_mandate_reference)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateResponse, self).from_dictionary(dictionary)
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = MandateCustomer()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'customerReference' in dictionary:
            self.customer_reference = dictionary['customerReference']
        if 'recurrenceType' in dictionary:
            self.recurrence_type = dictionary['recurrenceType']
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'uniqueMandateReference' in dictionary:
            self.unique_mandate_reference = dictionary['uniqueMandateReference']
        return self
