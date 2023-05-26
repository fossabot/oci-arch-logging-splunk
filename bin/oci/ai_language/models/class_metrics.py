# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClassMetrics(object):
    """
    class level Text Classification model metrics
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClassMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this ClassMetrics.
        :type label: str

        :param f1:
            The value to assign to the f1 property of this ClassMetrics.
        :type f1: float

        :param precision:
            The value to assign to the precision property of this ClassMetrics.
        :type precision: float

        :param recall:
            The value to assign to the recall property of this ClassMetrics.
        :type recall: float

        """
        self.swagger_types = {
            'label': 'str',
            'f1': 'float',
            'precision': 'float',
            'recall': 'float'
        }

        self.attribute_map = {
            'label': 'label',
            'f1': 'f1',
            'precision': 'precision',
            'recall': 'recall'
        }

        self._label = None
        self._f1 = None
        self._precision = None
        self._recall = None

    @property
    def label(self):
        """
        **[Required]** Gets the label of this ClassMetrics.
        Text classification label


        :return: The label of this ClassMetrics.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this ClassMetrics.
        Text classification label


        :param label: The label of this ClassMetrics.
        :type: str
        """
        self._label = label

    @property
    def f1(self):
        """
        **[Required]** Gets the f1 of this ClassMetrics.
        F1-score, is a measure of a model\u2019s accuracy on a dataset


        :return: The f1 of this ClassMetrics.
        :rtype: float
        """
        return self._f1

    @f1.setter
    def f1(self, f1):
        """
        Sets the f1 of this ClassMetrics.
        F1-score, is a measure of a model\u2019s accuracy on a dataset


        :param f1: The f1 of this ClassMetrics.
        :type: float
        """
        self._f1 = f1

    @property
    def precision(self):
        """
        **[Required]** Gets the precision of this ClassMetrics.
        Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)


        :return: The precision of this ClassMetrics.
        :rtype: float
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """
        Sets the precision of this ClassMetrics.
        Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)


        :param precision: The precision of this ClassMetrics.
        :type: float
        """
        self._precision = precision

    @property
    def recall(self):
        """
        **[Required]** Gets the recall of this ClassMetrics.
        Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.


        :return: The recall of this ClassMetrics.
        :rtype: float
        """
        return self._recall

    @recall.setter
    def recall(self, recall):
        """
        Sets the recall of this ClassMetrics.
        Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.


        :param recall: The recall of this ClassMetrics.
        :type: float
        """
        self._recall = recall

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
