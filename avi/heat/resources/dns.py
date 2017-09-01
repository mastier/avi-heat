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


class DnsARdata(object):
    # all schemas
    ip_address_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP address for fqdn"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ip_address',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip_address': ip_address_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip_address': getattr(IpAddr, 'field_references', {}),
    }

    unique_keys = {
        'ip_address': getattr(IpAddr, 'unique_keys', {}),
    }



class DnsInfo(object):
    # all schemas
    fqdn_schema = properties.Schema(
        properties.Schema.STRING,
        _("Fully qualified domain name."),
        required=False,
        update_allowed=True,
    )
    ttl_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Time to live for fqdn record. Default value is chosen from DNS profile for this cloud if no value provided."),
        required=False,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("DNS record type (Default: DNS_RECORD_A)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DNS_RECORD_A', 'DNS_RECORD_AAAA', 'DNS_RECORD_ANY', 'DNS_RECORD_AXFR', 'DNS_RECORD_CNAME', 'DNS_RECORD_DNSKEY', 'DNS_RECORD_HINFO', 'DNS_RECORD_MX', 'DNS_RECORD_NS', 'DNS_RECORD_OPT', 'DNS_RECORD_OTHER', 'DNS_RECORD_PTR', 'DNS_RECORD_RP', 'DNS_RECORD_RRSIG', 'DNS_RECORD_SOA', 'DNS_RECORD_SRV', 'DNS_RECORD_TXT']),
        ],
    )
    num_records_in_response_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.1.1) Specifies the number of records returned for this FQDN. Enter 0 to return all records. Default is 0 (Default: 1)"),
        required=False,
        update_allowed=True,
    )
    algorithm_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Specifies the algorithm to pick the IP address(es) to be returned, when multiple entries are configured. This does not apply if num_records_in_response is 0. Default is consistent hash. (Default: DNS_RECORD_RESPONSE_CONSISTENT_HASH)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DNS_RECORD_RESPONSE_CONSISTENT_HASH', 'DNS_RECORD_RESPONSE_ROUND_ROBIN']),
        ],
    )

    # properties list
    PROPERTIES = (
        'fqdn',
        'ttl',
        'type',
        'num_records_in_response',
        'algorithm',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'fqdn': fqdn_schema,
        'ttl': ttl_schema,
        'type': type_schema,
        'num_records_in_response': num_records_in_response_schema,
        'algorithm': algorithm_schema,
    }



class DnsNsRdata(object):
    # all schemas
    nsname_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Name Server name"),
        required=True,
        update_allowed=True,
    )
    ip_address_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) IP address for Name Server"),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'nsname',
        'ip_address',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'nsname': nsname_schema,
        'ip_address': ip_address_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip_address': getattr(IpAddr, 'field_references', {}),
    }

    unique_keys = {
        'ip_address': getattr(IpAddr, 'unique_keys', {}),
    }



class DnsSrvRdata(object):
    # all schemas
    priority_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Priority of the target hosting the service, low value implies higher priority for this service record (Default: 0)"),
        required=False,
        update_allowed=True,
    )
    weight_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Relative weight for service records with same priority, high value implies higher preference for this service record (Default: 0)"),
        required=False,
        update_allowed=True,
    )
    target_schema = properties.Schema(
        properties.Schema.STRING,
        _("Canonical hostname, of the machine hosting the service, with no trailing period. 'default.host' is valid but not 'default.host.'"),
        required=False,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Service port"),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'priority',
        'weight',
        'target',
        'port',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'priority': priority_schema,
        'weight': weight_schema,
        'target': target_schema,
        'port': port_schema,
    }



class DnsCnameRdata(object):
    # all schemas
    cname_schema = properties.Schema(
        properties.Schema.STRING,
        _("Canonical name"),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'cname',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'cname': cname_schema,
    }



class DnsRecord(object):
    # all schemas
    fqdn_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("Fully Qualified Domain Name"),
        required=True,
        update_allowed=False,
    )
    fqdn_schema = properties.Schema(
        properties.Schema.LIST,
        _("Fully Qualified Domain Name"),
        schema=fqdn_item_schema,
        required=False,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("DNS record type"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DNS_RECORD_A', 'DNS_RECORD_AAAA', 'DNS_RECORD_ANY', 'DNS_RECORD_AXFR', 'DNS_RECORD_CNAME', 'DNS_RECORD_DNSKEY', 'DNS_RECORD_HINFO', 'DNS_RECORD_MX', 'DNS_RECORD_NS', 'DNS_RECORD_OPT', 'DNS_RECORD_OTHER', 'DNS_RECORD_PTR', 'DNS_RECORD_RP', 'DNS_RECORD_RRSIG', 'DNS_RECORD_SOA', 'DNS_RECORD_SRV', 'DNS_RECORD_TXT']),
        ],
    )
    ttl_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Time To Live for this DNS record"),
        required=False,
        update_allowed=True,
    )
    ip_address_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP address in A record"),
        schema=DnsARdata.properties_schema,
        required=True,
        update_allowed=False,
    )
    ip_address_schema = properties.Schema(
        properties.Schema.LIST,
        _("IP address in A record"),
        schema=ip_address_item_schema,
        required=False,
        update_allowed=True,
    )
    service_locator_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("Service locator info in SRV record"),
        schema=DnsSrvRdata.properties_schema,
        required=True,
        update_allowed=False,
    )
    service_locator_schema = properties.Schema(
        properties.Schema.LIST,
        _("Service locator info in SRV record"),
        schema=service_locator_item_schema,
        required=False,
        update_allowed=True,
    )
    cname_schema = properties.Schema(
        properties.Schema.MAP,
        _("Canonical name in CNAME record"),
        schema=DnsCnameRdata.properties_schema,
        required=False,
        update_allowed=True,
    )
    ns_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) Name Server information in NS record"),
        schema=DnsNsRdata.properties_schema,
        required=True,
        update_allowed=False,
    )
    ns_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.1.1) Name Server information in NS record"),
        schema=ns_item_schema,
        required=False,
        update_allowed=True,
    )
    num_records_in_response_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.1.1) Specifies the number of records returned by the DNS service. Enter 0 to return all records. Default is 0 (Default: 0)"),
        required=False,
        update_allowed=True,
    )
    algorithm_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Specifies the algorithm to pick the IP address(es) to be returned, when multiple entries are configured. This does not apply if num_records_in_response is 0. Default is round-robin. (Default: DNS_RECORD_RESPONSE_ROUND_ROBIN)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DNS_RECORD_RESPONSE_CONSISTENT_HASH', 'DNS_RECORD_RESPONSE_ROUND_ROBIN']),
        ],
    )
    wildcard_match_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1) Enable wild-card match of fqdn: if an exact match is not found in the DNS table, the longest match is chosen by wild-carding the fqdn in the DNS request. Default is false. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    delegated_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.2) Configured FQDNs are delegated domains (i.e. they represent a zone cut). (Default: False)"),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _("Details of DNS record"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'fqdn',
        'type',
        'ttl',
        'ip_address',
        'service_locator',
        'cname',
        'ns',
        'num_records_in_response',
        'algorithm',
        'wildcard_match',
        'delegated',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'fqdn': fqdn_schema,
        'type': type_schema,
        'ttl': ttl_schema,
        'ip_address': ip_address_schema,
        'service_locator': service_locator_schema,
        'cname': cname_schema,
        'ns': ns_schema,
        'num_records_in_response': num_records_in_response_schema,
        'algorithm': algorithm_schema,
        'wildcard_match': wildcard_match_schema,
        'delegated': delegated_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ns': getattr(DnsNsRdata, 'field_references', {}),
        'cname': getattr(DnsCnameRdata, 'field_references', {}),
        'ip_address': getattr(DnsARdata, 'field_references', {}),
        'service_locator': getattr(DnsSrvRdata, 'field_references', {}),
    }

    unique_keys = {
        'ns': getattr(DnsNsRdata, 'unique_keys', {}),
        'cname': getattr(DnsCnameRdata, 'unique_keys', {}),
        'ip_address': getattr(DnsARdata, 'unique_keys', {}),
        'service_locator': getattr(DnsSrvRdata, 'unique_keys', {}),
    }

