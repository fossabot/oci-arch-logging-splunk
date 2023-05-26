# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateClusterOptionsDetails(object):
    """
    The properties that define extra options updating a cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateClusterOptionsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param admission_controller_options:
            The value to assign to the admission_controller_options property of this UpdateClusterOptionsDetails.
        :type admission_controller_options: oci.container_engine.models.AdmissionControllerOptions

        :param persistent_volume_config:
            The value to assign to the persistent_volume_config property of this UpdateClusterOptionsDetails.
        :type persistent_volume_config: oci.container_engine.models.PersistentVolumeConfigDetails

        :param service_lb_config:
            The value to assign to the service_lb_config property of this UpdateClusterOptionsDetails.
        :type service_lb_config: oci.container_engine.models.ServiceLbConfigDetails

        """
        self.swagger_types = {
            'admission_controller_options': 'AdmissionControllerOptions',
            'persistent_volume_config': 'PersistentVolumeConfigDetails',
            'service_lb_config': 'ServiceLbConfigDetails'
        }

        self.attribute_map = {
            'admission_controller_options': 'admissionControllerOptions',
            'persistent_volume_config': 'persistentVolumeConfig',
            'service_lb_config': 'serviceLbConfig'
        }

        self._admission_controller_options = None
        self._persistent_volume_config = None
        self._service_lb_config = None

    @property
    def admission_controller_options(self):
        """
        Gets the admission_controller_options of this UpdateClusterOptionsDetails.
        Configurable cluster admission controllers


        :return: The admission_controller_options of this UpdateClusterOptionsDetails.
        :rtype: oci.container_engine.models.AdmissionControllerOptions
        """
        return self._admission_controller_options

    @admission_controller_options.setter
    def admission_controller_options(self, admission_controller_options):
        """
        Sets the admission_controller_options of this UpdateClusterOptionsDetails.
        Configurable cluster admission controllers


        :param admission_controller_options: The admission_controller_options of this UpdateClusterOptionsDetails.
        :type: oci.container_engine.models.AdmissionControllerOptions
        """
        self._admission_controller_options = admission_controller_options

    @property
    def persistent_volume_config(self):
        """
        Gets the persistent_volume_config of this UpdateClusterOptionsDetails.

        :return: The persistent_volume_config of this UpdateClusterOptionsDetails.
        :rtype: oci.container_engine.models.PersistentVolumeConfigDetails
        """
        return self._persistent_volume_config

    @persistent_volume_config.setter
    def persistent_volume_config(self, persistent_volume_config):
        """
        Sets the persistent_volume_config of this UpdateClusterOptionsDetails.

        :param persistent_volume_config: The persistent_volume_config of this UpdateClusterOptionsDetails.
        :type: oci.container_engine.models.PersistentVolumeConfigDetails
        """
        self._persistent_volume_config = persistent_volume_config

    @property
    def service_lb_config(self):
        """
        Gets the service_lb_config of this UpdateClusterOptionsDetails.

        :return: The service_lb_config of this UpdateClusterOptionsDetails.
        :rtype: oci.container_engine.models.ServiceLbConfigDetails
        """
        return self._service_lb_config

    @service_lb_config.setter
    def service_lb_config(self, service_lb_config):
        """
        Sets the service_lb_config of this UpdateClusterOptionsDetails.

        :param service_lb_config: The service_lb_config of this UpdateClusterOptionsDetails.
        :type: oci.container_engine.models.ServiceLbConfigDetails
        """
        self._service_lb_config = service_lb_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
