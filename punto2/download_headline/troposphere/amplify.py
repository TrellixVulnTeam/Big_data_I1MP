# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 8.1.0


from . import AWSObject
from . import AWSProperty
from troposphere import Tags
from .validators import boolean


class BasicAuthConfig(AWSProperty):
    props = {
        'EnableBasicAuth': (boolean, False),
        'Password': (str, True),
        'Username': (str, True),
    }


class EnvironmentVariable(AWSProperty):
    props = {
        'Name': (str, True),
        'Value': (str, True),
    }


class AutoBranchCreationConfig(AWSProperty):
    props = {
        'AutoBranchCreationPatterns': ([str], False),
        'BasicAuthConfig': (BasicAuthConfig, False),
        'BuildSpec': (str, False),
        'EnableAutoBranchCreation': (boolean, False),
        'EnableAutoBuild': (boolean, False),
        'EnablePullRequestPreview': (boolean, False),
        'EnvironmentVariables': ([EnvironmentVariable], False),
        'PullRequestEnvironmentName': (str, False),
        'Stage': (str, False),
    }


class CustomRule(AWSProperty):
    props = {
        'Condition': (str, False),
        'Source': (str, True),
        'Status': (str, False),
        'Target': (str, True),
    }


class App(AWSObject):
    resource_type = "AWS::Amplify::App"

    props = {
        'AccessToken': (str, False),
        'AutoBranchCreationConfig': (AutoBranchCreationConfig, False),
        'BasicAuthConfig': (BasicAuthConfig, False),
        'BuildSpec': (str, False),
        'CustomRules': ([CustomRule], False),
        'Description': (str, False),
        'EnableBranchAutoDeletion': (boolean, False),
        'EnvironmentVariables': ([EnvironmentVariable], False),
        'IAMServiceRole': (str, False),
        'Name': (str, True),
        'OauthToken': (str, False),
        'Repository': (str, False),
        'Tags': (Tags, False),
    }


class Branch(AWSObject):
    resource_type = "AWS::Amplify::Branch"

    props = {
        'AppId': (str, True),
        'BasicAuthConfig': (BasicAuthConfig, False),
        'BranchName': (str, True),
        'BuildSpec': (str, False),
        'Description': (str, False),
        'EnableAutoBuild': (boolean, False),
        'EnablePullRequestPreview': (boolean, False),
        'EnvironmentVariables': ([EnvironmentVariable], False),
        'PullRequestEnvironmentName': (str, False),
        'Stage': (str, False),
        'Tags': (Tags, False),
    }


class SubDomainSetting(AWSProperty):
    props = {
        'BranchName': (str, True),
        'Prefix': (str, True),
    }


class Domain(AWSObject):
    resource_type = "AWS::Amplify::Domain"

    props = {
        'AppId': (str, True),
        'AutoSubDomainCreationPatterns': ([str], False),
        'AutoSubDomainIAMRole': (str, False),
        'DomainName': (str, True),
        'EnableAutoSubDomain': (boolean, False),
        'SubDomainSettings': ([SubDomainSetting], True),
    }
