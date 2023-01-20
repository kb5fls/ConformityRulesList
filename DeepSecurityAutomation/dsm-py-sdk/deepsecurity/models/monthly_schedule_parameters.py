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


class MonthlyScheduleParameters(object):
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
        'day_of_month': 'int',
        'week_of_month': 'str',
        'day_of_week': 'str',
        'months': 'list[str]'
    }

    attribute_map = {
        'start_time': 'startTime',
        'frequency_type': 'frequencyType',
        'day_of_month': 'dayOfMonth',
        'week_of_month': 'weekOfMonth',
        'day_of_week': 'dayOfWeek',
        'months': 'months'
    }

    def __init__(self, start_time=None, frequency_type=None, day_of_month=None, week_of_month=None, day_of_week=None, months=None):  # noqa: E501
        """MonthlyScheduleParameters - a model defined in Swagger"""  # noqa: E501

        self._start_time = None
        self._frequency_type = None
        self._day_of_month = None
        self._week_of_month = None
        self._day_of_week = None
        self._months = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if frequency_type is not None:
            self.frequency_type = frequency_type
        if day_of_month is not None:
            self.day_of_month = day_of_month
        if week_of_month is not None:
            self.week_of_month = week_of_month
        if day_of_week is not None:
            self.day_of_week = day_of_week
        if months is not None:
            self.months = months

    @property
    def start_time(self):
        """Gets the start_time of this MonthlyScheduleParameters.  # noqa: E501

        Date/Time when the task should run.  # noqa: E501

        :return: The start_time of this MonthlyScheduleParameters.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this MonthlyScheduleParameters.

        Date/Time when the task should run.  # noqa: E501

        :param start_time: The start_time of this MonthlyScheduleParameters.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def frequency_type(self):
        """Gets the frequency_type of this MonthlyScheduleParameters.  # noqa: E501

        Frequency type.  # noqa: E501

        :return: The frequency_type of this MonthlyScheduleParameters.  # noqa: E501
        :rtype: str
        """
        return self._frequency_type

    @frequency_type.setter
    def frequency_type(self, frequency_type):
        """Sets the frequency_type of this MonthlyScheduleParameters.

        Frequency type.  # noqa: E501

        :param frequency_type: The frequency_type of this MonthlyScheduleParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["day-of-month", "last-day-of-month", "custom"]  # noqa: E501
        if frequency_type not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency_type` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency_type, allowed_values)
            )

        self._frequency_type = frequency_type

    @property
    def day_of_month(self):
        """Gets the day_of_month of this MonthlyScheduleParameters.  # noqa: E501

        Specific day of month for frequency type: day-of-month.  # noqa: E501

        :return: The day_of_month of this MonthlyScheduleParameters.  # noqa: E501
        :rtype: int
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """Sets the day_of_month of this MonthlyScheduleParameters.

        Specific day of month for frequency type: day-of-month.  # noqa: E501

        :param day_of_month: The day_of_month of this MonthlyScheduleParameters.  # noqa: E501
        :type: int
        """

        self._day_of_month = day_of_month

    @property
    def week_of_month(self):
        """Gets the week_of_month of this MonthlyScheduleParameters.  # noqa: E501

        Specific week of month for frequency type: custom.  # noqa: E501

        :return: The week_of_month of this MonthlyScheduleParameters.  # noqa: E501
        :rtype: str
        """
        return self._week_of_month

    @week_of_month.setter
    def week_of_month(self, week_of_month):
        """Sets the week_of_month of this MonthlyScheduleParameters.

        Specific week of month for frequency type: custom.  # noqa: E501

        :param week_of_month: The week_of_month of this MonthlyScheduleParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["first", "second", "third", "fourth", "last"]  # noqa: E501
        if week_of_month not in allowed_values:
            raise ValueError(
                "Invalid value for `week_of_month` ({0}), must be one of {1}"  # noqa: E501
                .format(week_of_month, allowed_values)
            )

        self._week_of_month = week_of_month

    @property
    def day_of_week(self):
        """Gets the day_of_week of this MonthlyScheduleParameters.  # noqa: E501

        Specific day of week for frequency type: custom.  # noqa: E501

        :return: The day_of_week of this MonthlyScheduleParameters.  # noqa: E501
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this MonthlyScheduleParameters.

        Specific day of week for frequency type: custom.  # noqa: E501

        :param day_of_week: The day_of_week of this MonthlyScheduleParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # noqa: E501
        if day_of_week not in allowed_values:
            raise ValueError(
                "Invalid value for `day_of_week` ({0}), must be one of {1}"  # noqa: E501
                .format(day_of_week, allowed_values)
            )

        self._day_of_week = day_of_week

    @property
    def months(self):
        """Gets the months of this MonthlyScheduleParameters.  # noqa: E501

        Months of the year when the scheduled task will run.  # noqa: E501

        :return: The months of this MonthlyScheduleParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._months

    @months.setter
    def months(self, months):
        """Sets the months of this MonthlyScheduleParameters.

        Months of the year when the scheduled task will run.  # noqa: E501

        :param months: The months of this MonthlyScheduleParameters.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["january", "feburary", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]  # noqa: E501
        if not set(months).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `months` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(months) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._months = months

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
        if issubclass(MonthlyScheduleParameters, dict):
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
        if not isinstance(other, MonthlyScheduleParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

