# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage import DeployStage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoadBalancerTrafficShiftDeployStage(DeployStage):
    """
    Specifies load balancer traffic shift stage.
    """

    #: A constant which can be used with the traffic_shift_target property of a LoadBalancerTrafficShiftDeployStage.
    #: This constant has a value of "AUTO_SELECT"
    TRAFFIC_SHIFT_TARGET_AUTO_SELECT = "AUTO_SELECT"

    #: A constant which can be used with the traffic_shift_target property of a LoadBalancerTrafficShiftDeployStage.
    #: This constant has a value of "BLUE"
    TRAFFIC_SHIFT_TARGET_BLUE = "BLUE"

    #: A constant which can be used with the traffic_shift_target property of a LoadBalancerTrafficShiftDeployStage.
    #: This constant has a value of "GREEN"
    TRAFFIC_SHIFT_TARGET_GREEN = "GREEN"

    def __init__(self, **kwargs):
        """
        Initializes a new LoadBalancerTrafficShiftDeployStage object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.LoadBalancerTrafficShiftDeployStage.deploy_stage_type` attribute
        of this class is ``LOAD_BALANCER_TRAFFIC_SHIFT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LoadBalancerTrafficShiftDeployStage.
        :type id: str

        :param description:
            The value to assign to the description property of this LoadBalancerTrafficShiftDeployStage.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this LoadBalancerTrafficShiftDeployStage.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this LoadBalancerTrafficShiftDeployStage.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this LoadBalancerTrafficShiftDeployStage.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LoadBalancerTrafficShiftDeployStage.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this LoadBalancerTrafficShiftDeployStage.
            Allowed values for this property are: "WAIT", "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL", "OKE_BLUE_GREEN_DEPLOYMENT", "OKE_BLUE_GREEN_TRAFFIC_SHIFT", "OKE_CANARY_DEPLOYMENT", "OKE_CANARY_TRAFFIC_SHIFT", "OKE_CANARY_APPROVAL", "OKE_DEPLOYMENT", "DEPLOY_FUNCTION", "INVOKE_FUNCTION", "LOAD_BALANCER_TRAFFIC_SHIFT", "MANUAL_APPROVAL", "OKE_HELM_CHART_DEPLOYMENT", "SHELL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this LoadBalancerTrafficShiftDeployStage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this LoadBalancerTrafficShiftDeployStage.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LoadBalancerTrafficShiftDeployStage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this LoadBalancerTrafficShiftDeployStage.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this LoadBalancerTrafficShiftDeployStage.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LoadBalancerTrafficShiftDeployStage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this LoadBalancerTrafficShiftDeployStage.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this LoadBalancerTrafficShiftDeployStage.
        :type system_tags: dict(str, dict(str, object))

        :param blue_backend_ips:
            The value to assign to the blue_backend_ips property of this LoadBalancerTrafficShiftDeployStage.
        :type blue_backend_ips: oci.devops.models.BackendSetIpCollection

        :param green_backend_ips:
            The value to assign to the green_backend_ips property of this LoadBalancerTrafficShiftDeployStage.
        :type green_backend_ips: oci.devops.models.BackendSetIpCollection

        :param traffic_shift_target:
            The value to assign to the traffic_shift_target property of this LoadBalancerTrafficShiftDeployStage.
            Allowed values for this property are: "AUTO_SELECT", "BLUE", "GREEN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type traffic_shift_target: str

        :param rollout_policy:
            The value to assign to the rollout_policy property of this LoadBalancerTrafficShiftDeployStage.
        :type rollout_policy: oci.devops.models.LoadBalancerTrafficShiftRolloutPolicy

        :param load_balancer_config:
            The value to assign to the load_balancer_config property of this LoadBalancerTrafficShiftDeployStage.
        :type load_balancer_config: oci.devops.models.LoadBalancerConfig

        :param rollback_policy:
            The value to assign to the rollback_policy property of this LoadBalancerTrafficShiftDeployStage.
        :type rollback_policy: oci.devops.models.DeployStageRollbackPolicy

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'deploy_pipeline_id': 'str',
            'compartment_id': 'str',
            'deploy_stage_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'blue_backend_ips': 'BackendSetIpCollection',
            'green_backend_ips': 'BackendSetIpCollection',
            'traffic_shift_target': 'str',
            'rollout_policy': 'LoadBalancerTrafficShiftRolloutPolicy',
            'load_balancer_config': 'LoadBalancerConfig',
            'rollback_policy': 'DeployStageRollbackPolicy'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'deploy_pipeline_id': 'deployPipelineId',
            'compartment_id': 'compartmentId',
            'deploy_stage_type': 'deployStageType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'blue_backend_ips': 'blueBackendIps',
            'green_backend_ips': 'greenBackendIps',
            'traffic_shift_target': 'trafficShiftTarget',
            'rollout_policy': 'rolloutPolicy',
            'load_balancer_config': 'loadBalancerConfig',
            'rollback_policy': 'rollbackPolicy'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._deploy_pipeline_id = None
        self._compartment_id = None
        self._deploy_stage_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._blue_backend_ips = None
        self._green_backend_ips = None
        self._traffic_shift_target = None
        self._rollout_policy = None
        self._load_balancer_config = None
        self._rollback_policy = None
        self._deploy_stage_type = 'LOAD_BALANCER_TRAFFIC_SHIFT'

    @property
    def blue_backend_ips(self):
        """
        **[Required]** Gets the blue_backend_ips of this LoadBalancerTrafficShiftDeployStage.

        :return: The blue_backend_ips of this LoadBalancerTrafficShiftDeployStage.
        :rtype: oci.devops.models.BackendSetIpCollection
        """
        return self._blue_backend_ips

    @blue_backend_ips.setter
    def blue_backend_ips(self, blue_backend_ips):
        """
        Sets the blue_backend_ips of this LoadBalancerTrafficShiftDeployStage.

        :param blue_backend_ips: The blue_backend_ips of this LoadBalancerTrafficShiftDeployStage.
        :type: oci.devops.models.BackendSetIpCollection
        """
        self._blue_backend_ips = blue_backend_ips

    @property
    def green_backend_ips(self):
        """
        **[Required]** Gets the green_backend_ips of this LoadBalancerTrafficShiftDeployStage.

        :return: The green_backend_ips of this LoadBalancerTrafficShiftDeployStage.
        :rtype: oci.devops.models.BackendSetIpCollection
        """
        return self._green_backend_ips

    @green_backend_ips.setter
    def green_backend_ips(self, green_backend_ips):
        """
        Sets the green_backend_ips of this LoadBalancerTrafficShiftDeployStage.

        :param green_backend_ips: The green_backend_ips of this LoadBalancerTrafficShiftDeployStage.
        :type: oci.devops.models.BackendSetIpCollection
        """
        self._green_backend_ips = green_backend_ips

    @property
    def traffic_shift_target(self):
        """
        **[Required]** Gets the traffic_shift_target of this LoadBalancerTrafficShiftDeployStage.
        Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to green Backend IPs as per rolloutPolicy.

        Allowed values for this property are: "AUTO_SELECT", "BLUE", "GREEN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The traffic_shift_target of this LoadBalancerTrafficShiftDeployStage.
        :rtype: str
        """
        return self._traffic_shift_target

    @traffic_shift_target.setter
    def traffic_shift_target(self, traffic_shift_target):
        """
        Sets the traffic_shift_target of this LoadBalancerTrafficShiftDeployStage.
        Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to green Backend IPs as per rolloutPolicy.


        :param traffic_shift_target: The traffic_shift_target of this LoadBalancerTrafficShiftDeployStage.
        :type: str
        """
        allowed_values = ["AUTO_SELECT", "BLUE", "GREEN"]
        if not value_allowed_none_or_none_sentinel(traffic_shift_target, allowed_values):
            traffic_shift_target = 'UNKNOWN_ENUM_VALUE'
        self._traffic_shift_target = traffic_shift_target

    @property
    def rollout_policy(self):
        """
        **[Required]** Gets the rollout_policy of this LoadBalancerTrafficShiftDeployStage.

        :return: The rollout_policy of this LoadBalancerTrafficShiftDeployStage.
        :rtype: oci.devops.models.LoadBalancerTrafficShiftRolloutPolicy
        """
        return self._rollout_policy

    @rollout_policy.setter
    def rollout_policy(self, rollout_policy):
        """
        Sets the rollout_policy of this LoadBalancerTrafficShiftDeployStage.

        :param rollout_policy: The rollout_policy of this LoadBalancerTrafficShiftDeployStage.
        :type: oci.devops.models.LoadBalancerTrafficShiftRolloutPolicy
        """
        self._rollout_policy = rollout_policy

    @property
    def load_balancer_config(self):
        """
        **[Required]** Gets the load_balancer_config of this LoadBalancerTrafficShiftDeployStage.

        :return: The load_balancer_config of this LoadBalancerTrafficShiftDeployStage.
        :rtype: oci.devops.models.LoadBalancerConfig
        """
        return self._load_balancer_config

    @load_balancer_config.setter
    def load_balancer_config(self, load_balancer_config):
        """
        Sets the load_balancer_config of this LoadBalancerTrafficShiftDeployStage.

        :param load_balancer_config: The load_balancer_config of this LoadBalancerTrafficShiftDeployStage.
        :type: oci.devops.models.LoadBalancerConfig
        """
        self._load_balancer_config = load_balancer_config

    @property
    def rollback_policy(self):
        """
        Gets the rollback_policy of this LoadBalancerTrafficShiftDeployStage.

        :return: The rollback_policy of this LoadBalancerTrafficShiftDeployStage.
        :rtype: oci.devops.models.DeployStageRollbackPolicy
        """
        return self._rollback_policy

    @rollback_policy.setter
    def rollback_policy(self, rollback_policy):
        """
        Sets the rollback_policy of this LoadBalancerTrafficShiftDeployStage.

        :param rollback_policy: The rollback_policy of this LoadBalancerTrafficShiftDeployStage.
        :type: oci.devops.models.DeployStageRollbackPolicy
        """
        self._rollback_policy = rollback_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
