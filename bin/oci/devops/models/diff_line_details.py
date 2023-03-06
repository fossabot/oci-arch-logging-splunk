# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiffLineDetails(object):
    """
    Details about a line within the difference.
    """

    #: A constant which can be used with the conflict_marker property of a DiffLineDetails.
    #: This constant has a value of "BASE"
    CONFLICT_MARKER_BASE = "BASE"

    #: A constant which can be used with the conflict_marker property of a DiffLineDetails.
    #: This constant has a value of "TARGET"
    CONFLICT_MARKER_TARGET = "TARGET"

    #: A constant which can be used with the conflict_marker property of a DiffLineDetails.
    #: This constant has a value of "MARKER"
    CONFLICT_MARKER_MARKER = "MARKER"

    #: A constant which can be used with the conflict_marker property of a DiffLineDetails.
    #: This constant has a value of "NONE"
    CONFLICT_MARKER_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new DiffLineDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param base_line:
            The value to assign to the base_line property of this DiffLineDetails.
        :type base_line: int

        :param target_line:
            The value to assign to the target_line property of this DiffLineDetails.
        :type target_line: int

        :param line_content:
            The value to assign to the line_content property of this DiffLineDetails.
        :type line_content: str

        :param conflict_marker:
            The value to assign to the conflict_marker property of this DiffLineDetails.
            Allowed values for this property are: "BASE", "TARGET", "MARKER", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type conflict_marker: str

        """
        self.swagger_types = {
            'base_line': 'int',
            'target_line': 'int',
            'line_content': 'str',
            'conflict_marker': 'str'
        }

        self.attribute_map = {
            'base_line': 'baseLine',
            'target_line': 'targetLine',
            'line_content': 'lineContent',
            'conflict_marker': 'conflictMarker'
        }

        self._base_line = None
        self._target_line = None
        self._line_content = None
        self._conflict_marker = None

    @property
    def base_line(self):
        """
        Gets the base_line of this DiffLineDetails.
        The number of a line in the base version.


        :return: The base_line of this DiffLineDetails.
        :rtype: int
        """
        return self._base_line

    @base_line.setter
    def base_line(self, base_line):
        """
        Sets the base_line of this DiffLineDetails.
        The number of a line in the base version.


        :param base_line: The base_line of this DiffLineDetails.
        :type: int
        """
        self._base_line = base_line

    @property
    def target_line(self):
        """
        Gets the target_line of this DiffLineDetails.
        The number of a line in the target version.


        :return: The target_line of this DiffLineDetails.
        :rtype: int
        """
        return self._target_line

    @target_line.setter
    def target_line(self, target_line):
        """
        Sets the target_line of this DiffLineDetails.
        The number of a line in the target version.


        :param target_line: The target_line of this DiffLineDetails.
        :type: int
        """
        self._target_line = target_line

    @property
    def line_content(self):
        """
        Gets the line_content of this DiffLineDetails.
        The contents of a line.


        :return: The line_content of this DiffLineDetails.
        :rtype: str
        """
        return self._line_content

    @line_content.setter
    def line_content(self, line_content):
        """
        Sets the line_content of this DiffLineDetails.
        The contents of a line.


        :param line_content: The line_content of this DiffLineDetails.
        :type: str
        """
        self._line_content = line_content

    @property
    def conflict_marker(self):
        """
        Gets the conflict_marker of this DiffLineDetails.
        Indicates whether a line in a conflicted section of the difference is from the base version, the target version, or if its just a marker indicating the beginning, middle, or end of a conflicted section.

        Allowed values for this property are: "BASE", "TARGET", "MARKER", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The conflict_marker of this DiffLineDetails.
        :rtype: str
        """
        return self._conflict_marker

    @conflict_marker.setter
    def conflict_marker(self, conflict_marker):
        """
        Sets the conflict_marker of this DiffLineDetails.
        Indicates whether a line in a conflicted section of the difference is from the base version, the target version, or if its just a marker indicating the beginning, middle, or end of a conflicted section.


        :param conflict_marker: The conflict_marker of this DiffLineDetails.
        :type: str
        """
        allowed_values = ["BASE", "TARGET", "MARKER", "NONE"]
        if not value_allowed_none_or_none_sentinel(conflict_marker, allowed_values):
            conflict_marker = 'UNKNOWN_ENUM_VALUE'
        self._conflict_marker = conflict_marker

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
