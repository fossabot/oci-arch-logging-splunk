# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .payment_detail import PaymentDetail
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PaypalPaymentDetail(PaymentDetail):
    """
    PayPal Payment related details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PaypalPaymentDetail object with values from keyword arguments. The default value of the :py:attr:`~oci.osp_gateway.models.PaypalPaymentDetail.payment_method` attribute
        of this class is ``PAYPAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_paid_on:
            The value to assign to the time_paid_on property of this PaypalPaymentDetail.
        :type time_paid_on: datetime

        :param paid_by:
            The value to assign to the paid_by property of this PaypalPaymentDetail.
        :type paid_by: str

        :param payment_method:
            The value to assign to the payment_method property of this PaypalPaymentDetail.
            Allowed values for this property are: "CREDIT_CARD", "PAYPAL", "OTHER"
        :type payment_method: str

        :param amount_paid:
            The value to assign to the amount_paid property of this PaypalPaymentDetail.
        :type amount_paid: float

        :param paypal_id:
            The value to assign to the paypal_id property of this PaypalPaymentDetail.
        :type paypal_id: str

        :param paypal_reference:
            The value to assign to the paypal_reference property of this PaypalPaymentDetail.
        :type paypal_reference: str

        """
        self.swagger_types = {
            'time_paid_on': 'datetime',
            'paid_by': 'str',
            'payment_method': 'str',
            'amount_paid': 'float',
            'paypal_id': 'str',
            'paypal_reference': 'str'
        }

        self.attribute_map = {
            'time_paid_on': 'timePaidOn',
            'paid_by': 'paidBy',
            'payment_method': 'paymentMethod',
            'amount_paid': 'amountPaid',
            'paypal_id': 'paypalId',
            'paypal_reference': 'paypalReference'
        }

        self._time_paid_on = None
        self._paid_by = None
        self._payment_method = None
        self._amount_paid = None
        self._paypal_id = None
        self._paypal_reference = None
        self._payment_method = 'PAYPAL'

    @property
    def paypal_id(self):
        """
        Gets the paypal_id of this PaypalPaymentDetail.
        The id (email address) of the paypal payment


        :return: The paypal_id of this PaypalPaymentDetail.
        :rtype: str
        """
        return self._paypal_id

    @paypal_id.setter
    def paypal_id(self, paypal_id):
        """
        Sets the paypal_id of this PaypalPaymentDetail.
        The id (email address) of the paypal payment


        :param paypal_id: The paypal_id of this PaypalPaymentDetail.
        :type: str
        """
        self._paypal_id = paypal_id

    @property
    def paypal_reference(self):
        """
        Gets the paypal_reference of this PaypalPaymentDetail.
        paypal payment reference


        :return: The paypal_reference of this PaypalPaymentDetail.
        :rtype: str
        """
        return self._paypal_reference

    @paypal_reference.setter
    def paypal_reference(self, paypal_reference):
        """
        Sets the paypal_reference of this PaypalPaymentDetail.
        paypal payment reference


        :param paypal_reference: The paypal_reference of this PaypalPaymentDetail.
        :type: str
        """
        self._paypal_reference = paypal_reference

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
