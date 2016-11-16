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
from health_monitor import *


class DNSConfig(object):
    # all schemas
    domain_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Gslb Subdomain used for GslbService FQDN match and placement. "),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'domain_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'domain_name': domain_name_schema,
    }




class GslbPoolMember(object):
    # all schemas
    cluster_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("The Cluster UUID of the Site Controller Cluster."),
        required=False,
        update_allowed=True,
    )
    vs_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Select local virtual service in the specified controller cluster belonging to this GslbService."),
        required=False,
        update_allowed=True,
    )
    fqdn_schema = properties.Schema(
        properties.Schema.STRING,
        _("The member is a fully qualified domain name. The fqdn is resolved to an IP address by the controller. DNS service shall health monitor the resolved IP address while it will  return the fqdn in the DNS response."),
        required=False,
        update_allowed=True,
    )
    ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP Address of the Local Virtual Service."),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )
    ratio_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Overrides the default ratio of 1.  Reduces the percentage the LB algorithm would pick the server in relation to its peers.  Range is 1-20."),
        required=False,
        update_allowed=True,
    )
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or Disable member to decide if this address should be provided in DNS responses."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'cluster_uuid',
        'vs_uuid',
        'fqdn',
        'ip',
        'ratio',
        'enabled',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'cluster_uuid': cluster_uuid_schema,
        'vs_uuid': vs_uuid_schema,
        'fqdn': fqdn_schema,
        'ip': ip_schema,
        'ratio': ratio_schema,
        'enabled': enabled_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip': getattr(IpAddr, 'field_references', {}),
    }



class GslbHealthMonitor(AviResource):
    resource_name = "gslbhealthmonitor"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("A user friendly name for this health monitor."),
        required=True,
        update_allowed=True,
    )
    send_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Frequency, in seconds, that monitors are sent to a server."),
        required=False,
        update_allowed=True,
    )
    receive_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A valid response from the server is expected within the receive timeout window.  This timeout must be less than the send interval.  If server status is regularly flapping up and down, consider increasing this value."),
        required=False,
        update_allowed=True,
    )
    successful_checks_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of continuous successful health checks before server is marked up."),
        required=False,
        update_allowed=True,
    )
    failed_checks_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of continuous failed health checks before the server is marked down."),
        required=False,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Type of the health monitor."),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['HEALTH_MONITOR_DNS', 'HEALTH_MONITOR_HTTPS', 'HEALTH_MONITOR_EXTERNAL', 'HEALTH_MONITOR_UDP', 'HEALTH_MONITOR_TCP', 'HEALTH_MONITOR_HTTP', 'HEALTH_MONITOR_PING', 'HEALTH_MONITOR_GSLB']),
        ],
    )
    tcp_monitor_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HealthMonitorTcp.properties_schema,
        required=False,
        update_allowed=True,
    )
    http_monitor_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HealthMonitorHttp.properties_schema,
        required=False,
        update_allowed=True,
    )
    https_monitor_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HealthMonitorHttp.properties_schema,
        required=False,
        update_allowed=True,
    )
    external_monitor_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HealthMonitorExternal.properties_schema,
        required=False,
        update_allowed=True,
    )
    udp_monitor_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HealthMonitorUdp.properties_schema,
        required=False,
        update_allowed=True,
    )
    dns_monitor_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HealthMonitorDNS.properties_schema,
        required=False,
        update_allowed=True,
    )
    monitor_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Use this port instead of the port defined for the server in the Pool. If the monitor succeeds to this port, the load balanced traffic will still be sent to the port of the server defined within the Pool."),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'send_interval',
        'receive_timeout',
        'successful_checks',
        'failed_checks',
        'type',
        'tcp_monitor',
        'http_monitor',
        'https_monitor',
        'external_monitor',
        'udp_monitor',
        'dns_monitor',
        'monitor_port',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'send_interval': send_interval_schema,
        'receive_timeout': receive_timeout_schema,
        'successful_checks': successful_checks_schema,
        'failed_checks': failed_checks_schema,
        'type': type_schema,
        'tcp_monitor': tcp_monitor_schema,
        'http_monitor': http_monitor_schema,
        'https_monitor': https_monitor_schema,
        'external_monitor': external_monitor_schema,
        'udp_monitor': udp_monitor_schema,
        'dns_monitor': dns_monitor_schema,
        'monitor_port': monitor_port_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'https_monitor': getattr(HealthMonitorHttp, 'field_references', {}),
        'dns_monitor': getattr(HealthMonitorDNS, 'field_references', {}),
        'tcp_monitor': getattr(HealthMonitorTcp, 'field_references', {}),
        'udp_monitor': getattr(HealthMonitorUdp, 'field_references', {}),
        'http_monitor': getattr(HealthMonitorHttp, 'field_references', {}),
        'external_monitor': getattr(HealthMonitorExternal, 'field_references', {}),
    }



class GslbSite(object):
    # all schemas
    cluster_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the 'Cluster' object of the Controller Cluster in this site."),
        required=True,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name for the Site Controller Cluster."),
        required=True,
        update_allowed=True,
    )
    address_schema = properties.Schema(
        properties.Schema.STRING,
        _("IP Address or a DNS resolvable, fully qualified domain name of the Site Controller Cluster."),
        required=False,
        update_allowed=True,
    )
    ip_addresses_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=False,
    )
    ip_addresses_schema = properties.Schema(
        properties.Schema.LIST,
        _("IP Address(es) of the Site's Cluster. For a 3-node cluster, either the cluster vIP is provided, or the list of controller IPs in the cluster are provided."),
        schema=ip_addresses_item_schema,
        required=False,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The Site Controller Cluster's REST API port number."),
        required=False,
        update_allowed=True,
    )
    username_schema = properties.Schema(
        properties.Schema.STRING,
        _("The username used when authenticating with the Site. "),
        required=False,
        update_allowed=True,
    )
    password_schema = properties.Schema(
        properties.Schema.STRING,
        _("The password used when authenticating with the Site."),
        required=False,
        update_allowed=True,
    )
    dns_vs_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    dns_vs_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("The list of DNS-VSes on which the GSes shall be placed. The site has to be an ACTIVE member."),
        schema=dns_vs_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    member_type_schema = properties.Schema(
        properties.Schema.STRING,
        _("The site's member type: A leader is set to ACTIVE while allmembers are set to passive. "),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['GSLB_PASSIVE_MEMBER', 'GSLB_ACTIVE_MEMBER']),
        ],
    )
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or disable the Site.  This is useful in maintenance scenarios such as upgrade and routine maintenance.  A disabled site's configuration shall be retained but it will not get any new configuration updates.  It shall not participate in Health-Status monitoring.  VIPs of the Virtual Services on the disabled site shall not be sent in DNS response.  When a site transitions from disabled to enabled, it is treated similar to the addition of a new site."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'cluster_uuid',
        'name',
        'address',
        'ip_addresses',
        'port',
        'username',
        'password',
        'dns_vs_uuids',
        'member_type',
        'enabled',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'cluster_uuid': cluster_uuid_schema,
        'name': name_schema,
        'address': address_schema,
        'ip_addresses': ip_addresses_schema,
        'port': port_schema,
        'username': username_schema,
        'password': password_schema,
        'dns_vs_uuids': dns_vs_uuids_schema,
        'member_type': member_type_schema,
        'enabled': enabled_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip_addresses': getattr(IpAddr, 'field_references', {}),
    }



class GslbServiceDownResponse(object):
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Response from DNS service towards the client when the Gslb Service is DOWN."),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['GSLB_SERVICE_DOWN_RESPONSE_EMPTY', 'GSLB_SERVICE_DOWN_RESPONSE_NONE', 'GSLB_SERVICE_DOWN_RESPONSE_ALL_RECORDS', 'GSLB_SERVICE_DOWN_RESPONSE_FALLBACK_IP']),
        ],
    )
    fallback_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("Fallback IP address to use in response to the client query when the Gslb Service is DOWN."),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'type',
        'fallback_ip',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'fallback_ip': fallback_ip_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'fallback_ip': getattr(IpAddr, 'field_references', {}),
    }



class Gslb(AviResource):
    resource_name = "gslb"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name for the Gslb."),
        required=True,
        update_allowed=True,
    )
    dns_configs_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DNSConfig.properties_schema,
        required=True,
        update_allowed=False,
    )
    dns_configs_schema = properties.Schema(
        properties.Schema.LIST,
        _("Sub domain configuration for this Gslb. GslbService FQDN must be a match one of these subdomains. "),
        schema=dns_configs_item_schema,
        required=False,
        update_allowed=True,
    )
    sites_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=GslbSite.properties_schema,
        required=True,
        update_allowed=False,
    )
    sites_schema = properties.Schema(
        properties.Schema.LIST,
        _("Select Site belonging to this Gslb."),
        schema=sites_item_schema,
        required=False,
        update_allowed=True,
    )
    leader_cluster_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Mark this Site as leader of Gslb configuration.  This is the one among the sites."),
        required=True,
        update_allowed=True,
    )
    send_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Frequency with which group members communicate."),
        required=False,
        update_allowed=True,
    )
    clear_on_max_retries_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Max retries after which the remote site is treatedas a fresh start. In fresh start all the configsare downloaded."),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'dns_configs',
        'sites',
        'leader_cluster_uuid',
        'send_interval',
        'clear_on_max_retries',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'dns_configs': dns_configs_schema,
        'sites': sites_schema,
        'leader_cluster_uuid': leader_cluster_uuid_schema,
        'send_interval': send_interval_schema,
        'clear_on_max_retries': clear_on_max_retries_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'sites': getattr(GslbSite, 'field_references', {}),
        'dns_configs': getattr(DNSConfig, 'field_references', {}),
    }



class GslbPool(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the Gslb Service Pool."),
        required=True,
        update_allowed=True,
    )
    priority_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Priority of this pool of Members. If the priority of this is the highest in the group, DNS service picks up only this member for DNS responses."),
        required=False,
        update_allowed=True,
    )
    algorithm_schema = properties.Schema(
        properties.Schema.STRING,
        _("The load balancing algorithm will pick a local member within the Gslb Service list of available Members."),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['GSLB_ALGORITHM_CONSISTENT_HASH', 'GSLB_ALGORITHM_ROUND_ROBIN']),
        ],
    )
    consistent_hash_mask_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Mask to be applied on client IP for consistent hash algorithm."),
        required=False,
        update_allowed=True,
    )
    members_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=GslbPoolMember.properties_schema,
        required=True,
        update_allowed=False,
    )
    members_schema = properties.Schema(
        properties.Schema.LIST,
        _("Select list of Virtual Services belonging to this Gslb."),
        schema=members_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'priority',
        'algorithm',
        'consistent_hash_mask',
        'members',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'priority': priority_schema,
        'algorithm': algorithm_schema,
        'consistent_hash_mask': consistent_hash_mask_schema,
        'members': members_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'members': getattr(GslbPoolMember, 'field_references', {}),
    }



class GslbService(AviResource):
    resource_name = "gslbservice"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name for the Gslb Service."),
        required=True,
        update_allowed=True,
    )
    domain_names_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    domain_names_schema = properties.Schema(
        properties.Schema.LIST,
        _("Fully qualified domain name of the Gslb Service."),
        schema=domain_names_item_schema,
        required=False,
        update_allowed=True,
    )
    groups_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=GslbPool.properties_schema,
        required=True,
        update_allowed=False,
    )
    groups_schema = properties.Schema(
        properties.Schema.LIST,
        _("Select list of pools belonging to this Gslb Service."),
        schema=groups_item_schema,
        required=False,
        update_allowed=True,
    )
    num_dns_ip_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of IP addresses of this Gslb Service to be returned by the DNS Service. Enter 0 to return all IP addresses."),
        required=False,
        update_allowed=True,
    )
    ttl_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("TTL value (in seconds) for records served for this Gslb Service by the DNS Service."),
        required=False,
        update_allowed=True,
    )
    down_response_schema = properties.Schema(
        properties.Schema.MAP,
        _("Response to the client query when the Gslb Service is DOWN."),
        schema=GslbServiceDownResponse.properties_schema,
        required=False,
        update_allowed=True,
    )
    health_monitor_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    health_monitor_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("Verify VS health by applying one or more health monitors.  Active monitors generate synthetic traffic from DNS Service Engine and to mark a VS up or down based on the response.  You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        schema=health_monitor_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    controller_health_status_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("GS member's overall health status is derived based on a combination of controller and datapath health-status inputs. Datapath status is determined by the association of health monitor profiles, while the controller provided status is determined through this configuration. "),
        required=False,
        update_allowed=True,
    )
    health_monitor_scope_schema = properties.Schema(
        properties.Schema.STRING,
        _("Health monitor probe can be executed for all the members or it can be executed only for Non-Avi members. This operational mode is useful to reduce the number of health monitor probes in case of a hybrid scenario where Avi members can have controller derived status while Non-Avi members can be probed by via health monitor probes in dataplane."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['GSLB_SERVICE_HEALTH_MONITOR_ONLY_NON_AVI_MEMBERS', 'GSLB_SERVICE_HEALTH_MONITOR_ALL_MEMBERS']),
        ],
    )
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or disable the Gslb Service. If the Gslb Service is enabled, then the VIPs are sent in the DNS responses based on reachability and configured algorithm. If the Gslb Service is disabled, then the VIPs are no longer available in the DNS response."),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'domain_names',
        'groups',
        'num_dns_ip',
        'ttl',
        'down_response',
        'health_monitor_uuids',
        'controller_health_status_enabled',
        'health_monitor_scope',
        'enabled',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'domain_names': domain_names_schema,
        'groups': groups_schema,
        'num_dns_ip': num_dns_ip_schema,
        'ttl': ttl_schema,
        'down_response': down_response_schema,
        'health_monitor_uuids': health_monitor_uuids_schema,
        'controller_health_status_enabled': controller_health_status_enabled_schema,
        'health_monitor_scope': health_monitor_scope_schema,
        'enabled': enabled_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'health_monitor_uuids': 'gslbhealthmonitor',
        'down_response': getattr(GslbServiceDownResponse, 'field_references', {}),
        'groups': getattr(GslbPool, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::GslbHealthMonitor': GslbHealthMonitor,
        'Avi::LBaaS::GslbService': GslbService,
        'Avi::LBaaS::Gslb': Gslb,
    }

