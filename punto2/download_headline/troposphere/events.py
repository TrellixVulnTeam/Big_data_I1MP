# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 8.1.0


from . import AWSObject
from . import AWSProperty
from .validators import integer


class EventBus(AWSObject):
    resource_type = "AWS::Events::EventBus"

    props = {
        'EventSourceName': (str, False),
        'Name': (str, True),
    }


class Condition(AWSProperty):
    props = {
        'Key': (str, False),
        'Type': (str, False),
        'Value': (str, False),
    }


class EventBusPolicy(AWSObject):
    resource_type = "AWS::Events::EventBusPolicy"

    props = {
        'Action': (str, True),
        'Condition': (Condition, False),
        'EventBusName': (str, False),
        'Principal': (str, True),
        'StatementId': (str, True),
    }


class BatchArrayProperties(AWSProperty):
    props = {
        'Size': (integer, False),
    }


class BatchRetryStrategy(AWSProperty):
    props = {
        'Attempts': (integer, False),
    }


class BatchParameters(AWSProperty):
    props = {
        'ArrayProperties': (BatchArrayProperties, False),
        'JobDefinition': (str, True),
        'JobName': (str, True),
        'RetryStrategy': (BatchRetryStrategy, False),
    }


class AwsVpcConfiguration(AWSProperty):
    props = {
        'AssignPublicIp': (str, False),
        'SecurityGroups': ([str], False),
        'Subnets': ([str], True),
    }


class NetworkConfiguration(AWSProperty):
    props = {
        'AwsVpcConfiguration': (AwsVpcConfiguration, False),
    }


class EcsParameters(AWSProperty):
    props = {
        'Group': (str, False),
        'LaunchType': (str, False),
        'NetworkConfiguration': (NetworkConfiguration, False),
        'PlatformVersion': (str, False),
        'TaskCount': (integer, False),
        'TaskDefinitionArn': (str, True),
    }


class HttpParameters(AWSProperty):
    props = {
        'HeaderParameters': (dict, False),
        'PathParameterValues': ([str], False),
        'QueryStringParameters': (dict, False),
    }


class InputTransformer(AWSProperty):
    props = {
        'InputPathsMap': (dict, False),
        'InputTemplate': (str, True),
    }


class KinesisParameters(AWSProperty):
    props = {
        'PartitionKeyPath': (str, True),
    }


class RunCommandTarget(AWSProperty):
    props = {
        'Key': (str, True),
        'Values': ([str], True),
    }


class RunCommandParameters(AWSProperty):
    props = {
        'RunCommandTargets': ([RunCommandTarget], True),
    }


class SqsParameters(AWSProperty):
    props = {
        'MessageGroupId': (str, True),
    }


class Target(AWSProperty):
    props = {
        'Arn': (str, True),
        'BatchParameters': (BatchParameters, False),
        'EcsParameters': (EcsParameters, False),
        'HttpParameters': (HttpParameters, False),
        'Id': (str, True),
        'Input': (str, False),
        'InputPath': (str, False),
        'InputTransformer': (InputTransformer, False),
        'KinesisParameters': (KinesisParameters, False),
        'RoleArn': (str, False),
        'RunCommandParameters': (RunCommandParameters, False),
        'SqsParameters': (SqsParameters, False),
    }


class Rule(AWSObject):
    resource_type = "AWS::Events::Rule"

    props = {
        'Description': (str, False),
        'EventBusName': (str, False),
        'EventPattern': (dict, False),
        'Name': (str, False),
        'RoleArn': (str, False),
        'ScheduleExpression': (str, False),
        'State': (str, False),
        'Targets': ([Target], False),
    }
