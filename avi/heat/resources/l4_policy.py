# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from common import *
from options import *
from match import *


class L4Policies(object):
    # all schemas
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.2.7) Index of the virtual service L4 policy set"),
        required=True,
        update_allowed=True,
    )
    l4_policy_set_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.7) ID of the virtual service L4 policy set You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'index',
        'l4_policy_set_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'index': index_schema,
        'l4_policy_set_uuid': l4_policy_set_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'l4_policy_set_uuid': 'l4policyset',
    }

    unique_keys = {
        'my_key': 'index',
    }



class L4RuleActionSelectPool(object):
    # all schemas
    action_type_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.7) Indicates action to take on rule match"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['L4_RULE_ACTION_SELECT_POOL', 'L4_RULE_ACTION_SELECT_POOLGROUP']),
        ],
    )
    pool_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.7) ID of the pool of servers to serve the request You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    pool_group_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.7) ID of the pool group to serve the request You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'action_type',
        'pool_uuid',
        'pool_group_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'action_type': action_type_schema,
        'pool_uuid': pool_uuid_schema,
        'pool_group_uuid': pool_group_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'pool_uuid': 'pool',
        'pool_group_uuid': 'poolgroup',
    }



class L4RuleProtocolMatch(object):
    # all schemas
    match_criteria_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.7) Criterion to use for transport protocol matching"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['IS_IN', 'IS_NOT_IN']),
        ],
    )
    protocol_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.7) Transport protocol to match"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['PROTOCOL_ICMP', 'PROTOCOL_TCP', 'PROTOCOL_UDP']),
        ],
    )

    # properties list
    PROPERTIES = (
        'match_criteria',
        'protocol',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'match_criteria': match_criteria_schema,
        'protocol': protocol_schema,
    }



class L4RulePortMatch(object):
    # all schemas
    match_criteria_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.7) Criterion to use for Virtual Service port matching"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['IS_IN', 'IS_NOT_IN']),
        ],
    )
    ports_item_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.2.7) Virtual Service's listening port(s)"),
        required=True,
        update_allowed=False,
    )
    ports_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.2.7) Virtual Service's listening port(s)"),
        schema=ports_item_schema,
        required=False,
        update_allowed=True,
    )
    port_ranges_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.2.7) Range of TCP/UDP port numbers of the Virtual Service"),
        schema=PortRange.properties_schema,
        required=True,
        update_allowed=False,
    )
    port_ranges_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.2.7) Range of TCP/UDP port numbers of the Virtual Service"),
        schema=port_ranges_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'match_criteria',
        'ports',
        'port_ranges',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'match_criteria': match_criteria_schema,
        'ports': ports_schema,
        'port_ranges': port_ranges_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'port_ranges': getattr(PortRange, 'field_references', {}),
    }

    unique_keys = {
        'port_ranges': getattr(PortRange, 'unique_keys', {}),
    }



class L4RuleAction(object):
    # all schemas
    select_pool_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.2.7) Indicates pool or pool-group selection on rule match"),
        schema=L4RuleActionSelectPool.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'select_pool',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'select_pool': select_pool_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'select_pool': getattr(L4RuleActionSelectPool, 'field_references', {}),
    }

    unique_keys = {
        'select_pool': getattr(L4RuleActionSelectPool, 'unique_keys', {}),
    }



class L4RuleMatchTarget(object):
    # all schemas
    client_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.2.7) IP addresses to match against client IP"),
        schema=IpAddrMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.2.7) Port number to match against Virtual Service listner port"),
        schema=L4RulePortMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    protocol_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.2.7) TCP/UDP/ICMP protocol to match against transport protocol"),
        schema=L4RuleProtocolMatch.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'client_ip',
        'port',
        'protocol',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'client_ip': client_ip_schema,
        'port': port_schema,
        'protocol': protocol_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'client_ip': getattr(IpAddrMatch, 'field_references', {}),
        'protocol': getattr(L4RuleProtocolMatch, 'field_references', {}),
        'port': getattr(L4RulePortMatch, 'field_references', {}),
    }

    unique_keys = {
        'client_ip': getattr(IpAddrMatch, 'unique_keys', {}),
        'protocol': getattr(L4RuleProtocolMatch, 'unique_keys', {}),
        'port': getattr(L4RulePortMatch, 'unique_keys', {}),
    }



class L4Rule(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.7) Name of the rule"),
        required=True,
        update_allowed=True,
    )
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.2.7) Index of the rule"),
        required=True,
        update_allowed=True,
    )
    enable_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.2.7) Enable or disable the rule (Default: True)"),
        required=False,
        update_allowed=True,
    )
    match_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.2.7) Match criteria of the rule"),
        schema=L4RuleMatchTarget.properties_schema,
        required=False,
        update_allowed=True,
    )
    action_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.2.7) Action to be performed upon successful rule match"),
        schema=L4RuleAction.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'index',
        'enable',
        'match',
        'action',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'index': index_schema,
        'enable': enable_schema,
        'match': match_schema,
        'action': action_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'action': getattr(L4RuleAction, 'field_references', {}),
        'match': getattr(L4RuleMatchTarget, 'field_references', {}),
    }

    unique_keys = {
        'action': getattr(L4RuleAction, 'unique_keys', {}),
        'my_key': 'index',
        'match': getattr(L4RuleMatchTarget, 'unique_keys', {}),
    }



class L4ConnectionPolicy(object):
    # all schemas
    rules_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.2.7) Rules to apply when a new transport connection is setup"),
        schema=L4Rule.properties_schema,
        required=True,
        update_allowed=False,
    )
    rules_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.2.7) Rules to apply when a new transport connection is setup"),
        schema=rules_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'rules',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'rules': rules_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'rules': getattr(L4Rule, 'field_references', {}),
    }

    unique_keys = {
        'rules': getattr(L4Rule, 'unique_keys', {}),
    }



class L4PolicySet(AviResource):
    resource_name = "l4policyset"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.7) Name of the L4 Policy Set"),
        required=True,
        update_allowed=True,
    )
    l4_connection_policy_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.2.7) Policy to apply when a new transport connection is setup"),
        schema=L4ConnectionPolicy.properties_schema,
        required=False,
        update_allowed=True,
    )
    created_by_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.7) Creator name"),
        required=False,
        update_allowed=True,
    )
    is_internal_policy_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.2.7)  (Default: False)"),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.7) "),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'l4_connection_policy',
        'created_by',
        'is_internal_policy',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'l4_connection_policy': l4_connection_policy_schema,
        'created_by': created_by_schema,
        'is_internal_policy': is_internal_policy_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'l4_connection_policy': getattr(L4ConnectionPolicy, 'field_references', {}),
    }

    unique_keys = {
        'l4_connection_policy': getattr(L4ConnectionPolicy, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::L4PolicySet': L4PolicySet,
    }

