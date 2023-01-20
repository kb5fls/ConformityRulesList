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


class Contact(object):
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
        'phone_number': 'str',
        'mobile_number': 'str',
        'pager_number': 'str',
        'email_address': 'str',
        'locale': 'str',
        'role_id': 'int',
        'report_pdf_password_enabled': 'bool',
        'report_pdf_password': 'str',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'phone_number': 'phoneNumber',
        'mobile_number': 'mobileNumber',
        'pager_number': 'pagerNumber',
        'email_address': 'emailAddress',
        'locale': 'locale',
        'role_id': 'roleID',
        'report_pdf_password_enabled': 'reportPDFPasswordEnabled',
        'report_pdf_password': 'reportPDFPassword',
        'id': 'ID'
    }

    def __init__(self, name=None, description=None, phone_number=None, mobile_number=None, pager_number=None, email_address=None, locale=None, role_id=None, report_pdf_password_enabled=None, report_pdf_password=None, id=None):  # noqa: E501
        """Contact - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._phone_number = None
        self._mobile_number = None
        self._pager_number = None
        self._email_address = None
        self._locale = None
        self._role_id = None
        self._report_pdf_password_enabled = None
        self._report_pdf_password = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if phone_number is not None:
            self.phone_number = phone_number
        if mobile_number is not None:
            self.mobile_number = mobile_number
        if pager_number is not None:
            self.pager_number = pager_number
        if email_address is not None:
            self.email_address = email_address
        if locale is not None:
            self.locale = locale
        if role_id is not None:
            self.role_id = role_id
        if report_pdf_password_enabled is not None:
            self.report_pdf_password_enabled = report_pdf_password_enabled
        if report_pdf_password is not None:
            self.report_pdf_password = report_pdf_password
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this Contact.  # noqa: E501

        Name of the Contact. Searchable as String.  # noqa: E501

        :return: The name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Contact.

        Name of the Contact. Searchable as String.  # noqa: E501

        :param name: The name of this Contact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Contact.  # noqa: E501

        Description of the Contact. Searchable as String.  # noqa: E501

        :return: The description of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Contact.

        Description of the Contact. Searchable as String.  # noqa: E501

        :param description: The description of this Contact.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def phone_number(self):
        """Gets the phone_number of this Contact.  # noqa: E501

        Phone number of the Contact. Searchable as String.  # noqa: E501

        :return: The phone_number of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Contact.

        Phone number of the Contact. Searchable as String.  # noqa: E501

        :param phone_number: The phone_number of this Contact.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def mobile_number(self):
        """Gets the mobile_number of this Contact.  # noqa: E501

        Mobile number of the Contact. Searchable as String.  # noqa: E501

        :return: The mobile_number of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        """Sets the mobile_number of this Contact.

        Mobile number of the Contact. Searchable as String.  # noqa: E501

        :param mobile_number: The mobile_number of this Contact.  # noqa: E501
        :type: str
        """

        self._mobile_number = mobile_number

    @property
    def pager_number(self):
        """Gets the pager_number of this Contact.  # noqa: E501

        Pager number of the Contact. Searchable as String.  # noqa: E501

        :return: The pager_number of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._pager_number

    @pager_number.setter
    def pager_number(self, pager_number):
        """Sets the pager_number of this Contact.

        Pager number of the Contact. Searchable as String.  # noqa: E501

        :param pager_number: The pager_number of this Contact.  # noqa: E501
        :type: str
        """

        self._pager_number = pager_number

    @property
    def email_address(self):
        """Gets the email_address of this Contact.  # noqa: E501

        Email address of the Contact. Searchable as String.  # noqa: E501

        :return: The email_address of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Contact.

        Email address of the Contact. Searchable as String.  # noqa: E501

        :param email_address: The email_address of this Contact.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def locale(self):
        """Gets the locale of this Contact.  # noqa: E501

        Locale of the Contact.  # noqa: E501

        :return: The locale of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Contact.

        Locale of the Contact.  # noqa: E501

        :param locale: The locale of this Contact.  # noqa: E501
        :type: str
        """
        allowed_values = ["en-US", "ja-JP"]  # noqa: E501
        if locale not in allowed_values:
            raise ValueError(
                "Invalid value for `locale` ({0}), must be one of {1}"  # noqa: E501
                .format(locale, allowed_values)
            )

        self._locale = locale

    @property
    def role_id(self):
        """Gets the role_id of this Contact.  # noqa: E501

        ID of the role assigned to the Contact. Searchable as Numeric.  # noqa: E501

        :return: The role_id of this Contact.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this Contact.

        ID of the role assigned to the Contact. Searchable as Numeric.  # noqa: E501

        :param role_id: The role_id of this Contact.  # noqa: E501
        :type: int
        """

        self._role_id = role_id

    @property
    def report_pdf_password_enabled(self):
        """Gets the report_pdf_password_enabled of this Contact.  # noqa: E501

        Controls whether the reports that the Contact generates are password-protected. Set to true to password-protect, and false otherwise. Defaults to false. Searchable as Boolean.  # noqa: E501

        :return: The report_pdf_password_enabled of this Contact.  # noqa: E501
        :rtype: bool
        """
        return self._report_pdf_password_enabled

    @report_pdf_password_enabled.setter
    def report_pdf_password_enabled(self, report_pdf_password_enabled):
        """Sets the report_pdf_password_enabled of this Contact.

        Controls whether the reports that the Contact generates are password-protected. Set to true to password-protect, and false otherwise. Defaults to false. Searchable as Boolean.  # noqa: E501

        :param report_pdf_password_enabled: The report_pdf_password_enabled of this Contact.  # noqa: E501
        :type: bool
        """

        self._report_pdf_password_enabled = report_pdf_password_enabled

    @property
    def report_pdf_password(self):
        """Gets the report_pdf_password of this Contact.  # noqa: E501

        Password that protects the reports that the Contact generates. Ignored when reportPDFPasswordEnabled is false.  # noqa: E501

        :return: The report_pdf_password of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._report_pdf_password

    @report_pdf_password.setter
    def report_pdf_password(self, report_pdf_password):
        """Sets the report_pdf_password of this Contact.

        Password that protects the reports that the Contact generates. Ignored when reportPDFPasswordEnabled is false.  # noqa: E501

        :param report_pdf_password: The report_pdf_password of this Contact.  # noqa: E501
        :type: str
        """

        self._report_pdf_password = report_pdf_password

    @property
    def id(self):
        """Gets the id of this Contact.  # noqa: E501

        ID of the Contact. Searchable as ID.  # noqa: E501

        :return: The id of this Contact.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Contact.

        ID of the Contact. Searchable as ID.  # noqa: E501

        :param id: The id of this Contact.  # noqa: E501
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
        if issubclass(Contact, dict):
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
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

