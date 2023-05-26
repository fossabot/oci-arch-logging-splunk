# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplySdmMaskingPolicyDifferenceDetails(object):
    """
    Details to apply the SDM masking policy difference to a masking policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplySdmMaskingPolicyDifferenceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sdm_masking_policy_difference_id:
            The value to assign to the sdm_masking_policy_difference_id property of this ApplySdmMaskingPolicyDifferenceDetails.
        :type sdm_masking_policy_difference_id: str

        """
        self.swagger_types = {
            'sdm_masking_policy_difference_id': 'str'
        }

        self.attribute_map = {
            'sdm_masking_policy_difference_id': 'sdmMaskingPolicyDifferenceId'
        }

        self._sdm_masking_policy_difference_id = None

    @property
    def sdm_masking_policy_difference_id(self):
        """
        Gets the sdm_masking_policy_difference_id of this ApplySdmMaskingPolicyDifferenceDetails.
        The OCID of the SDM masking policy difference.


        :return: The sdm_masking_policy_difference_id of this ApplySdmMaskingPolicyDifferenceDetails.
        :rtype: str
        """
        return self._sdm_masking_policy_difference_id

    @sdm_masking_policy_difference_id.setter
    def sdm_masking_policy_difference_id(self, sdm_masking_policy_difference_id):
        """
        Sets the sdm_masking_policy_difference_id of this ApplySdmMaskingPolicyDifferenceDetails.
        The OCID of the SDM masking policy difference.


        :param sdm_masking_policy_difference_id: The sdm_masking_policy_difference_id of this ApplySdmMaskingPolicyDifferenceDetails.
        :type: str
        """
        self._sdm_masking_policy_difference_id = sdm_masking_policy_difference_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
