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

from deepsecurity.models.rights import Rights  # noqa: F401,E501


class Role(object):
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
        'urn': 'str',
        'immutable': 'bool',
        'can_only_manipulate_users_with_equal_or_lesser_rights': 'bool',
        'all_computers': 'bool',
        'all_policies': 'bool',
        'allow_user_interface': 'bool',
        'allow_web_service': 'bool',
        'allow_manage_workload_security_link': 'bool',
        'allow_migration': 'bool',
        'rights': 'Rights',
        'computer_ids': 'list[int]',
        'computer_group_ids': 'list[int]',
        'policy_ids': 'list[int]',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'urn': 'urn',
        'immutable': 'immutable',
        'can_only_manipulate_users_with_equal_or_lesser_rights': 'canOnlyManipulateUsersWithEqualOrLesserRights',
        'all_computers': 'allComputers',
        'all_policies': 'allPolicies',
        'allow_user_interface': 'allowUserInterface',
        'allow_web_service': 'allowWebService',
        'allow_manage_workload_security_link': 'allowManageWorkloadSecurityLink',
        'allow_migration': 'allowMigration',
        'rights': 'rights',
        'computer_ids': 'computerIDs',
        'computer_group_ids': 'computerGroupIDs',
        'policy_ids': 'policyIDs',
        'id': 'ID'
    }

    def __init__(self, name=None, description=None, urn=None, immutable=None, can_only_manipulate_users_with_equal_or_lesser_rights=None, all_computers=None, all_policies=None, allow_user_interface=None, allow_web_service=None, allow_manage_workload_security_link=None, allow_migration=None, rights=None, computer_ids=None, computer_group_ids=None, policy_ids=None, id=None):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._urn = None
        self._immutable = None
        self._can_only_manipulate_users_with_equal_or_lesser_rights = None
        self._all_computers = None
        self._all_policies = None
        self._allow_user_interface = None
        self._allow_web_service = None
        self._allow_manage_workload_security_link = None
        self._allow_migration = None
        self._rights = None
        self._computer_ids = None
        self._computer_group_ids = None
        self._policy_ids = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if urn is not None:
            self.urn = urn
        if immutable is not None:
            self.immutable = immutable
        if can_only_manipulate_users_with_equal_or_lesser_rights is not None:
            self.can_only_manipulate_users_with_equal_or_lesser_rights = can_only_manipulate_users_with_equal_or_lesser_rights
        if all_computers is not None:
            self.all_computers = all_computers
        if all_policies is not None:
            self.all_policies = all_policies
        if allow_user_interface is not None:
            self.allow_user_interface = allow_user_interface
        if allow_web_service is not None:
            self.allow_web_service = allow_web_service
        if allow_manage_workload_security_link is not None:
            self.allow_manage_workload_security_link = allow_manage_workload_security_link
        if allow_migration is not None:
            self.allow_migration = allow_migration
        if rights is not None:
            self.rights = rights
        if computer_ids is not None:
            self.computer_ids = computer_ids
        if computer_group_ids is not None:
            self.computer_group_ids = computer_group_ids
        if policy_ids is not None:
            self.policy_ids = policy_ids
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this Role.  # noqa: E501

        Name of the administrator role. Searchable as String.  # noqa: E501

        :return: The name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Role.

        Name of the administrator role. Searchable as String.  # noqa: E501

        :param name: The name of this Role.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Role.  # noqa: E501

        Description of the administrator role. Searchable as String.  # noqa: E501

        :return: The description of this Role.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Role.

        Description of the administrator role. Searchable as String.  # noqa: E501

        :param description: The description of this Role.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def urn(self):
        """Gets the urn of this Role.  # noqa: E501

        Uniform resource name.  # noqa: E501

        :return: The urn of this Role.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this Role.

        Uniform resource name.  # noqa: E501

        :param urn: The urn of this Role.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def immutable(self):
        """Gets the immutable of this Role.  # noqa: E501

        The default immutable role in Deep Security Manager.  # noqa: E501

        :return: The immutable of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._immutable

    @immutable.setter
    def immutable(self, immutable):
        """Sets the immutable of this Role.

        The default immutable role in Deep Security Manager.  # noqa: E501

        :param immutable: The immutable of this Role.  # noqa: E501
        :type: bool
        """

        self._immutable = immutable

    @property
    def can_only_manipulate_users_with_equal_or_lesser_rights(self):
        """Gets the can_only_manipulate_users_with_equal_or_lesser_rights of this Role.  # noqa: E501

        Controls whether or not the role can only manipulate users with equal or lesser rights. Searchable as Boolean.  # noqa: E501

        :return: The can_only_manipulate_users_with_equal_or_lesser_rights of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._can_only_manipulate_users_with_equal_or_lesser_rights

    @can_only_manipulate_users_with_equal_or_lesser_rights.setter
    def can_only_manipulate_users_with_equal_or_lesser_rights(self, can_only_manipulate_users_with_equal_or_lesser_rights):
        """Sets the can_only_manipulate_users_with_equal_or_lesser_rights of this Role.

        Controls whether or not the role can only manipulate users with equal or lesser rights. Searchable as Boolean.  # noqa: E501

        :param can_only_manipulate_users_with_equal_or_lesser_rights: The can_only_manipulate_users_with_equal_or_lesser_rights of this Role.  # noqa: E501
        :type: bool
        """

        self._can_only_manipulate_users_with_equal_or_lesser_rights = can_only_manipulate_users_with_equal_or_lesser_rights

    @property
    def all_computers(self):
        """Gets the all_computers of this Role.  # noqa: E501

        Controls whether or not the role is allowed to access all computers. Searchable as Boolean.  # noqa: E501

        :return: The all_computers of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._all_computers

    @all_computers.setter
    def all_computers(self, all_computers):
        """Sets the all_computers of this Role.

        Controls whether or not the role is allowed to access all computers. Searchable as Boolean.  # noqa: E501

        :param all_computers: The all_computers of this Role.  # noqa: E501
        :type: bool
        """

        self._all_computers = all_computers

    @property
    def all_policies(self):
        """Gets the all_policies of this Role.  # noqa: E501

        Controls whether or not the role is allowed to access all policies. Searchable as Boolean.  # noqa: E501

        :return: The all_policies of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._all_policies

    @all_policies.setter
    def all_policies(self, all_policies):
        """Sets the all_policies of this Role.

        Controls whether or not the role is allowed to access all policies. Searchable as Boolean.  # noqa: E501

        :param all_policies: The all_policies of this Role.  # noqa: E501
        :type: bool
        """

        self._all_policies = all_policies

    @property
    def allow_user_interface(self):
        """Gets the allow_user_interface of this Role.  # noqa: E501

        Controls whether or not the role is allowed to use the user interface. Searchable as Boolean.  # noqa: E501

        :return: The allow_user_interface of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._allow_user_interface

    @allow_user_interface.setter
    def allow_user_interface(self, allow_user_interface):
        """Sets the allow_user_interface of this Role.

        Controls whether or not the role is allowed to use the user interface. Searchable as Boolean.  # noqa: E501

        :param allow_user_interface: The allow_user_interface of this Role.  # noqa: E501
        :type: bool
        """

        self._allow_user_interface = allow_user_interface

    @property
    def allow_web_service(self):
        """Gets the allow_web_service of this Role.  # noqa: E501

        Controls whether or not the role is allowed to use the web service API. Searchable as Boolean.  # noqa: E501

        :return: The allow_web_service of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._allow_web_service

    @allow_web_service.setter
    def allow_web_service(self, allow_web_service):
        """Sets the allow_web_service of this Role.

        Controls whether or not the role is allowed to use the web service API. Searchable as Boolean.  # noqa: E501

        :param allow_web_service: The allow_web_service of this Role.  # noqa: E501
        :type: bool
        """

        self._allow_web_service = allow_web_service

    @property
    def allow_manage_workload_security_link(self):
        """Gets the allow_manage_workload_security_link of this Role.  # noqa: E501

        Controls whether or not the role is allowed management of Workload Security Link. Searchable as Boolean.  # noqa: E501

        :return: The allow_manage_workload_security_link of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._allow_manage_workload_security_link

    @allow_manage_workload_security_link.setter
    def allow_manage_workload_security_link(self, allow_manage_workload_security_link):
        """Sets the allow_manage_workload_security_link of this Role.

        Controls whether or not the role is allowed management of Workload Security Link. Searchable as Boolean.  # noqa: E501

        :param allow_manage_workload_security_link: The allow_manage_workload_security_link of this Role.  # noqa: E501
        :type: bool
        """

        self._allow_manage_workload_security_link = allow_manage_workload_security_link

    @property
    def allow_migration(self):
        """Gets the allow_migration of this Role.  # noqa: E501

        Controls whether or not the role is allowed migration to Workload Security. Searchable as Boolean.  # noqa: E501

        :return: The allow_migration of this Role.  # noqa: E501
        :rtype: bool
        """
        return self._allow_migration

    @allow_migration.setter
    def allow_migration(self, allow_migration):
        """Sets the allow_migration of this Role.

        Controls whether or not the role is allowed migration to Workload Security. Searchable as Boolean.  # noqa: E501

        :param allow_migration: The allow_migration of this Role.  # noqa: E501
        :type: bool
        """

        self._allow_migration = allow_migration

    @property
    def rights(self):
        """Gets the rights of this Role.  # noqa: E501

        Rights that the role is granted.  # noqa: E501

        :return: The rights of this Role.  # noqa: E501
        :rtype: Rights
        """
        return self._rights

    @rights.setter
    def rights(self, rights):
        """Sets the rights of this Role.

        Rights that the role is granted.  # noqa: E501

        :param rights: The rights of this Role.  # noqa: E501
        :type: Rights
        """

        self._rights = rights

    @property
    def computer_ids(self):
        """Gets the computer_ids of this Role.  # noqa: E501

        List of computer IDs that the role can access. Ignored if 'allComputers' is true.  # noqa: E501

        :return: The computer_ids of this Role.  # noqa: E501
        :rtype: list[int]
        """
        return self._computer_ids

    @computer_ids.setter
    def computer_ids(self, computer_ids):
        """Sets the computer_ids of this Role.

        List of computer IDs that the role can access. Ignored if 'allComputers' is true.  # noqa: E501

        :param computer_ids: The computer_ids of this Role.  # noqa: E501
        :type: list[int]
        """

        self._computer_ids = computer_ids

    @property
    def computer_group_ids(self):
        """Gets the computer_group_ids of this Role.  # noqa: E501

        List of computer group IDs that the role can access. A group ID of '0' allows access to computers not in a computer group. Note that groups must be identified individually and that access to sub-groups is not automatically granted. Ignored if 'allComputers' is true.  # noqa: E501

        :return: The computer_group_ids of this Role.  # noqa: E501
        :rtype: list[int]
        """
        return self._computer_group_ids

    @computer_group_ids.setter
    def computer_group_ids(self, computer_group_ids):
        """Sets the computer_group_ids of this Role.

        List of computer group IDs that the role can access. A group ID of '0' allows access to computers not in a computer group. Note that groups must be identified individually and that access to sub-groups is not automatically granted. Ignored if 'allComputers' is true.  # noqa: E501

        :param computer_group_ids: The computer_group_ids of this Role.  # noqa: E501
        :type: list[int]
        """

        self._computer_group_ids = computer_group_ids

    @property
    def policy_ids(self):
        """Gets the policy_ids of this Role.  # noqa: E501

        List of policy IDs that the role can access. Ignored if 'allPolicies' is true.  # noqa: E501

        :return: The policy_ids of this Role.  # noqa: E501
        :rtype: list[int]
        """
        return self._policy_ids

    @policy_ids.setter
    def policy_ids(self, policy_ids):
        """Sets the policy_ids of this Role.

        List of policy IDs that the role can access. Ignored if 'allPolicies' is true.  # noqa: E501

        :param policy_ids: The policy_ids of this Role.  # noqa: E501
        :type: list[int]
        """

        self._policy_ids = policy_ids

    @property
    def id(self):
        """Gets the id of this Role.  # noqa: E501

        ID of the administrator role. Searchable as ID.  # noqa: E501

        :return: The id of this Role.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.

        ID of the administrator role. Searchable as ID.  # noqa: E501

        :param id: The id of this Role.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(Role, dict):
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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

