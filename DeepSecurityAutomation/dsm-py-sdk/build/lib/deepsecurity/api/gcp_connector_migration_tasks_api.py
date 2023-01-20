# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2022 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.686
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsecurity.api_client import ApiClient


class GCPConnectorMigrationTasksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_connector_migration_task2(self, connector_migration_task, api_version, **kwargs):  # noqa: E501
        """Create a Connector Migration Task  # noqa: E501

        Create a new GCP Connector Migration Task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_connector_migration_task2(connector_migration_task, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectorMigrationTask connector_migration_task: The task to migrate the connector. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ConnectorMigrationTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_connector_migration_task2_with_http_info(connector_migration_task, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_connector_migration_task2_with_http_info(connector_migration_task, api_version, **kwargs)  # noqa: E501
            return data

    def create_connector_migration_task2_with_http_info(self, connector_migration_task, api_version, **kwargs):  # noqa: E501
        """Create a Connector Migration Task  # noqa: E501

        Create a new GCP Connector Migration Task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_connector_migration_task2_with_http_info(connector_migration_task, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectorMigrationTask connector_migration_task: The task to migrate the connector. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ConnectorMigrationTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connector_migration_task', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_connector_migration_task2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connector_migration_task' is set
        if ('connector_migration_task' not in params or
                params['connector_migration_task'] is None):
            raise ValueError("Missing the required parameter `connector_migration_task` when calling `create_connector_migration_task2`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_connector_migration_task2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'connector_migration_task' in params:
            body_params = params['connector_migration_task']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/connectormigrationtasks/gcp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectorMigrationTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_connector_migration_tasks2(self, connector_ids, api_version, **kwargs):  # noqa: E501
        """Create Connector Migration Tasks  # noqa: E501

        Create new GCP Connector Migration Tasks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_connector_migration_tasks2(connector_ids, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchConnectorMigrationTask connector_ids: Connector IDs to be migrated. (required)
        :param str api_version: The version of the api being called. (required)
        :return: BatchConnectorMigrationTaskList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_connector_migration_tasks2_with_http_info(connector_ids, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_connector_migration_tasks2_with_http_info(connector_ids, api_version, **kwargs)  # noqa: E501
            return data

    def create_connector_migration_tasks2_with_http_info(self, connector_ids, api_version, **kwargs):  # noqa: E501
        """Create Connector Migration Tasks  # noqa: E501

        Create new GCP Connector Migration Tasks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_connector_migration_tasks2_with_http_info(connector_ids, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchConnectorMigrationTask connector_ids: Connector IDs to be migrated. (required)
        :param str api_version: The version of the api being called. (required)
        :return: BatchConnectorMigrationTaskList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connector_ids', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_connector_migration_tasks2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connector_ids' is set
        if ('connector_ids' not in params or
                params['connector_ids'] is None):
            raise ValueError("Missing the required parameter `connector_ids` when calling `create_connector_migration_tasks2`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_connector_migration_tasks2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'connector_ids' in params:
            body_params = params['connector_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/batchconnectormigrationtasks/gcp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchConnectorMigrationTaskList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def describe_connector_migration_task2(self, connector_migration_task_id, api_version, **kwargs):  # noqa: E501
        """Describe a Connector Migration Task  # noqa: E501

        Describe an GCP connector migration task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_connector_migration_task2(connector_migration_task_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int connector_migration_task_id: The ID number of the connector migration task to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ConnectorMigrationTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_connector_migration_task2_with_http_info(connector_migration_task_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_connector_migration_task2_with_http_info(connector_migration_task_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_connector_migration_task2_with_http_info(self, connector_migration_task_id, api_version, **kwargs):  # noqa: E501
        """Describe a Connector Migration Task  # noqa: E501

        Describe an GCP connector migration task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_connector_migration_task2_with_http_info(connector_migration_task_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int connector_migration_task_id: The ID number of the connector migration task to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ConnectorMigrationTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connector_migration_task_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_connector_migration_task2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connector_migration_task_id' is set
        if ('connector_migration_task_id' not in params or
                params['connector_migration_task_id'] is None):
            raise ValueError("Missing the required parameter `connector_migration_task_id` when calling `describe_connector_migration_task2`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_connector_migration_task2`")  # noqa: E501

        if 'connector_migration_task_id' in params and not re.search('\\d+', str(params['connector_migration_task_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `connector_migration_task_id` when calling `describe_connector_migration_task2`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'connector_migration_task_id' in params:
            path_params['connectorMigrationTaskID'] = params['connector_migration_task_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/connectormigrationtasks/gcp/{connectorMigrationTaskID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectorMigrationTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_connector_migration_tasks2(self, api_version, **kwargs):  # noqa: E501
        """List Connector Migration Tasks  # noqa: E501

        Describe GCP connector migration tasks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_connector_migration_tasks2(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: ConnectorMigrationTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_connector_migration_tasks2_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_connector_migration_tasks2_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_connector_migration_tasks2_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List Connector Migration Tasks  # noqa: E501

        Describe GCP connector migration tasks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_connector_migration_tasks2_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: ConnectorMigrationTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_connector_migration_tasks2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_connector_migration_tasks2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/connectormigrationtasks/gcp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectorMigrationTasks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_connector_migration_tasks2(self, api_version, **kwargs):  # noqa: E501
        """Create a Connector Migration Task  # noqa: E501

        Create a new GCP Connector Migration Task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_connector_migration_tasks2(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: ConnectorMigrationTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_connector_migration_tasks2_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_connector_migration_tasks2_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def search_connector_migration_tasks2_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Create a Connector Migration Task  # noqa: E501

        Create a new GCP Connector Migration Task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_connector_migration_tasks2_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: ConnectorMigrationTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'search_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_connector_migration_tasks2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_connector_migration_tasks2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search_filter' in params:
            body_params = params['search_filter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/connectormigrationtasks/gcp/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectorMigrationTasks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
