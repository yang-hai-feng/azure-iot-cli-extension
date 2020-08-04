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

try:
    from .model_information_py3 import ModelInformation
    from .service_error_py3 import ServiceError
    from .model_search_options_py3 import ModelSearchOptions
except (SyntaxError, ImportError):
    from .model_information import ModelInformation
    from .service_error import ServiceError
    from .model_search_options import ModelSearchOptions

__all__ = [
    'ModelInformation',
    'ServiceError',
    'ModelSearchOptions',
]