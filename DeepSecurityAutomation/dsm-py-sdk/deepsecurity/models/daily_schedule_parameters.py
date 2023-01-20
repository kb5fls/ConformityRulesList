# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2022 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.686
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DailyScheduleParameters(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start_time': 'int',
        'frequency_type': 'str',
        'custom_interval': 'int'
    }

    attribute_map = {
        'start_time': 'startTime',
        'frequency_type': 'frequencyType',
        'custom_interval': 'customInterval'
    }

    def __init__(self, start_time=None, frequency_type=None, custom_interval=None):  # noqa: E501
        """DailyScheduleParameters - a model defined in Swagger"""  # noqa: E501

        self._start_time = None
        self._frequency_type = None
        self._custom_interval = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if frequency_type is not None:
            self.frequency_type = frequency_type
        if custom_interval is not None:
            self.custom_interval = custom_interval

    @property
    def start_time(self):
        """Gets the start_time of this DailyScheduleParameters.  # noqa: E501

        Date/Time when the task should run.  # noqa: E501

        :return: The start_time of this DailyScheduleParameters.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DailyScheduleParameters.

        Date/Time when the task should run.  # noqa: E501

        :param start_time: The start_time of this DailyScheduleParameters.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def frequency_type(self):
        """Gets the frequency_type of this DailyScheduleParameters.  # noqa: E501

        Frequency type.  # noqa: E501

        :return: The frequency_type of this DailyScheduleParameters.  # noqa: E501
        :rtype: str
        """
        return self._frequency_type

    @frequency_type.setter
    def frequency_type(self, frequency_type):
        """Sets the frequency_type of this DailyScheduleParameters.

        Frequency type.  # noqa: E501

        :param frequency_type: The frequency_type of this DailyScheduleParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["everyday", "weekdays", "custom"]  # noqa: E501
        if frequency_type not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency_type` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency_type, allowed_values)
            )

        self._frequency_type = frequency_type

    @property
    def custom_interval(self):
        """Gets the custom_interval of this DailyScheduleParameters.  # noqa: E501

        Custom interval.  # noqa: E501

        :return: The custom_interval of this DailyScheduleParameters.  # noqa: E501
        :rtype: int
        """
        return self._custom_interval

    @custom_interval.setter
    def custom_interval(self, custom_interval):
        """Sets the custom_interval of this DailyScheduleParameters.

        Custom interval.  # noqa: E501

        :param custom_interval: The custom_interval of this DailyScheduleParameters.  # noqa: E501
        :type: int
        """

        self._custom_interval = custom_interval

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DailyScheduleParameters, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DailyScheduleParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

