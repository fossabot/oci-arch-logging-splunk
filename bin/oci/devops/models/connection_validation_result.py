# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionValidationResult(object):
    """
    The result of validating the credentials of a connection.
    """

    #: A constant which can be used with the result property of a ConnectionValidationResult.
    #: This constant has a value of "PASS"
    RESULT_PASS = "PASS"

    #: A constant which can be used with the result property of a ConnectionValidationResult.
    #: This constant has a value of "FAIL"
    RESULT_FAIL = "FAIL"

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionValidationResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param result:
            The value to assign to the result property of this ConnectionValidationResult.
            Allowed values for this property are: "PASS", "FAIL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type result: str

        :param time_validated:
            The value to assign to the time_validated property of this ConnectionValidationResult.
        :type time_validated: datetime

        :param message:
            The value to assign to the message property of this ConnectionValidationResult.
        :type message: str

        """
        self.swagger_types = {
            'result': 'str',
            'time_validated': 'datetime',
            'message': 'str'
        }

        self.attribute_map = {
            'result': 'result',
            'time_validated': 'timeValidated',
            'message': 'message'
        }

        self._result = None
        self._time_validated = None
        self._message = None

    @property
    def result(self):
        """
        Gets the result of this ConnectionValidationResult.
        The latest result of whether the credentials pass the validation.

        Allowed values for this property are: "PASS", "FAIL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The result of this ConnectionValidationResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this ConnectionValidationResult.
        The latest result of whether the credentials pass the validation.


        :param result: The result of this ConnectionValidationResult.
        :type: str
        """
        allowed_values = ["PASS", "FAIL"]
        if not value_allowed_none_or_none_sentinel(result, allowed_values):
            result = 'UNKNOWN_ENUM_VALUE'
        self._result = result

    @property
    def time_validated(self):
        """
        Gets the time_validated of this ConnectionValidationResult.
        The latest timestamp when the connection was validated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_validated of this ConnectionValidationResult.
        :rtype: datetime
        """
        return self._time_validated

    @time_validated.setter
    def time_validated(self, time_validated):
        """
        Sets the time_validated of this ConnectionValidationResult.
        The latest timestamp when the connection was validated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_validated: The time_validated of this ConnectionValidationResult.
        :type: datetime
        """
        self._time_validated = time_validated

    @property
    def message(self):
        """
        Gets the message of this ConnectionValidationResult.
        A message describing the result of connection validation in more detail.


        :return: The message of this ConnectionValidationResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ConnectionValidationResult.
        A message describing the result of connection validation in more detail.


        :param message: The message of this ConnectionValidationResult.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
