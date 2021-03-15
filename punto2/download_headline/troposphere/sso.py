# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 18.6.0


from . import AWSObject
from troposphere import Tags


class Assignment(AWSObject):
    resource_type = "AWS::SSO::Assignment"

    props = {
        'InstanceArn': (str, True),
        'PermissionSetArn': (str, True),
        'PrincipalId': (str, True),
        'PrincipalType': (str, True),
        'TargetId': (str, True),
        'TargetType': (str, True),
    }


class PermissionSet(AWSObject):
    resource_type = "AWS::SSO::PermissionSet"

    props = {
        'Description': (str, False),
        'InlinePolicy': (str, False),
        'InstanceArn': (str, True),
        'ManagedPolicies': ([str], False),
        'Name': (str, True),
        'RelayStateType': (str, False),
        'SessionDuration': (str, False),
        'Tags': (Tags, False),
    }
