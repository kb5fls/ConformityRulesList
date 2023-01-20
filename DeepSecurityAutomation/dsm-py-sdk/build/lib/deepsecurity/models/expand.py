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


class Expand(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    none = "none"
    all = "all"
    computer_status = "computerStatus"
    tasks = "tasks"
    security_updates = "securityUpdates"
    computer_settings = "computerSettings"
    all_security_modules = "allSecurityModules"
    anti_malware = "antiMalware"
    web_reputation = "webReputation"
    activity_monitoring = "activityMonitoring"
    firewall = "firewall"
    intrusion_prevention = "intrusionPrevention"
    integrity_monitoring = "integrityMonitoring"
    log_inspection = "logInspection"
    application_control = "applicationControl"
    sap = "SAP"
    interfaces = "interfaces"
    esx_summary = "ESXSummary"
    all_virtual_machine_summaries = "allVirtualMachineSummaries"
    azure_arm_virtual_machine_summary = "azureARMVirtualMachineSummary"
    azure_vm_virtual_machine_summary = "azureVMVirtualMachineSummary"
    ec2_virtual_machine_summary = "ec2VirtualMachineSummary"
    no_connector_virtual_machine_summary = "noConnectorVirtualMachineSummary"
    vmware_vm_virtual_machine_summary = "vmwareVMVirtualMachineSummary"
    vcloud_vm_virtual_machine_summary = "vcloudVMVirtualMachineSummary"
    workspace_virtual_machine_summary = "workspaceVirtualMachineSummary"
    gcp_virtual_machine_summary = "gcpVirtualMachineSummary"

    def __init__(self, *args):  # noqa: E501
        """Expand - a model defined in Swagger"""  # noqa: E501
        self._options_set = set()
        self.add(*args)

    def add(self, *args):
        allowed_values = ["none", "all", "computerStatus", "tasks", "securityUpdates", "computerSettings", "allSecurityModules", "antiMalware", "webReputation", "activityMonitoring", "firewall", "intrusionPrevention", "integrityMonitoring", "logInspection", "applicationControl", "SAP", "interfaces", "ESXSummary", "allVirtualMachineSummaries", "azureARMVirtualMachineSummary", "azureVMVirtualMachineSummary", "ec2VirtualMachineSummary", "noConnectorVirtualMachineSummary", "vmwareVMVirtualMachineSummary", "vcloudVMVirtualMachineSummary", "workspaceVirtualMachineSummary", "gcpVirtualMachineSummary"]

        if not set(args).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(args) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._options_set.update(args)

    def delete(self, *args):
        for x in args:
            self._options_set.discard(x)

    def clear(self):
        self._options_set.clear()

    def list(self):
        return list(self._options_set)


