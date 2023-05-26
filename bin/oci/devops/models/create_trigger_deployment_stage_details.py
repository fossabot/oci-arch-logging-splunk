# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_build_pipeline_stage_details import CreateBuildPipelineStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTriggerDeploymentStageDetails(CreateBuildPipelineStageDetails):
    """
    Specifies the Trigger Deployment stage, which runs another pipeline of the application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTriggerDeploymentStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateTriggerDeploymentStageDetails.build_pipeline_stage_type` attribute
        of this class is ``TRIGGER_DEPLOYMENT_PIPELINE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateTriggerDeploymentStageDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateTriggerDeploymentStageDetails.
        :type description: str

        :param build_pipeline_stage_type:
            The value to assign to the build_pipeline_stage_type property of this CreateTriggerDeploymentStageDetails.
        :type build_pipeline_stage_type: str

        :param build_pipeline_id:
            The value to assign to the build_pipeline_id property of this CreateTriggerDeploymentStageDetails.
        :type build_pipeline_id: str

        :param build_pipeline_stage_predecessor_collection:
            The value to assign to the build_pipeline_stage_predecessor_collection property of this CreateTriggerDeploymentStageDetails.
        :type build_pipeline_stage_predecessor_collection: oci.devops.models.BuildPipelineStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateTriggerDeploymentStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateTriggerDeploymentStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this CreateTriggerDeploymentStageDetails.
        :type deploy_pipeline_id: str

        :param is_pass_all_parameters_enabled:
            The value to assign to the is_pass_all_parameters_enabled property of this CreateTriggerDeploymentStageDetails.
        :type is_pass_all_parameters_enabled: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'build_pipeline_stage_type': 'str',
            'build_pipeline_id': 'str',
            'build_pipeline_stage_predecessor_collection': 'BuildPipelineStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'deploy_pipeline_id': 'str',
            'is_pass_all_parameters_enabled': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'build_pipeline_stage_type': 'buildPipelineStageType',
            'build_pipeline_id': 'buildPipelineId',
            'build_pipeline_stage_predecessor_collection': 'buildPipelineStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'deploy_pipeline_id': 'deployPipelineId',
            'is_pass_all_parameters_enabled': 'isPassAllParametersEnabled'
        }

        self._display_name = None
        self._description = None
        self._build_pipeline_stage_type = None
        self._build_pipeline_id = None
        self._build_pipeline_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._deploy_pipeline_id = None
        self._is_pass_all_parameters_enabled = None
        self._build_pipeline_stage_type = 'TRIGGER_DEPLOYMENT_PIPELINE'

    @property
    def deploy_pipeline_id(self):
        """
        **[Required]** Gets the deploy_pipeline_id of this CreateTriggerDeploymentStageDetails.
        A target deployment pipeline OCID that will run in this stage.


        :return: The deploy_pipeline_id of this CreateTriggerDeploymentStageDetails.
        :rtype: str
        """
        return self._deploy_pipeline_id

    @deploy_pipeline_id.setter
    def deploy_pipeline_id(self, deploy_pipeline_id):
        """
        Sets the deploy_pipeline_id of this CreateTriggerDeploymentStageDetails.
        A target deployment pipeline OCID that will run in this stage.


        :param deploy_pipeline_id: The deploy_pipeline_id of this CreateTriggerDeploymentStageDetails.
        :type: str
        """
        self._deploy_pipeline_id = deploy_pipeline_id

    @property
    def is_pass_all_parameters_enabled(self):
        """
        **[Required]** Gets the is_pass_all_parameters_enabled of this CreateTriggerDeploymentStageDetails.
        A boolean flag that specifies whether all the parameters must be passed when the deployment is triggered.


        :return: The is_pass_all_parameters_enabled of this CreateTriggerDeploymentStageDetails.
        :rtype: bool
        """
        return self._is_pass_all_parameters_enabled

    @is_pass_all_parameters_enabled.setter
    def is_pass_all_parameters_enabled(self, is_pass_all_parameters_enabled):
        """
        Sets the is_pass_all_parameters_enabled of this CreateTriggerDeploymentStageDetails.
        A boolean flag that specifies whether all the parameters must be passed when the deployment is triggered.


        :param is_pass_all_parameters_enabled: The is_pass_all_parameters_enabled of this CreateTriggerDeploymentStageDetails.
        :type: bool
        """
        self._is_pass_all_parameters_enabled = is_pass_all_parameters_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
