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


class HealthMonitorSSLAttributes(object):
    # all schemas
    ssl_profile_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) SSL profile defines ciphers and SSL versions to be used for healthmonitor traffic to the back-end servers. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=True,
        update_allowed=True,
    )
    pki_profile_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) PKI profile used to validate the SSL certificate presented by a server. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    ssl_key_and_certificate_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Service engines will present this SSL certificate to the server. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ssl_profile_uuid',
        'pki_profile_uuid',
        'ssl_key_and_certificate_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ssl_profile_uuid': ssl_profile_uuid_schema,
        'pki_profile_uuid': pki_profile_uuid_schema,
        'ssl_key_and_certificate_uuid': ssl_key_and_certificate_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'pki_profile_uuid': 'pkiprofile',
        'ssl_profile_uuid': 'sslprofile',
        'ssl_key_and_certificate_uuid': 'sslkeyandcertificate',
    }



class HealthMonitorTcp(object):
    # all schemas
    tcp_request_schema = properties.Schema(
        properties.Schema.STRING,
        _("Request data to send after completing the TCP handshake."),
        required=False,
        update_allowed=True,
    )
    tcp_response_schema = properties.Schema(
        properties.Schema.STRING,
        _("Match for the desired keyword in the first 2Kb of the server's TCP response. If this field is left blank, no server response is required."),
        required=False,
        update_allowed=True,
    )
    maintenance_response_schema = properties.Schema(
        properties.Schema.STRING,
        _("Match or look for this keyword in the first 2KB of server's response indicating server maintenance.  A successful match results in the server being marked down."),
        required=False,
        update_allowed=True,
    )
    tcp_half_open_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Configure TCP health monitor to use half-open TCP connections to monitor the health of backend servers thereby avoiding consumption of a full fledged server side connection and the overhead and logs associated with it.  This method is light-weight as it makes use of listener in server's kernel layer to measure the health and a child socket or user thread is not created on the server side. (Default: False)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'tcp_request',
        'tcp_response',
        'maintenance_response',
        'tcp_half_open',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'tcp_request': tcp_request_schema,
        'tcp_response': tcp_response_schema,
        'maintenance_response': maintenance_response_schema,
        'tcp_half_open': tcp_half_open_schema,
    }



class HealthMonitorExternal(object):
    # all schemas
    command_path_schema = properties.Schema(
        properties.Schema.STRING,
        _("Path of external health monitor script."),
        required=False,
        update_allowed=True,
    )
    command_parameters_schema = properties.Schema(
        properties.Schema.STRING,
        _("Optional arguments to feed into the script."),
        required=False,
        update_allowed=True,
    )
    command_code_schema = properties.Schema(
        properties.Schema.STRING,
        _("Command script provided inline."),
        required=True,
        update_allowed=True,
    )
    command_variables_schema = properties.Schema(
        properties.Schema.STRING,
        _("Environment variables to be fed into the script."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'command_path',
        'command_parameters',
        'command_code',
        'command_variables',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'command_path': command_path_schema,
        'command_parameters': command_parameters_schema,
        'command_code': command_code_schema,
        'command_variables': command_variables_schema,
    }



class HealthMonitorHttp(object):
    # all schemas
    http_request_schema = properties.Schema(
        properties.Schema.STRING,
        _("Send an HTTP request to the server.  The default GET / HTTP/1.0 may be extended with additional headers or information.  For instance, GET /index.htm HTTP/1.1 Host: www.site.com Connection: Close"),
        required=False,
        update_allowed=True,
    )
    http_response_code_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("List of HTTP response codes to match as successful.  Default is 2xx."),
        required=True,
        update_allowed=False,
        constraints=[
            constraints.AllowedValues(['HTTP_1XX', 'HTTP_2XX', 'HTTP_3XX', 'HTTP_4XX', 'HTTP_5XX', 'HTTP_ANY']),
        ],
    )
    http_response_code_schema = properties.Schema(
        properties.Schema.LIST,
        _("List of HTTP response codes to match as successful.  Default is 2xx."),
        schema=http_response_code_item_schema,
        required=False,
        update_allowed=True,
    )
    http_response_schema = properties.Schema(
        properties.Schema.STRING,
        _("Match for a keyword in the first 2Kb of the server header and body response."),
        required=False,
        update_allowed=True,
    )
    maintenance_code_item_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Match or look for this HTTP response code indicating server maintenance.  A successful match results in the server being marked down."),
        required=True,
        update_allowed=False,
    )
    maintenance_code_schema = properties.Schema(
        properties.Schema.LIST,
        _("Match or look for this HTTP response code indicating server maintenance.  A successful match results in the server being marked down."),
        schema=maintenance_code_item_schema,
        required=False,
        update_allowed=True,
    )
    maintenance_response_schema = properties.Schema(
        properties.Schema.STRING,
        _("Match or look for this keyword in the first 2KB of server header and body response indicating server maintenance.  A successful match results in the server being marked down."),
        required=False,
        update_allowed=True,
    )
    ssl_attributes_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) SSL attributes for HTTPS health monitor."),
        schema=HealthMonitorSSLAttributes.properties_schema,
        required=False,
        update_allowed=True,
    )
    exact_http_request_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.6,17.2.2) Use the exact http_request string as specified by user, without any automatic insert of headers like Host header. (Default: False)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'http_request',
        'http_response_code',
        'http_response',
        'maintenance_code',
        'maintenance_response',
        'ssl_attributes',
        'exact_http_request',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'http_request': http_request_schema,
        'http_response_code': http_response_code_schema,
        'http_response': http_response_schema,
        'maintenance_code': maintenance_code_schema,
        'maintenance_response': maintenance_response_schema,
        'ssl_attributes': ssl_attributes_schema,
        'exact_http_request': exact_http_request_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ssl_attributes': getattr(HealthMonitorSSLAttributes, 'field_references', {}),
    }

    unique_keys = {
        'ssl_attributes': getattr(HealthMonitorSSLAttributes, 'unique_keys', {}),
    }



class HealthMonitorUdp(object):
    # all schemas
    udp_request_schema = properties.Schema(
        properties.Schema.STRING,
        _("Send UDP request."),
        required=False,
        update_allowed=True,
    )
    udp_response_schema = properties.Schema(
        properties.Schema.STRING,
        _("Match for keyword in the UDP response."),
        required=False,
        update_allowed=True,
    )
    maintenance_response_schema = properties.Schema(
        properties.Schema.STRING,
        _("Match or look for this keyword in the first 2KB of server's response indicating server maintenance.  A successful match results in the server being marked down."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'udp_request',
        'udp_response',
        'maintenance_response',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'udp_request': udp_request_schema,
        'udp_response': udp_response_schema,
        'maintenance_response': maintenance_response_schema,
    }



class HealthMonitorDNS(object):
    # all schemas
    query_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("The DNS monitor will query the DNS server for the fully qualified name in this field."),
        required=True,
        update_allowed=True,
    )
    qtype_schema = properties.Schema(
        properties.Schema.STRING,
        _("  Query_Type: Response has atleast one answer of which      the resource record type matches the query type   Any_Type: Response should contain atleast one answer  AnyThing: An empty answer is enough (Default: DNS_QUERY_TYPE)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DNS_ANY_THING', 'DNS_ANY_TYPE', 'DNS_QUERY_TYPE']),
        ],
    )
    rcode_schema = properties.Schema(
        properties.Schema.STRING,
        _("When No Error is selected, a DNS query will be marked failed is any error code is returned by the server.  With Any selected, the monitor ignores error code in the responses. (Default: RCODE_NO_ERROR)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['RCODE_ANYTHING', 'RCODE_NO_ERROR']),
        ],
    )
    response_string_schema = properties.Schema(
        properties.Schema.STRING,
        _("The resource record of the queried DNS server's response for the Request Name must include the IP address defined in this field. "),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'query_name',
        'qtype',
        'rcode',
        'response_string',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'query_name': query_name_schema,
        'qtype': qtype_schema,
        'rcode': rcode_schema,
        'response_string': response_string_schema,
    }



class HealthMonitor(AviResource):
    resource_name = "healthmonitor"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("A user friendly name for this health monitor."),
        required=True,
        update_allowed=True,
    )
    send_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Frequency, in seconds, that monitors are sent to a server. (Units: SEC) (Default: 10)"),
        required=False,
        update_allowed=True,
    )
    receive_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A valid response from the server is expected within the receive timeout window.  This timeout must be less than the send interval.  If server status is regularly flapping up and down, consider increasing this value. (Units: SEC) (Default: 4)"),
        required=False,
        update_allowed=True,
    )
    successful_checks_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of continuous successful health checks before server is marked up. (Default: 2)"),
        required=False,
        update_allowed=True,
    )
    failed_checks_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of continuous failed health checks before the server is marked down. (Default: 2)"),
        required=False,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Type of the health monitor."),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['HEALTH_MONITOR_DNS', 'HEALTH_MONITOR_EXTERNAL', 'HEALTH_MONITOR_GSLB', 'HEALTH_MONITOR_HTTP', 'HEALTH_MONITOR_HTTPS', 'HEALTH_MONITOR_PING', 'HEALTH_MONITOR_TCP', 'HEALTH_MONITOR_UDP']),
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
    is_federated_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.3) This field describes the object's replication scope. If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines.  If the field is set to true, then the object is replicated across the federation.   (Default: False)"),
        required=False,
        update_allowed=False,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
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
        'is_federated',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
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
        'is_federated': is_federated_schema,
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

    unique_keys = {
        'https_monitor': getattr(HealthMonitorHttp, 'unique_keys', {}),
        'dns_monitor': getattr(HealthMonitorDNS, 'unique_keys', {}),
        'tcp_monitor': getattr(HealthMonitorTcp, 'unique_keys', {}),
        'udp_monitor': getattr(HealthMonitorUdp, 'unique_keys', {}),
        'http_monitor': getattr(HealthMonitorHttp, 'unique_keys', {}),
        'external_monitor': getattr(HealthMonitorExternal, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::HealthMonitor': HealthMonitor,
    }

