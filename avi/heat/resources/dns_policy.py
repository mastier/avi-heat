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
from match import *
from dns import *


class DnsQueryTypeMatch(object):
    # all schemas
    match_criteria_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Criterion to use for matching the DNS query typein the question section"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['IS_IN', 'IS_NOT_IN']),
        ],
    )
    query_type_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) DNS query types in the request query "),
        required=True,
        update_allowed=False,
        constraints=[
            constraints.AllowedValues(['DNS_RECORD_A', 'DNS_RECORD_AAAA', 'DNS_RECORD_ANY', 'DNS_RECORD_AXFR', 'DNS_RECORD_CNAME', 'DNS_RECORD_DNSKEY', 'DNS_RECORD_HINFO', 'DNS_RECORD_MX', 'DNS_RECORD_NS', 'DNS_RECORD_OPT', 'DNS_RECORD_OTHER', 'DNS_RECORD_PTR', 'DNS_RECORD_RP', 'DNS_RECORD_RRSIG', 'DNS_RECORD_SOA', 'DNS_RECORD_SRV', 'DNS_RECORD_TXT']),
        ],
    )
    query_type_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.1.1) DNS query types in the request query "),
        schema=query_type_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'match_criteria',
        'query_type',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'match_criteria': match_criteria_schema,
        'query_type': query_type_schema,
    }



class DnsQueryNameMatch(object):
    # all schemas
    match_criteria_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Criterion to use for string matching the DNS query domain name in the question section"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['BEGINS_WITH', 'CONTAINS', 'DOES_NOT_BEGIN_WITH', 'DOES_NOT_CONTAIN', 'DOES_NOT_END_WITH', 'DOES_NOT_EQUAL', 'ENDS_WITH', 'EQUALS', 'REGEX_DOES_NOT_MATCH', 'REGEX_MATCH']),
        ],
    )
    query_domain_names_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Domain name to match against that specified in the question section of the DNS query"),
        required=True,
        update_allowed=False,
    )
    query_domain_names_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.1.1) Domain name to match against that specified in the question section of the DNS query"),
        schema=query_domain_names_item_schema,
        required=False,
        update_allowed=True,
    )
    string_group_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) UUID of the string group(s) for matching against DNS query domain name in the question section"),
        required=True,
        update_allowed=False,
    )
    string_group_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.1.1) UUID of the string group(s) for matching against DNS query domain name in the question section You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        schema=string_group_uuids_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'match_criteria',
        'query_domain_names',
        'string_group_uuids',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'match_criteria': match_criteria_schema,
        'query_domain_names': query_domain_names_schema,
        'string_group_uuids': string_group_uuids_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'string_group_uuids': 'stringgroup',
    }



class DnsGeoLocationMatch(object):
    # all schemas
    match_criteria_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.5) Criterion to use for matching the client IP's geographical location"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['IS_IN', 'IS_NOT_IN']),
        ],
    )
    use_edns_client_subnet_ip_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.5) Use the IP address from the EDNS client subnet option, if available, to derive geo location of the DNS query (Default: True)"),
        required=False,
        update_allowed=True,
    )
    geolocation_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.5) Geographical location of the client IP to be used in the match. This location is of the format Country/State/City e.g. US/CA/Santa Clara."),
        required=False,
        update_allowed=True,
    )
    geolocation_tag_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.5) Geolocation tag for the client IP. This could be any string value for the client IP, e.g. client IPs from US East Coast geolocation would be tagged as 'East Coast'."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'match_criteria',
        'use_edns_client_subnet_ip',
        'geolocation_name',
        'geolocation_tag',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'match_criteria': match_criteria_schema,
        'use_edns_client_subnet_ip': use_edns_client_subnet_ip_schema,
        'geolocation_name': geolocation_name_schema,
        'geolocation_tag': geolocation_tag_schema,
    }



class DnsRuleActionGslbSiteSelection(object):
    # all schemas
    site_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.5) GSLB site name"),
        required=True,
        update_allowed=True,
    )
    is_site_preferred_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.2.5) When set to true, GSLB site is a preferred site. This setting comes into play when the site is down, as well as no configured fallback site is available (all fallback sites are also down), then any one available site is selected based on the default algorithm for GSLB pool member selection. (Default: True)"),
        required=False,
        update_allowed=True,
    )
    fallback_site_names_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.5) GSLB fallback sites to use in case the desired site is down."),
        required=True,
        update_allowed=False,
    )
    fallback_site_names_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.2.5) GSLB fallback sites to use in case the desired site is down."),
        schema=fallback_site_names_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'site_name',
        'is_site_preferred',
        'fallback_site_names',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'site_name': site_name_schema,
        'is_site_preferred': is_site_preferred_schema,
        'fallback_site_names': fallback_site_names_schema,
    }



class DnsRuleActionAllowDrop(object):
    # all schemas
    allow_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1) Allow the DNS query (Default: True)"),
        required=False,
        update_allowed=True,
    )
    reset_conn_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1) Reset the TCP connection of the DNS query, if allow is set to false to drop the query (Default: True)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'allow',
        'reset_conn',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'allow': allow_schema,
        'reset_conn': reset_conn_schema,
    }



class DnsClientIpMatch(object):
    # all schemas
    client_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.6,17.2.2) IP addresses to match against client IP"),
        schema=IpAddrMatch.properties_schema,
        required=True,
        update_allowed=True,
    )
    use_edns_client_subnet_ip_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.6,17.2.2) Use the IP address from the EDNS client subnet option, if available, as the source IP address of the client. It should be noted that the edns subnet IP may not be a /32 IP address. (Default: False)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'client_ip',
        'use_edns_client_subnet_ip',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'client_ip': client_ip_schema,
        'use_edns_client_subnet_ip': use_edns_client_subnet_ip_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'client_ip': getattr(IpAddrMatch, 'field_references', {}),
    }

    unique_keys = {
        'client_ip': getattr(IpAddrMatch, 'unique_keys', {}),
    }



class DnsRuleActionResponse(object):
    # all schemas
    rcode_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) DNS response code (Default: DNS_RCODE_NOERROR)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DNS_RCODE_FORMERR', 'DNS_RCODE_NOERROR', 'DNS_RCODE_NOTAUTH', 'DNS_RCODE_NOTIMP', 'DNS_RCODE_NOTZONE', 'DNS_RCODE_NXDOMAIN', 'DNS_RCODE_NXRRSET', 'DNS_RCODE_REFUSED', 'DNS_RCODE_SERVFAIL', 'DNS_RCODE_YXDOMAIN', 'DNS_RCODE_YXRRSET']),
        ],
    )
    truncation_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1) DNS response is truncated (Default: False)"),
        required=False,
        update_allowed=True,
    )
    authoritative_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1) DNS response is authoritative (Default: True)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'rcode',
        'truncation',
        'authoritative',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'rcode': rcode_schema,
        'truncation': truncation_schema,
        'authoritative': authoritative_schema,
    }



class DnsPolicies(object):
    # all schemas
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.1.1) Index of the dns policy"),
        required=True,
        update_allowed=True,
    )
    dns_policy_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) UUID of the dns policy You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'index',
        'dns_policy_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'index': index_schema,
        'dns_policy_uuid': dns_policy_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'dns_policy_uuid': 'dnspolicy',
    }

    unique_keys = {
        'my_key': 'index',
    }



class DnsTransportProtocolMatch(object):
    # all schemas
    match_criteria_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Criterion to use for matching the DNS transport protocol"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['IS_IN', 'IS_NOT_IN']),
        ],
    )
    protocol_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Protocol to match against transport protocol used by DNS query"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DNS_OVER_TCP', 'DNS_OVER_UDP']),
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



class DnsRuleMatchTarget(object):
    # all schemas
    client_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) (Deprecated in: 17.1.6,17.2.2) IP addresses to match against client IP. From 17.1.6 release onwards, IP addresses needs to be configured in the client_ip_address field of this message."),
        schema=IpAddrMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    protocol_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) DNS transport protocol match"),
        schema=DnsTransportProtocolMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    query_name_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) Domain names to match against query name"),
        schema=DnsQueryNameMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    query_type_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) DNS query types to match against request query type"),
        schema=DnsQueryTypeMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    geo_location_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.5) Geographical location attribute to match against that of the client IP"),
        schema=DnsGeoLocationMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    client_ip_address_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.6,17.2.2) IP addresses to match against client IP or the EDNS client subnet IP"),
        schema=DnsClientIpMatch.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'client_ip',
        'protocol',
        'query_name',
        'query_type',
        'geo_location',
        'client_ip_address',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'client_ip': client_ip_schema,
        'protocol': protocol_schema,
        'query_name': query_name_schema,
        'query_type': query_type_schema,
        'geo_location': geo_location_schema,
        'client_ip_address': client_ip_address_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'client_ip': getattr(IpAddrMatch, 'field_references', {}),
        'protocol': getattr(DnsTransportProtocolMatch, 'field_references', {}),
        'client_ip_address': getattr(DnsClientIpMatch, 'field_references', {}),
        'query_type': getattr(DnsQueryTypeMatch, 'field_references', {}),
        'geo_location': getattr(DnsGeoLocationMatch, 'field_references', {}),
        'query_name': getattr(DnsQueryNameMatch, 'field_references', {}),
    }

    unique_keys = {
        'client_ip': getattr(IpAddrMatch, 'unique_keys', {}),
        'protocol': getattr(DnsTransportProtocolMatch, 'unique_keys', {}),
        'client_ip_address': getattr(DnsClientIpMatch, 'unique_keys', {}),
        'query_type': getattr(DnsQueryTypeMatch, 'unique_keys', {}),
        'geo_location': getattr(DnsGeoLocationMatch, 'unique_keys', {}),
        'query_name': getattr(DnsQueryNameMatch, 'unique_keys', {}),
    }



class DnsRuleAction(object):
    # all schemas
    allow_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) Allow or drop the DNS query"),
        schema=DnsRuleActionAllowDrop.properties_schema,
        required=False,
        update_allowed=True,
    )
    response_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) Generate a response for the DNS query"),
        schema=DnsRuleActionResponse.properties_schema,
        required=False,
        update_allowed=True,
    )
    gslb_site_selection_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.5) Select a specific GSLB site for the DNS query. This action should be used only when GSLB services have been configured for the DNS virtual service."),
        schema=DnsRuleActionGslbSiteSelection.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'allow',
        'response',
        'gslb_site_selection',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'allow': allow_schema,
        'response': response_schema,
        'gslb_site_selection': gslb_site_selection_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'gslb_site_selection': getattr(DnsRuleActionGslbSiteSelection, 'field_references', {}),
        'response': getattr(DnsRuleActionResponse, 'field_references', {}),
        'allow': getattr(DnsRuleActionAllowDrop, 'field_references', {}),
    }

    unique_keys = {
        'gslb_site_selection': getattr(DnsRuleActionGslbSiteSelection, 'unique_keys', {}),
        'response': getattr(DnsRuleActionResponse, 'unique_keys', {}),
        'allow': getattr(DnsRuleActionAllowDrop, 'unique_keys', {}),
    }



class DnsRule(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Name of the rule"),
        required=True,
        update_allowed=True,
    )
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.1.1) Index of the rule"),
        required=True,
        update_allowed=True,
    )
    enable_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1) Enable or disable the rule (Default: True)"),
        required=False,
        update_allowed=True,
    )
    match_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) Add match criteria to the rule"),
        schema=DnsRuleMatchTarget.properties_schema,
        required=False,
        update_allowed=True,
    )
    action_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) Action to be performed upon successful matching"),
        schema=DnsRuleAction.properties_schema,
        required=False,
        update_allowed=True,
    )
    log_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1) Log DNS query upon rule match"),
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
        'log',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'index': index_schema,
        'enable': enable_schema,
        'match': match_schema,
        'action': action_schema,
        'log': log_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'action': getattr(DnsRuleAction, 'field_references', {}),
        'match': getattr(DnsRuleMatchTarget, 'field_references', {}),
    }

    unique_keys = {
        'action': getattr(DnsRuleAction, 'unique_keys', {}),
        'my_key': 'index',
        'match': getattr(DnsRuleMatchTarget, 'unique_keys', {}),
    }



class DnsPolicy(AviResource):
    resource_name = "dnspolicy"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Name of the DNS Policy"),
        required=True,
        update_allowed=True,
    )
    rule_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) DNS rules"),
        schema=DnsRule.properties_schema,
        required=True,
        update_allowed=False,
    )
    rule_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.1.1) DNS rules"),
        schema=rule_item_schema,
        required=False,
        update_allowed=True,
    )
    created_by_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Creator name"),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) "),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'rule',
        'created_by',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'rule': rule_schema,
        'created_by': created_by_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'rule': getattr(DnsRule, 'field_references', {}),
    }

    unique_keys = {
        'rule': getattr(DnsRule, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::DnsPolicy': DnsPolicy,
    }
