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

from deepsecurity.models.activity_monitoring_policy_extension import ActivityMonitoringPolicyExtension  # noqa: F401,E501
from deepsecurity.models.anti_malware_policy_extension import AntiMalwarePolicyExtension  # noqa: F401,E501
from deepsecurity.models.application_control_policy_extension import ApplicationControlPolicyExtension  # noqa: F401,E501
from deepsecurity.models.firewall_policy_extension import FirewallPolicyExtension  # noqa: F401,E501
from deepsecurity.models.integrity_monitoring_policy_extension import IntegrityMonitoringPolicyExtension  # noqa: F401,E501
from deepsecurity.models.interface_types import InterfaceTypes  # noqa: F401,E501
from deepsecurity.models.intrusion_prevention_policy_extension import IntrusionPreventionPolicyExtension  # noqa: F401,E501
from deepsecurity.models.log_inspection_policy_extension import LogInspectionPolicyExtension  # noqa: F401,E501
from deepsecurity.models.policy_settings import PolicySettings  # noqa: F401,E501
from deepsecurity.models.sap_policy_extension import SAPPolicyExtension  # noqa: F401,E501
from deepsecurity.models.web_reputation_policy_extension import WebReputationPolicyExtension  # noqa: F401,E501


class Policy(object):
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
        'parent_id': 'int',
        'name': 'str',
        'description': 'str',
        'policy_settings': 'PolicySettings',
        'recommendation_scan_mode': 'str',
        'auto_requires_update': 'str',
        'interface_types': 'InterfaceTypes',
        'id': 'int',
        'anti_malware': 'AntiMalwarePolicyExtension',
        'web_reputation': 'WebReputationPolicyExtension',
        'activity_monitoring': 'ActivityMonitoringPolicyExtension',
        'firewall': 'FirewallPolicyExtension',
        'intrusion_prevention': 'IntrusionPreventionPolicyExtension',
        'integrity_monitoring': 'IntegrityMonitoringPolicyExtension',
        'log_inspection': 'LogInspectionPolicyExtension',
        'application_control': 'ApplicationControlPolicyExtension',
        'sap': 'SAPPolicyExtension'
    }

    attribute_map = {
        'parent_id': 'parentID',
        'name': 'name',
        'description': 'description',
        'policy_settings': 'policySettings',
        'recommendation_scan_mode': 'recommendationScanMode',
        'auto_requires_update': 'autoRequiresUpdate',
        'interface_types': 'interfaceTypes',
        'id': 'ID',
        'anti_malware': 'antiMalware',
        'web_reputation': 'webReputation',
        'activity_monitoring': 'activityMonitoring',
        'firewall': 'firewall',
        'intrusion_prevention': 'intrusionPrevention',
        'integrity_monitoring': 'integrityMonitoring',
        'log_inspection': 'logInspection',
        'application_control': 'applicationControl',
        'sap': 'SAP'
    }

    def __init__(self, parent_id=None, name=None, description=None, policy_settings=None, recommendation_scan_mode=None, auto_requires_update=None, interface_types=None, id=None, anti_malware=None, web_reputation=None, activity_monitoring=None, firewall=None, intrusion_prevention=None, integrity_monitoring=None, log_inspection=None, application_control=None, sap=None):  # noqa: E501
        """Policy - a model defined in Swagger"""  # noqa: E501

        self._parent_id = None
        self._name = None
        self._description = None
        self._policy_settings = None
        self._recommendation_scan_mode = None
        self._auto_requires_update = None
        self._interface_types = None
        self._id = None
        self._anti_malware = None
        self._web_reputation = None
        self._activity_monitoring = None
        self._firewall = None
        self._intrusion_prevention = None
        self._integrity_monitoring = None
        self._log_inspection = None
        self._application_control = None
        self._sap = None
        self.discriminator = None

        if parent_id is not None:
            self.parent_id = parent_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if policy_settings is not None:
            self.policy_settings = policy_settings
        if recommendation_scan_mode is not None:
            self.recommendation_scan_mode = recommendation_scan_mode
        if auto_requires_update is not None:
            self.auto_requires_update = auto_requires_update
        if interface_types is not None:
            self.interface_types = interface_types
        if id is not None:
            self.id = id
        if anti_malware is not None:
            self.anti_malware = anti_malware
        if web_reputation is not None:
            self.web_reputation = web_reputation
        if activity_monitoring is not None:
            self.activity_monitoring = activity_monitoring
        if firewall is not None:
            self.firewall = firewall
        if intrusion_prevention is not None:
            self.intrusion_prevention = intrusion_prevention
        if integrity_monitoring is not None:
            self.integrity_monitoring = integrity_monitoring
        if log_inspection is not None:
            self.log_inspection = log_inspection
        if application_control is not None:
            self.application_control = application_control
        if sap is not None:
            self.sap = sap

    @property
    def parent_id(self):
        """Gets the parent_id of this Policy.  # noqa: E501

        ID of the parent policy. Searchable as Numeric.  # noqa: E501

        :return: The parent_id of this Policy.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Policy.

        ID of the parent policy. Searchable as Numeric.  # noqa: E501

        :param parent_id: The parent_id of this Policy.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this Policy.  # noqa: E501

        Name of the policy. Searchable as String.  # noqa: E501

        :return: The name of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Policy.

        Name of the policy. Searchable as String.  # noqa: E501

        :param name: The name of this Policy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Policy.  # noqa: E501

        Description of the policy. Searchable as String.  # noqa: E501

        :return: The description of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Policy.

        Description of the policy. Searchable as String.  # noqa: E501

        :param description: The description of this Policy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def policy_settings(self):
        """Gets the policy_settings of this Policy.  # noqa: E501

        All configurable policy settings.  # noqa: E501

        :return: The policy_settings of this Policy.  # noqa: E501
        :rtype: PolicySettings
        """
        return self._policy_settings

    @policy_settings.setter
    def policy_settings(self, policy_settings):
        """Sets the policy_settings of this Policy.

        All configurable policy settings.  # noqa: E501

        :param policy_settings: The policy_settings of this Policy.  # noqa: E501
        :type: PolicySettings
        """

        self._policy_settings = policy_settings

    @property
    def recommendation_scan_mode(self):
        """Gets the recommendation_scan_mode of this Policy.  # noqa: E501

        Enable or disable ongoing recommendation scans for computers assigned this policy. Searchable as Choice.  # noqa: E501

        :return: The recommendation_scan_mode of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._recommendation_scan_mode

    @recommendation_scan_mode.setter
    def recommendation_scan_mode(self, recommendation_scan_mode):
        """Sets the recommendation_scan_mode of this Policy.

        Enable or disable ongoing recommendation scans for computers assigned this policy. Searchable as Choice.  # noqa: E501

        :param recommendation_scan_mode: The recommendation_scan_mode of this Policy.  # noqa: E501
        :type: str
        """
        allowed_values = ["off", "ongoing"]  # noqa: E501
        if recommendation_scan_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `recommendation_scan_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(recommendation_scan_mode, allowed_values)
            )

        self._recommendation_scan_mode = recommendation_scan_mode

    @property
    def auto_requires_update(self):
        """Gets the auto_requires_update of this Policy.  # noqa: E501

        Automatically update computers assigned this policy when the configuration changes. Searchable as Choice.  # noqa: E501

        :return: The auto_requires_update of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._auto_requires_update

    @auto_requires_update.setter
    def auto_requires_update(self, auto_requires_update):
        """Sets the auto_requires_update of this Policy.

        Automatically update computers assigned this policy when the configuration changes. Searchable as Choice.  # noqa: E501

        :param auto_requires_update: The auto_requires_update of this Policy.  # noqa: E501
        :type: str
        """
        allowed_values = ["off", "on"]  # noqa: E501
        if auto_requires_update not in allowed_values:
            raise ValueError(
                "Invalid value for `auto_requires_update` ({0}), must be one of {1}"  # noqa: E501
                .format(auto_requires_update, allowed_values)
            )

        self._auto_requires_update = auto_requires_update

    @property
    def interface_types(self):
        """Gets the interface_types of this Policy.  # noqa: E501

        When \"Rules can apply to specific interfaces\" is selected, Deep Security will map the network interfaces detected on a computer to the types in this list.  # noqa: E501

        :return: The interface_types of this Policy.  # noqa: E501
        :rtype: InterfaceTypes
        """
        return self._interface_types

    @interface_types.setter
    def interface_types(self, interface_types):
        """Sets the interface_types of this Policy.

        When \"Rules can apply to specific interfaces\" is selected, Deep Security will map the network interfaces detected on a computer to the types in this list.  # noqa: E501

        :param interface_types: The interface_types of this Policy.  # noqa: E501
        :type: InterfaceTypes
        """

        self._interface_types = interface_types

    @property
    def id(self):
        """Gets the id of this Policy.  # noqa: E501

        ID of the policy. Searchable as ID.  # noqa: E501

        :return: The id of this Policy.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Policy.

        ID of the policy. Searchable as ID.  # noqa: E501

        :param id: The id of this Policy.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def anti_malware(self):
        """Gets the anti_malware of this Policy.  # noqa: E501

        Configuration for the Anti-Malware module.  # noqa: E501

        :return: The anti_malware of this Policy.  # noqa: E501
        :rtype: AntiMalwarePolicyExtension
        """
        return self._anti_malware

    @anti_malware.setter
    def anti_malware(self, anti_malware):
        """Sets the anti_malware of this Policy.

        Configuration for the Anti-Malware module.  # noqa: E501

        :param anti_malware: The anti_malware of this Policy.  # noqa: E501
        :type: AntiMalwarePolicyExtension
        """

        self._anti_malware = anti_malware

    @property
    def web_reputation(self):
        """Gets the web_reputation of this Policy.  # noqa: E501

        Configuration for the Web Reputation module.  # noqa: E501

        :return: The web_reputation of this Policy.  # noqa: E501
        :rtype: WebReputationPolicyExtension
        """
        return self._web_reputation

    @web_reputation.setter
    def web_reputation(self, web_reputation):
        """Sets the web_reputation of this Policy.

        Configuration for the Web Reputation module.  # noqa: E501

        :param web_reputation: The web_reputation of this Policy.  # noqa: E501
        :type: WebReputationPolicyExtension
        """

        self._web_reputation = web_reputation

    @property
    def activity_monitoring(self):
        """Gets the activity_monitoring of this Policy.  # noqa: E501

        Configuration for the Activity Monitoring module.  # noqa: E501

        :return: The activity_monitoring of this Policy.  # noqa: E501
        :rtype: ActivityMonitoringPolicyExtension
        """
        return self._activity_monitoring

    @activity_monitoring.setter
    def activity_monitoring(self, activity_monitoring):
        """Sets the activity_monitoring of this Policy.

        Configuration for the Activity Monitoring module.  # noqa: E501

        :param activity_monitoring: The activity_monitoring of this Policy.  # noqa: E501
        :type: ActivityMonitoringPolicyExtension
        """

        self._activity_monitoring = activity_monitoring

    @property
    def firewall(self):
        """Gets the firewall of this Policy.  # noqa: E501

        Configuration for the Firewall module.  # noqa: E501

        :return: The firewall of this Policy.  # noqa: E501
        :rtype: FirewallPolicyExtension
        """
        return self._firewall

    @firewall.setter
    def firewall(self, firewall):
        """Sets the firewall of this Policy.

        Configuration for the Firewall module.  # noqa: E501

        :param firewall: The firewall of this Policy.  # noqa: E501
        :type: FirewallPolicyExtension
        """

        self._firewall = firewall

    @property
    def intrusion_prevention(self):
        """Gets the intrusion_prevention of this Policy.  # noqa: E501

        Configuration for the Intrusion Prevention module.  # noqa: E501

        :return: The intrusion_prevention of this Policy.  # noqa: E501
        :rtype: IntrusionPreventionPolicyExtension
        """
        return self._intrusion_prevention

    @intrusion_prevention.setter
    def intrusion_prevention(self, intrusion_prevention):
        """Sets the intrusion_prevention of this Policy.

        Configuration for the Intrusion Prevention module.  # noqa: E501

        :param intrusion_prevention: The intrusion_prevention of this Policy.  # noqa: E501
        :type: IntrusionPreventionPolicyExtension
        """

        self._intrusion_prevention = intrusion_prevention

    @property
    def integrity_monitoring(self):
        """Gets the integrity_monitoring of this Policy.  # noqa: E501

        Configuration for the Integrity Monitoring module.  # noqa: E501

        :return: The integrity_monitoring of this Policy.  # noqa: E501
        :rtype: IntegrityMonitoringPolicyExtension
        """
        return self._integrity_monitoring

    @integrity_monitoring.setter
    def integrity_monitoring(self, integrity_monitoring):
        """Sets the integrity_monitoring of this Policy.

        Configuration for the Integrity Monitoring module.  # noqa: E501

        :param integrity_monitoring: The integrity_monitoring of this Policy.  # noqa: E501
        :type: IntegrityMonitoringPolicyExtension
        """

        self._integrity_monitoring = integrity_monitoring

    @property
    def log_inspection(self):
        """Gets the log_inspection of this Policy.  # noqa: E501

        Configuration for the Log Inspection module.  # noqa: E501

        :return: The log_inspection of this Policy.  # noqa: E501
        :rtype: LogInspectionPolicyExtension
        """
        return self._log_inspection

    @log_inspection.setter
    def log_inspection(self, log_inspection):
        """Sets the log_inspection of this Policy.

        Configuration for the Log Inspection module.  # noqa: E501

        :param log_inspection: The log_inspection of this Policy.  # noqa: E501
        :type: LogInspectionPolicyExtension
        """

        self._log_inspection = log_inspection

    @property
    def application_control(self):
        """Gets the application_control of this Policy.  # noqa: E501

        Configuration for the Application Control module.  # noqa: E501

        :return: The application_control of this Policy.  # noqa: E501
        :rtype: ApplicationControlPolicyExtension
        """
        return self._application_control

    @application_control.setter
    def application_control(self, application_control):
        """Sets the application_control of this Policy.

        Configuration for the Application Control module.  # noqa: E501

        :param application_control: The application_control of this Policy.  # noqa: E501
        :type: ApplicationControlPolicyExtension
        """

        self._application_control = application_control

    @property
    def sap(self):
        """Gets the sap of this Policy.  # noqa: E501


        :return: The sap of this Policy.  # noqa: E501
        :rtype: SAPPolicyExtension
        """
        return self._sap

    @sap.setter
    def sap(self, sap):
        """Sets the sap of this Policy.


        :param sap: The sap of this Policy.  # noqa: E501
        :type: SAPPolicyExtension
        """

        self._sap = sap

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
        if issubclass(Policy, dict):
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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

