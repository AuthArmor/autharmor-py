# coding: utf-8

"""
    Autharmor

    Auth Armor - Auth Anywhere API

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from pydantic import StrictInt, StrictStr

from typing import Optional

from autharmor_python.models.get_user_auth_history_response import GetUserAuthHistoryResponse
from autharmor_python.models.get_user_response import GetUserResponse
from autharmor_python.models.get_users_response import GetUsersResponse
from autharmor_python.models.update_user_request import UpdateUserRequest
from autharmor_python.models.user import User

from autharmor_python.api_client import ApiClient
from autharmor_python.api_response import ApiResponse
from autharmor_python.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UsersApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def v4_users_get(self, username : Optional[StrictStr] = None, page_number : Optional[StrictInt] = None, page_size : Optional[StrictInt] = None, sort_direction : Optional[StrictStr] = None, sort_column : Optional[StrictStr] = None, **kwargs) -> GetUsersResponse:  # noqa: E501
        """  Get Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v4_users_get(username, page_number, page_size, sort_direction, sort_column, async_req=True)
        >>> result = thread.get()

        :param username:
        :type username: str
        :param page_number:
        :type page_number: int
        :param page_size:
        :type page_size: int
        :param sort_direction:
        :type sort_direction: str
        :param sort_column:
        :type sort_column: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetUsersResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the v4_users_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.v4_users_get_with_http_info(username, page_number, page_size, sort_direction, sort_column, **kwargs)  # noqa: E501

    @validate_arguments
    def v4_users_get_with_http_info(self, username : Optional[StrictStr] = None, page_number : Optional[StrictInt] = None, page_size : Optional[StrictInt] = None, sort_direction : Optional[StrictStr] = None, sort_column : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """  Get Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v4_users_get_with_http_info(username, page_number, page_size, sort_direction, sort_column, async_req=True)
        >>> result = thread.get()

        :param username:
        :type username: str
        :param page_number:
        :type page_number: int
        :param page_size:
        :type page_size: int
        :param sort_direction:
        :type sort_direction: str
        :param sort_column:
        :type sort_column: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetUsersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'username',
            'page_number',
            'page_size',
            'sort_direction',
            'sort_column'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v4_users_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('username') is not None:  # noqa: E501
            _query_params.append(('username', _params['username']))

        if _params.get('page_number') is not None:  # noqa: E501
            _query_params.append(('page_number', _params['page_number']))

        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('page_size', _params['page_size']))

        if _params.get('sort_direction') is not None:  # noqa: E501
            _query_params.append(('sort_direction', _params['sort_direction']))

        if _params.get('sort_column') is not None:  # noqa: E501
            _query_params.append(('sort_column', _params['sort_column']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "GetUsersResponse",
            '401': None,
            '403': None,
        }

        return self.api_client.call_api(
            '/v4/users', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def v4_users_user_id_auth_history_get(self, user_id : StrictStr, username : Optional[StrictStr] = None, page_number : Optional[StrictInt] = None, page_size : Optional[StrictInt] = None, sort_direction : Optional[StrictStr] = None, sort_column : Optional[StrictStr] = None, **kwargs) -> GetUserAuthHistoryResponse:  # noqa: E501
        """  Get Auth History for User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v4_users_user_id_auth_history_get(user_id, username, page_number, page_size, sort_direction, sort_column, async_req=True)
        >>> result = thread.get()

        :param user_id: (required)
        :type user_id: str
        :param username:
        :type username: str
        :param page_number:
        :type page_number: int
        :param page_size:
        :type page_size: int
        :param sort_direction:
        :type sort_direction: str
        :param sort_column:
        :type sort_column: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetUserAuthHistoryResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the v4_users_user_id_auth_history_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.v4_users_user_id_auth_history_get_with_http_info(user_id, username, page_number, page_size, sort_direction, sort_column, **kwargs)  # noqa: E501

    @validate_arguments
    def v4_users_user_id_auth_history_get_with_http_info(self, user_id : StrictStr, username : Optional[StrictStr] = None, page_number : Optional[StrictInt] = None, page_size : Optional[StrictInt] = None, sort_direction : Optional[StrictStr] = None, sort_column : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """  Get Auth History for User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v4_users_user_id_auth_history_get_with_http_info(user_id, username, page_number, page_size, sort_direction, sort_column, async_req=True)
        >>> result = thread.get()

        :param user_id: (required)
        :type user_id: str
        :param username:
        :type username: str
        :param page_number:
        :type page_number: int
        :param page_size:
        :type page_size: int
        :param sort_direction:
        :type sort_direction: str
        :param sort_column:
        :type sort_column: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetUserAuthHistoryResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'user_id',
            'username',
            'page_number',
            'page_size',
            'sort_direction',
            'sort_column'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v4_users_user_id_auth_history_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['user_id']:
            _path_params['user_id'] = _params['user_id']


        # process the query parameters
        _query_params = []
        if _params.get('username') is not None:  # noqa: E501
            _query_params.append(('username', _params['username']))

        if _params.get('page_number') is not None:  # noqa: E501
            _query_params.append(('page_number', _params['page_number']))

        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('page_size', _params['page_size']))

        if _params.get('sort_direction') is not None:  # noqa: E501
            _query_params.append(('sort_direction', _params['sort_direction']))

        if _params.get('sort_column') is not None:  # noqa: E501
            _query_params.append(('sort_column', _params['sort_column']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "GetUserAuthHistoryResponse",
            '401': None,
            '403': None,
        }

        return self.api_client.call_api(
            '/v4/users/{user_id}/auth_history', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def v4_users_user_id_get(self, user_id : StrictStr, username : Optional[StrictStr] = None, **kwargs) -> GetUserResponse:  # noqa: E501
        """  Get User By Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v4_users_user_id_get(user_id, username, async_req=True)
        >>> result = thread.get()

        :param user_id: (required)
        :type user_id: str
        :param username:
        :type username: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetUserResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the v4_users_user_id_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.v4_users_user_id_get_with_http_info(user_id, username, **kwargs)  # noqa: E501

    @validate_arguments
    def v4_users_user_id_get_with_http_info(self, user_id : StrictStr, username : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """  Get User By Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v4_users_user_id_get_with_http_info(user_id, username, async_req=True)
        >>> result = thread.get()

        :param user_id: (required)
        :type user_id: str
        :param username:
        :type username: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetUserResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'user_id',
            'username'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v4_users_user_id_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['user_id']:
            _path_params['user_id'] = _params['user_id']


        # process the query parameters
        _query_params = []
        if _params.get('username') is not None:  # noqa: E501
            _query_params.append(('username', _params['username']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "GetUserResponse",
            '401': None,
            '403': None,
        }

        return self.api_client.call_api(
            '/v4/users/{user_id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def v4_users_user_id_put(self, user_id : StrictStr, username : Optional[StrictStr] = None, update_user_request : Optional[UpdateUserRequest] = None, **kwargs) -> User:  # noqa: E501
        """  Update User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v4_users_user_id_put(user_id, username, update_user_request, async_req=True)
        >>> result = thread.get()

        :param user_id: (required)
        :type user_id: str
        :param username:
        :type username: str
        :param update_user_request:
        :type update_user_request: UpdateUserRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: User
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the v4_users_user_id_put_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.v4_users_user_id_put_with_http_info(user_id, username, update_user_request, **kwargs)  # noqa: E501

    @validate_arguments
    def v4_users_user_id_put_with_http_info(self, user_id : StrictStr, username : Optional[StrictStr] = None, update_user_request : Optional[UpdateUserRequest] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """  Update User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v4_users_user_id_put_with_http_info(user_id, username, update_user_request, async_req=True)
        >>> result = thread.get()

        :param user_id: (required)
        :type user_id: str
        :param username:
        :type username: str
        :param update_user_request:
        :type update_user_request: UpdateUserRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(User, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'user_id',
            'username',
            'update_user_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v4_users_user_id_put" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['user_id']:
            _path_params['user_id'] = _params['user_id']


        # process the query parameters
        _query_params = []
        if _params.get('username') is not None:  # noqa: E501
            _query_params.append(('username', _params['username']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_user_request'] is not None:
            _body_params = _params['update_user_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "User",
            '401': None,
            '403': None,
        }

        return self.api_client.call_api(
            '/v4/users/{user_id}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
