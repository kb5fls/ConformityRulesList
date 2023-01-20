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


class ComputerFilter(object):
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
        'type': 'str',
        'computer_id': 'int',
        'computer_group_id': 'int',
        'policy_id': 'int',
        'smart_folder_id': 'int'
    }

    attribute_map = {
        'type': 'type',
        'computer_id': 'computerID',
        'computer_group_id': 'computerGroupID',
        'policy_id': 'policyID',
        'smart_folder_id': 'smartFolderID'
    }

    def __init__(self, type=None, computer_id=None, computer_group_id=None, policy_id=None, smart_folder_id=None):  # noqa: E501
        """ComputerFilter - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._computer_id = None
        self._computer_group_id = None
        self._policy_id = None
        self._smart_folder_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if computer_id is not None:
            self.computer_id = computer_id
        if computer_group_id is not None:
            self.computer_group_id = computer_group_id
        if policy_id is not None:
            self.policy_id = policy_id
        if smart_folder_id is not None:
            self.smart_folder_id = smart_folder_id

    @property
    def type(self):
        """Gets the type of this ComputerFilter.  # noqa: E501

        The type of computer filter.  # noqa: E501

        :return: The type of this ComputerFilter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComputerFilter.

        The type of computer filter.  # noqa: E501

        :param type: The type of this ComputerFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["computer", "all-computers", "computers-in-group", "computers-in-group-or-subgroup", "computers-using-policy", "computers-using-policy-or-subpolicy", "computers-in-smart-folder"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def computer_id(self):
        """Gets the computer_id of this ComputerFilter.  # noqa: E501

        Computer ID for filter type: computer.  # noqa: E501

        :return: The computer_id of this ComputerFilter.  # noqa: E501
        :rtype: int
        """
        return self._computer_id

    @computer_id.setter
    def computer_id(self, computer_id):
        """Sets the computer_id of this ComputerFilter.

        Computer ID for filter type: computer.  # noqa: E501

        :param computer_id: The computer_id of this ComputerFilter.  # noqa: E501
        :type: int
        """

        self._computer_id = computer_id

    @property
    def computer_group_id(self):
        """Gets the computer_group_id of this ComputerFilter.  # noqa: E501

        Computer Group ID for filter type: computers-in-group or computers-in-group-or-subgroup.  # noqa: E501

        :return: The computer_group_id of this ComputerFilter.  # noqa: E501
        :rtype: int
        """
        return self._computer_group_id

    @computer_group_id.setter
    def computer_group_id(self, computer_group_id):
        """Sets the computer_group_id of this ComputerFilter.

        Computer Group ID for filter type: computers-in-group or computers-in-group-or-subgroup.  # noqa: E501

        :param computer_group_id: The computer_group_id of this ComputerFilter.  # noqa: E501
        :type: int
        """

        self._computer_group_id = computer_group_id

    @property
    def policy_id(self):
        """Gets the policy_id of this ComputerFilter.  # noqa: E501

        Policy ID for filter type: computers-using-policy or computers-using-policy-or-subpolicy.  # noqa: E501

        :return: The policy_id of this ComputerFilter.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ComputerFilter.

        Policy ID for filter type: computers-using-policy or computers-using-policy-or-subpolicy.  # noqa: E501

        :param policy_id: The policy_id of this ComputerFilter.  # noqa: E501
        :type: int
        """

        self._policy_id = policy_id

    @property
    def smart_folder_id(self):
        """Gets the smart_folder_id of this ComputerFilter.  # noqa: E501

        Smart Folder ID for filter type: computers-in-smart-folder.  # noqa: E501

        :return: The smart_folder_id of this ComputerFilter.  # noqa: E501
        :rtype: int
        """
        return self._smart_folder_id

    @smart_folder_id.setter
    def smart_folder_id(self, smart_folder_id):
        """Sets the smart_folder_id of this ComputerFilter.

        Smart Folder ID for filter type: computers-in-smart-folder.  # noqa: E501

        :param smart_folder_id: The smart_folder_id of this ComputerFilter.  # noqa: E501
        :type: int
        """

        self._smart_folder_id = smart_folder_id

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
        if issubclass(ComputerFilter, dict):
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
        if not isinstance(other, ComputerFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

