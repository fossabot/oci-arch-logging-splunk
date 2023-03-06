# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyLimitRuleCase(object):
    """
    SteeringPolicyLimitRuleCase model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyLimitRuleCase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param case_condition:
            The value to assign to the case_condition property of this SteeringPolicyLimitRuleCase.
        :type case_condition: str

        :param count:
            The value to assign to the count property of this SteeringPolicyLimitRuleCase.
        :type count: int

        """
        self.swagger_types = {
            'case_condition': 'str',
            'count': 'int'
        }

        self.attribute_map = {
            'case_condition': 'caseCondition',
            'count': 'count'
        }

        self._case_condition = None
        self._count = None

    @property
    def case_condition(self):
        """
        Gets the case_condition of this SteeringPolicyLimitRuleCase.
        An expression that uses conditions at the time of a DNS query to indicate
        whether a case matches. Conditions may include the geographical location, IP
        subnet, or ASN the DNS query originated. **Example:** If you have an
        office that uses the subnet `192.0.2.0/24` you could use a `caseCondition`
        expression `query.client.address in ('192.0.2.0/24')` to define a case that
        matches queries from that office.


        :return: The case_condition of this SteeringPolicyLimitRuleCase.
        :rtype: str
        """
        return self._case_condition

    @case_condition.setter
    def case_condition(self, case_condition):
        """
        Sets the case_condition of this SteeringPolicyLimitRuleCase.
        An expression that uses conditions at the time of a DNS query to indicate
        whether a case matches. Conditions may include the geographical location, IP
        subnet, or ASN the DNS query originated. **Example:** If you have an
        office that uses the subnet `192.0.2.0/24` you could use a `caseCondition`
        expression `query.client.address in ('192.0.2.0/24')` to define a case that
        matches queries from that office.


        :param case_condition: The case_condition of this SteeringPolicyLimitRuleCase.
        :type: str
        """
        self._case_condition = case_condition

    @property
    def count(self):
        """
        **[Required]** Gets the count of this SteeringPolicyLimitRuleCase.
        The number of answers allowed to remain after the limit rule has been processed, keeping only the
        first of the remaining answers in the list. Example: If the `count` property is set to `2` and
        four answers remain before the limit rule is processed, only the first two answers in the list will
        remain after the limit rule has been processed.


        :return: The count of this SteeringPolicyLimitRuleCase.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this SteeringPolicyLimitRuleCase.
        The number of answers allowed to remain after the limit rule has been processed, keeping only the
        first of the remaining answers in the list. Example: If the `count` property is set to `2` and
        four answers remain before the limit rule is processed, only the first two answers in the list will
        remain after the limit rule has been processed.


        :param count: The count of this SteeringPolicyLimitRuleCase.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
