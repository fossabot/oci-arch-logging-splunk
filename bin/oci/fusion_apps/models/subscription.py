# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Subscription(object):
    """
    Subscription information for compartmentId. Only root compartments are allowed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Subscription object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Subscription.
        :type id: str

        :param classic_subscription_id:
            The value to assign to the classic_subscription_id property of this Subscription.
        :type classic_subscription_id: str

        :param service_name:
            The value to assign to the service_name property of this Subscription.
        :type service_name: str

        :param skus:
            The value to assign to the skus property of this Subscription.
        :type skus: list[oci.fusion_apps.models.SubscriptionSku]

        """
        self.swagger_types = {
            'id': 'str',
            'classic_subscription_id': 'str',
            'service_name': 'str',
            'skus': 'list[SubscriptionSku]'
        }

        self.attribute_map = {
            'id': 'id',
            'classic_subscription_id': 'classicSubscriptionId',
            'service_name': 'serviceName',
            'skus': 'skus'
        }

        self._id = None
        self._classic_subscription_id = None
        self._service_name = None
        self._skus = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Subscription.
        OCID of the subscription details for particular root compartment or tenancy.


        :return: The id of this Subscription.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Subscription.
        OCID of the subscription details for particular root compartment or tenancy.


        :param id: The id of this Subscription.
        :type: str
        """
        self._id = id

    @property
    def classic_subscription_id(self):
        """
        **[Required]** Gets the classic_subscription_id of this Subscription.
        Subscription id.


        :return: The classic_subscription_id of this Subscription.
        :rtype: str
        """
        return self._classic_subscription_id

    @classic_subscription_id.setter
    def classic_subscription_id(self, classic_subscription_id):
        """
        Sets the classic_subscription_id of this Subscription.
        Subscription id.


        :param classic_subscription_id: The classic_subscription_id of this Subscription.
        :type: str
        """
        self._classic_subscription_id = classic_subscription_id

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this Subscription.
        The type of subscription, such as 'CLOUDCM'/'SAAS'/'CRM', etc.


        :return: The service_name of this Subscription.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this Subscription.
        The type of subscription, such as 'CLOUDCM'/'SAAS'/'CRM', etc.


        :param service_name: The service_name of this Subscription.
        :type: str
        """
        self._service_name = service_name

    @property
    def skus(self):
        """
        **[Required]** Gets the skus of this Subscription.
        Stock keeping unit.


        :return: The skus of this Subscription.
        :rtype: list[oci.fusion_apps.models.SubscriptionSku]
        """
        return self._skus

    @skus.setter
    def skus(self, skus):
        """
        Sets the skus of this Subscription.
        Stock keeping unit.


        :param skus: The skus of this Subscription.
        :type: list[oci.fusion_apps.models.SubscriptionSku]
        """
        self._skus = skus

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
