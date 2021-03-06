# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CommandModel(Model):
    """CommandModel.

    :param request_schema:
    :type request_schema: ~product.models.SchemaField
    :param response_schema:
    :type response_schema: ~product.models.SchemaField
    :param command_execution_type: Possible values include: 'Synchronous',
     'Asynchronous'
    :type command_execution_type: str or ~product.models.enum
    :param name:
    :type name: str
    :param comment:
    :type comment: str
    :param display_name:
    :type display_name: dict[str, str]
    :param id:
    :type id: str
    :param description:
    :type description: dict[str, str]
    :param language_version:
    :type language_version: int
    """

    _attribute_map = {
        'request_schema': {'key': 'requestSchema', 'type': 'SchemaField'},
        'response_schema': {'key': 'responseSchema', 'type': 'SchemaField'},
        'command_execution_type': {'key': 'commandExecutionType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'description', 'type': '{str}'},
        'language_version': {'key': 'languageVersion', 'type': 'int'},
    }

    def __init__(self, *, request_schema=None, response_schema=None, command_execution_type=None, name: str=None, comment: str=None, display_name=None, id: str=None, description=None, language_version: int=None, **kwargs) -> None:
        super(CommandModel, self).__init__(**kwargs)
        self.request_schema = request_schema
        self.response_schema = response_schema
        self.command_execution_type = command_execution_type
        self.name = name
        self.comment = comment
        self.display_name = display_name
        self.id = id
        self.description = description
        self.language_version = language_version
