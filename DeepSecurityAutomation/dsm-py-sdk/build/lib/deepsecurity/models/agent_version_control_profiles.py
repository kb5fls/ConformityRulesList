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

from deepsecurity.models.agent_version_control_profile import AgentVersionControlProfile  # noqa: F401,E501


class AgentVersionControlProfiles(object):
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
        'agent_version_control_profiles': 'list[AgentVersionControlProfile]'
    }

    attribute_map = {
        'agent_version_control_profiles': 'agentVersionControlProfiles'
    }

    def __init__(self, agent_version_control_profiles=None):  # noqa: E501
        """AgentVersionControlProfiles - a model defined in Swagger"""  # noqa: E501

        self._agent_version_control_profiles = None
        self.discriminator = None

        if agent_version_control_profiles is not None:
            self.agent_version_control_profiles = agent_version_control_profiles

    @property
    def agent_version_control_profiles(self):
        """Gets the agent_version_control_profiles of this AgentVersionControlProfiles.  # noqa: E501


        :return: The agent_version_control_profiles of this AgentVersionControlProfiles.  # noqa: E501
        :rtype: list[AgentVersionControlProfile]
        """
        return self._agent_version_control_profiles

    @agent_version_control_profiles.setter
    def agent_version_control_profiles(self, agent_version_control_profiles):
        """Sets the agent_version_control_profiles of this AgentVersionControlProfiles.


        :param agent_version_control_profiles: The agent_version_control_profiles of this AgentVersionControlProfiles.  # noqa: E501
        :type: list[AgentVersionControlProfile]
        """

        self._agent_version_control_profiles = agent_version_control_profiles

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
        if issubclass(AgentVersionControlProfiles, dict):
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
        if not isinstance(other, AgentVersionControlProfiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

