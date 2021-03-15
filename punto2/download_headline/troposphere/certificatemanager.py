# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 15.1.0


from . import AWSObject
from . import AWSProperty
from troposphere import Tags


class DomainValidationOption(AWSProperty):
    props = {
        'DomainName': (str, True),
        'HostedZoneId': (str, False),
        'ValidationDomain': (str, False),
    }


class Certificate(AWSObject):
    resource_type = "AWS::CertificateManager::Certificate"

    props = {
        'CertificateAuthorityArn': (str, False),
        'CertificateTransparencyLoggingPreference': (str, False),
        'DomainName': (str, True),
        'DomainValidationOptions': ([DomainValidationOption], False),
        'SubjectAlternativeNames': ([str], False),
        'Tags': ((Tags, list), False),
        'ValidationMethod': (str, False),
    }
