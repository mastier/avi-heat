# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from options import *
from common import *


class UserAccountProfile(AviResource):
    resource_name = "useraccountprofile"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    max_password_history_count_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of passwords to be maintained in the password history. Default is 4 passwords. (Default: 4)"),
        required=False,
        update_allowed=True,
    )
    max_login_failure_count_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of login attempts before lockout. Default is 3 attempts. (Default: 3)"),
        required=False,
        update_allowed=True,
    )
    account_lock_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Lock timeout period (in minutes). Default is 30 minutes. (Units: MIN) (Default: 30)"),
        required=False,
        update_allowed=True,
    )
    max_concurrent_sessions_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of concurrent sessions allowed. There are unlimited sessions by default. (Default: 0)"),
        required=False,
        update_allowed=True,
    )
    credentials_timeout_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The time period after which credentials expire. Default is 180 days. (Units: DAYS) (Default: 180)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'max_password_history_count',
        'max_login_failure_count',
        'account_lock_timeout',
        'max_concurrent_sessions',
        'credentials_timeout_threshold',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'max_password_history_count': max_password_history_count_schema,
        'max_login_failure_count': max_login_failure_count_schema,
        'account_lock_timeout': account_lock_timeout_schema,
        'max_concurrent_sessions': max_concurrent_sessions_schema,
        'credentials_timeout_threshold': credentials_timeout_threshold_schema,
    }



class Permission(object):
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['JOB_OWNER_CONSISTENCY_CHECKER', 'JOB_OWNER_DEBUG_VIRTUALSERVICE', 'JOB_OWNER_NETWORKSECURITYPOLICY', 'JOB_OWNER_PKI_PROFILE', 'JOB_OWNER_POSTGRES_STATUS', 'JOB_OWNER_SEGROUP', 'JOB_OWNER_SSL', 'JOB_OWNER_TECHSUPPORT_UPLOADER', 'JOB_OWNER_VIRTUALSERVICE']),
        ],
    )
    resource_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['PERMISSION_ACTIONGROUPCONFIG', 'PERMISSION_ALERT', 'PERMISSION_ALERTCONFIG', 'PERMISSION_ALERTEMAILCONFIG', 'PERMISSION_ALERTSYSLOGCONFIG', 'PERMISSION_ANALYTICSPROFILE', 'PERMISSION_APPLICATIONPERSISTENCEPROFILE', 'PERMISSION_APPLICATIONPROFILE', 'PERMISSION_AUTHPROFILE', 'PERMISSION_AUTOSCALE', 'PERMISSION_CERTIFICATEMANAGEMENTPROFILE', 'PERMISSION_CLOUD', 'PERMISSION_CONTROLLER', 'PERMISSION_CUSTOMIPAMDNSPROFILE', 'PERMISSION_DNSPOLICY', 'PERMISSION_ERRORPAGEBODY', 'PERMISSION_ERRORPAGEPROFILE', 'PERMISSION_EXEMPT', 'PERMISSION_GSLB', 'PERMISSION_GSLBGEODBPROFILE', 'PERMISSION_GSLBSERVICE', 'PERMISSION_HEALTHMONITOR', 'PERMISSION_HTTPPOLICYSET', 'PERMISSION_INTERNAL', 'PERMISSION_IPADDRGROUP', 'PERMISSION_IPAMDNSPROVIDERPROFILE', 'PERMISSION_MICROSERVICEGROUP', 'PERMISSION_NETWORK', 'PERMISSION_NETWORKPROFILE', 'PERMISSION_NETWORKSECURITYPOLICY', 'PERMISSION_PKIPROFILE', 'PERMISSION_POOL', 'PERMISSION_POOLGROUP', 'PERMISSION_POOLGROUPDEPLOYMENTPOLICY', 'PERMISSION_POOL_MAINTENANCE', 'PERMISSION_PRIORITYLABELS', 'PERMISSION_REBOOT', 'PERMISSION_ROLE', 'PERMISSION_SERVICEENGINE', 'PERMISSION_SERVICEENGINEGROUP', 'PERMISSION_SE_TOKEN', 'PERMISSION_SNMPTRAPPROFILE', 'PERMISSION_SSLKEYANDCERTIFICATE', 'PERMISSION_SSLPROFILE', 'PERMISSION_STRINGGROUP', 'PERMISSION_SYSTEMCONFIGURATION', 'PERMISSION_TECHSUPPORT', 'PERMISSION_TENANT', 'PERMISSION_TRAFFICCLONEPROFILE', 'PERMISSION_TRAFFIC_CAPTURE', 'PERMISSION_UPGRADE', 'PERMISSION_USER', 'PERMISSION_USER_CREDENTIAL', 'PERMISSION_VIRTUALSERVICE', 'PERMISSION_VIRTUALSERVICE_MAINTENANCE', 'PERMISSION_VRFCONTEXT', 'PERMISSION_VSDATASCRIPTSET', 'PERMISSION_WAFPOLICY', 'PERMISSION_WAFPROFILE']),
        ],
    )

    # properties list
    PROPERTIES = (
        'type',
        'resource',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'resource': resource_schema,
    }



class Role(AviResource):
    resource_name = "role"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    privileges_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=Permission.properties_schema,
        required=True,
        update_allowed=False,
    )
    privileges_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=privileges_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'privileges',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'privileges': privileges_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'privileges': getattr(Permission, 'field_references', {}),
    }

    unique_keys = {
        'privileges': getattr(Permission, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::UserAccountProfile': UserAccountProfile,
        'Avi::LBaaS::Role': Role,
    }

