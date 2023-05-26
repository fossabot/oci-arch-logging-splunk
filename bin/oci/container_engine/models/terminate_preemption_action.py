# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .preemption_action import PreemptionAction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TerminatePreemptionAction(PreemptionAction):
    """
    Terminates the preemptible instance when it is interrupted for eviction.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TerminatePreemptionAction object with values from keyword arguments. The default value of the :py:attr:`~oci.container_engine.models.TerminatePreemptionAction.type` attribute
        of this class is ``TERMINATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TerminatePreemptionAction.
            Allowed values for this property are: "TERMINATE"
        :type type: str

        :param is_preserve_boot_volume:
            The value to assign to the is_preserve_boot_volume property of this TerminatePreemptionAction.
        :type is_preserve_boot_volume: bool

        """
        self.swagger_types = {
            'type': 'str',
            'is_preserve_boot_volume': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'is_preserve_boot_volume': 'isPreserveBootVolume'
        }

        self._type = None
        self._is_preserve_boot_volume = None
        self._type = 'TERMINATE'

    @property
    def is_preserve_boot_volume(self):
        """
        Gets the is_preserve_boot_volume of this TerminatePreemptionAction.
        Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated. Defaults to false if not specified.


        :return: The is_preserve_boot_volume of this TerminatePreemptionAction.
        :rtype: bool
        """
        return self._is_preserve_boot_volume

    @is_preserve_boot_volume.setter
    def is_preserve_boot_volume(self, is_preserve_boot_volume):
        """
        Sets the is_preserve_boot_volume of this TerminatePreemptionAction.
        Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated. Defaults to false if not specified.


        :param is_preserve_boot_volume: The is_preserve_boot_volume of this TerminatePreemptionAction.
        :type: bool
        """
        self._is_preserve_boot_volume = is_preserve_boot_volume

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
