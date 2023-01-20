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


class TrustRulesetUpdateRequest(object):
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
        'name': 'str',
        'description': 'str',
        'rule_ids': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'rule_ids': 'ruleIds'
    }

    def __init__(self, name=None, description=None, rule_ids=None):  # noqa: E501
        """TrustRulesetUpdateRequest - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._rule_ids = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if rule_ids is not None:
            self.rule_ids = rule_ids

    @property
    def name(self):
        """Gets the name of this TrustRulesetUpdateRequest.  # noqa: E501

        Name of the trust ruleset. Searchable as String.  # noqa: E501

        :return: The name of this TrustRulesetUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrustRulesetUpdateRequest.

        Name of the trust ruleset. Searchable as String.  # noqa: E501

        :param name: The name of this TrustRulesetUpdateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this TrustRulesetUpdateRequest.  # noqa: E501

        Description of the trust ruleset. Searchable as String.  # noqa: E501

        :return: The description of this TrustRulesetUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TrustRulesetUpdateRequest.

        Description of the trust ruleset. Searchable as String.  # noqa: E501

        :param description: The description of this TrustRulesetUpdateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def rule_ids(self):
        """Gets the rule_ids of this TrustRulesetUpdateRequest.  # noqa: E501

        List of rule Ids.  # noqa: E501

        :return: The rule_ids of this TrustRulesetUpdateRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this TrustRulesetUpdateRequest.

        List of rule Ids.  # noqa: E501

        :param rule_ids: The rule_ids of this TrustRulesetUpdateRequest.  # noqa: E501
        :type: list[int]
        """

        self._rule_ids = rule_ids

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
        if issubclass(TrustRulesetUpdateRequest, dict):
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
        if not isinstance(other, TrustRulesetUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

