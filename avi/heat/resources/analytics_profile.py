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
from match import *


class ClientLogStreamingConfig(object):
    # all schemas
    external_server_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) The destination server IP address or hostname. If a name is provided, this should be resolvable on Avi Service Engines."),
        required=True,
        update_allowed=True,
    )
    external_server_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.1.1) The destination server's service port. (Default: 514)"),
        required=False,
        update_allowed=True,
    )
    log_types_to_send_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Type of logs to stream to the external server. Default is LOGS_ALL, i.e., send all logs. (Default: LOGS_ALL)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['LOGS_ALL', 'LOGS_SIGNIFICANT_ONLY', 'LOGS_UDF_ONLY', 'LOGS_UDF_SIGNIFICANT']),
        ],
    )
    max_logs_per_second_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.1.1) Maximum number of logs per second streamed to the remote server. By default, 100 logs per second are streamed. Set this to zero(0) to not enforce any limit. (Default: 100)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'external_server',
        'external_server_port',
        'log_types_to_send',
        'max_logs_per_second',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'external_server': external_server_schema,
        'external_server_port': external_server_port_schema,
        'log_types_to_send': log_types_to_send_schema,
        'max_logs_per_second': max_logs_per_second_schema,
    }



class ClientLogConfiguration(object):
    # all schemas
    enable_significant_log_collection_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable significant log collection. By default, this flag is enabled, which means that Avi SEs collect significant logs and forward them to Controller for further processing. For example, these logs correspond to error conditions such as when the response code for a request is 500. Users can disable this flag to turn off default significant log collection. (Default: True)"),
        required=False,
        update_allowed=True,
    )
    significant_log_processing_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Significant logs are processed by the Logs Analytics system according to this setting. (Default: LOGS_PROCESSING_SYNC_AND_INDEX_ON_DEMAND)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['LOGS_PROCESSING_AUTO_SYNC_AND_INDEX', 'LOGS_PROCESSING_AUTO_SYNC_BUT_INDEX_ON_DEMAND', 'LOGS_PROCESSING_NONE', 'LOGS_PROCESSING_SYNC_AND_INDEX_ON_DEMAND']),
        ],
    )
    filtered_log_processing_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) (Note: Only sync_and_index_on_demand is implemented at this time) Filtered logs are logs that match any client log filters or rules with logging enabled. Such logs are processed by the Logs Analytics system according to this setting. (Default: LOGS_PROCESSING_SYNC_AND_INDEX_ON_DEMAND)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['LOGS_PROCESSING_AUTO_SYNC_AND_INDEX', 'LOGS_PROCESSING_AUTO_SYNC_BUT_INDEX_ON_DEMAND', 'LOGS_PROCESSING_NONE', 'LOGS_PROCESSING_SYNC_AND_INDEX_ON_DEMAND']),
        ],
    )
    non_significant_log_processing_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) (Note: Only sync_and_index_on_demand is implemented at this time) Logs that are neither significant nor filtered, are processed by the Logs Analytics system according to this setting. (Default: LOGS_PROCESSING_SYNC_AND_INDEX_ON_DEMAND)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['LOGS_PROCESSING_AUTO_SYNC_AND_INDEX', 'LOGS_PROCESSING_AUTO_SYNC_BUT_INDEX_ON_DEMAND', 'LOGS_PROCESSING_NONE', 'LOGS_PROCESSING_SYNC_AND_INDEX_ON_DEMAND']),
        ],
    )

    # properties list
    PROPERTIES = (
        'enable_significant_log_collection',
        'significant_log_processing',
        'filtered_log_processing',
        'non_significant_log_processing',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'enable_significant_log_collection': enable_significant_log_collection_schema,
        'significant_log_processing': significant_log_processing_schema,
        'filtered_log_processing': filtered_log_processing_schema,
        'non_significant_log_processing': non_significant_log_processing_schema,
    }



class AnalyticsProfile(AviResource):
    resource_name = "analyticsprofile"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("The name of the analytics profile."),
        required=True,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    apdex_response_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("If a client receives an HTTP response in less than the Satisfactory Latency Threshold, the request is considered Satisfied. It is considered Tolerated if it is not Satisfied and less than Tolerated Latency Factor multiplied by the Satisfactory Latency Threshold. Greater than this number and the client's request is considered Frustrated. (Units: MILLISECONDS) (Default: 500)"),
        required=False,
        update_allowed=True,
    )
    apdex_response_tolerated_factor_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Client tolerated response latency factor. Client must receive a response within this factor times the satisfactory threshold (apdex_response_threshold) to be considered tolerated (Default: 4.0)"),
        required=False,
        update_allowed=True,
    )
    apdex_server_response_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A server HTTP response is considered Satisfied if latency is less than the Satisfactory Latency Threshold. The response is considered tolerated when it is greater than Satisfied but less than the Tolerated Latency Factor * S_Latency.  Greater than this number and the server response is considered Frustrated. (Units: MILLISECONDS) (Default: 400)"),
        required=False,
        update_allowed=True,
    )
    apdex_server_response_tolerated_factor_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Server tolerated response latency factor. Servermust response within this factor times the satisfactory threshold (apdex_server_response_threshold) to be considered tolerated (Default: 4.0)"),
        required=False,
        update_allowed=True,
    )
    apdex_rtt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Satisfactory client to Avi Round Trip Time(RTT). (Units: MILLISECONDS) (Default: 250)"),
        required=False,
        update_allowed=True,
    )
    apdex_rtt_tolerated_factor_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Tolerated client to Avi Round Trip Time(RTT) factor.  It is a multiple of apdex_rtt_tolerated_factor. (Default: 4.0)"),
        required=False,
        update_allowed=True,
    )
    apdex_server_rtt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Satisfactory client to Avi Round Trip Time(RTT). (Units: MILLISECONDS) (Default: 125)"),
        required=False,
        update_allowed=True,
    )
    apdex_server_rtt_tolerated_factor_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Tolerated client to Avi Round Trip Time(RTT) factor.  It is a multiple of apdex_rtt_tolerated_factor. (Default: 4.0)"),
        required=False,
        update_allowed=True,
    )
    apdex_rum_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("If a client is able to load a page in less than the Satisfactory Latency Threshold, the PageLoad is considered Satisfied.  It is considered tolerated if it is greater than Satisfied but less than the Tolerated Latency multiplied by Satisifed Latency. Greater than this number and the client's request is considered Frustrated.  A PageLoad includes the time for DNS lookup, download of all HTTP objects, and page render time. (Units: MILLISECONDS) (Default: 5000)"),
        required=False,
        update_allowed=True,
    )
    apdex_rum_tolerated_factor_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Virtual service threshold factor for tolerated Page Load Time (PLT) as multiple of apdex_rum_threshold. (Default: 4.0)"),
        required=False,
        update_allowed=True,
    )
    conn_lossy_total_rexmt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between client and Avi is considered lossy when more than this percentage of packets are retransmitted. (Units: PERCENT) (Default: 50)"),
        required=False,
        update_allowed=True,
    )
    conn_lossy_timeo_rexmt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between client and Avi is considered lossy when more than this percentage of packets are retransmitted due to timeout. (Units: PERCENT) (Default: 20)"),
        required=False,
        update_allowed=True,
    )
    conn_lossy_ooo_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between client and Avi is considered lossy when more than this percentage of out of order packets are received. (Units: PERCENT) (Default: 50)"),
        required=False,
        update_allowed=True,
    )
    conn_lossy_zero_win_size_event_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A client connection is considered lossy when percentage of times a packet could not be trasmitted due to TCP zero window is above this threshold. (Units: PERCENT) (Default: 2)"),
        required=False,
        update_allowed=True,
    )
    conn_server_lossy_total_rexmt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between Avi and server is considered lossy when more than this percentage of packets are retransmitted. (Units: PERCENT) (Default: 50)"),
        required=False,
        update_allowed=True,
    )
    conn_server_lossy_timeo_rexmt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between Avi and server is considered lossy when more than this percentage of packets are retransmitted due to timeout. (Units: PERCENT) (Default: 20)"),
        required=False,
        update_allowed=True,
    )
    conn_server_lossy_ooo_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between Avi and server is considered lossy when more than this percentage of out of order packets are received. (Units: PERCENT) (Default: 50)"),
        required=False,
        update_allowed=True,
    )
    conn_server_lossy_zero_win_size_event_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A server connection is considered lossy when percentage of times a packet could not be trasmitted due to TCP zero window is above this threshold. (Units: PERCENT) (Default: 2)"),
        required=False,
        update_allowed=True,
    )
    exclude_client_close_before_request_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude client closed connection before an HTTP request could be completed from being classified as an error. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    exclude_tcp_reset_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude TCP resets by client from the list of potential errors. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    exclude_server_tcp_reset_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude server TCP reset from errors.  It is common for applications like MS Exchange. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    exclude_persistence_change_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude persistence server changed while load balancing' from the list of errors. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    exclude_syn_retransmit_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude 'server unanswered syns' from the list of errors. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    exclude_invalid_dns_query_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude invalid dns queries from the list of errors. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    exclude_invalid_dns_domain_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude dns queries to domains outside the domains configured in the DNS application profile from the list of errors. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    exclude_no_dns_record_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude queries to domains that did not have configured services/records from the list of errors. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    exclude_unsupported_dns_query_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude unsupported dns queries from the list of errors. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    hs_performance_boost_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Adds free performance score credits to health score. It can be used for compensating health score for known slow applications. (Default: 0)"),
        required=False,
        update_allowed=True,
    )
    hs_max_anomaly_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum penalty that may be deducted from health score for anomalies. (Default: 10)"),
        required=False,
        update_allowed=True,
    )
    hs_max_resources_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum penalty that may be deducted from health score for high resource utilization. (Default: 25)"),
        required=False,
        update_allowed=True,
    )
    hs_max_security_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum penalty that may be deducted from health score based on security assessment. (Default: 100)"),
        required=False,
        update_allowed=True,
    )
    hs_security_nonpfs_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Penalty for allowing non-PFS handshakes. (Default: 1.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_weak_signature_algo_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Penalty for allowing weak signature algorithm(s). (Default: 1.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_ssl30_score_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when supporting SSL3.0 encryption protocol (Default: 3.5)"),
        required=False,
        update_allowed=True,
    )
    hs_security_tls10_score_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when supporting TLS1.0 encryption protocol (Default: 5.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_tls11_score_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when supporting TLS1.1 encryption protocol (Default: 5.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_tls12_score_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when supporting TLS1.2 encryption protocol (Default: 5.0)"),
        required=False,
        update_allowed=True,
    )
    hs_event_throttle_window_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Time window (in secs) within which only unique health change events should occur (Default: 1209600)"),
        required=False,
        update_allowed=True,
    )
    hs_min_dos_rate_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("DoS connection rate below which the DoS security assessment will not kick in. (Default: 1000)"),
        required=False,
        update_allowed=True,
    )
    hs_security_certscore_expired_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the certificate has expired (Default: 0.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_certscore_le07d_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the certificate expires in less than or equal to 7 days (Default: 2.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_certscore_le30d_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the certificate expires in less than or equal to 30 days (Default: 4.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_certscore_gt30d_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the certificate expires in more than 30 days (Default: 5.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_cipherscore_eq000b_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the minimum cipher strength is 0 bits (Default: 0.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_cipherscore_lt128b_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the minimum cipher strength is less than 128 bits (Default: 3.5)"),
        required=False,
        update_allowed=True,
    )
    hs_security_cipherscore_ge128b_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the minimum cipher strength is greater than equal to 128 bits (Default: 5.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_selfsignedcert_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Deprecated (Default: 1.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_encalgo_score_rc4_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when RC4 algorithm is used for encryption. (Default: 2.5)"),
        required=False,
        update_allowed=True,
    )
    hs_security_encalgo_score_none_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when no algorithm is used for encryption. (Default: 0.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_chain_invalidity_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Penalty for allowing certificates with invalid chain. (Default: 1.0)"),
        required=False,
        update_allowed=True,
    )
    hs_security_hsts_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Penalty for not enabling HSTS. (Default: 1.0)"),
        required=False,
        update_allowed=True,
    )
    disable_server_analytics_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Disable analytics on backend servers. This may be desired in container environment when there are large number of  ephemeral servers (Default: False)"),
        required=False,
        update_allowed=True,
    )
    disable_se_analytics_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Disable node (service engine) level analytics forvs metrics (Default: False)"),
        required=False,
        update_allowed=True,
    )
    hs_pscore_traffic_threshold_l4_client_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed. (Default: 10.0)"),
        required=False,
        update_allowed=True,
    )
    hs_pscore_traffic_threshold_l4_server_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed. (Default: 10.0)"),
        required=False,
        update_allowed=True,
    )
    exclude_gs_down_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude queries to GSLB services that are operationally down from the list of errors. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    exclude_no_valid_gs_member_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude queries to GSLB services that have no available members from the list of errors. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    client_log_config_schema = properties.Schema(
        properties.Schema.MAP,
        _("Configure which logs are sent to the Avi Controller from SEs and how they are processed."),
        schema=ClientLogConfiguration.properties_schema,
        required=False,
        update_allowed=True,
    )
    client_log_streaming_config_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.1.1) Configure to stream logs to an external server."),
        schema=ClientLogStreamingConfig.properties_schema,
        required=False,
        update_allowed=True,
    )
    exclude_http_error_codes_item_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("List of HTTP status codes to be excluded from being classified as an error.  Error connections or responses impacts health score, are included as significant logs, and may be classified as part of a DoS attack."),
        required=True,
        update_allowed=False,
    )
    exclude_http_error_codes_schema = properties.Schema(
        properties.Schema.LIST,
        _("List of HTTP status codes to be excluded from being classified as an error.  Error connections or responses impacts health score, are included as significant logs, and may be classified as part of a DoS attack."),
        schema=exclude_http_error_codes_item_schema,
        required=False,
        update_allowed=True,
    )
    ranges_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("List of HTTP status code ranges to be excluded from being classified as an error."),
        schema=HTTPStatusRange.properties_schema,
        required=True,
        update_allowed=False,
    )
    ranges_schema = properties.Schema(
        properties.Schema.LIST,
        _("List of HTTP status code ranges to be excluded from being classified as an error."),
        schema=ranges_item_schema,
        required=False,
        update_allowed=True,
    )
    resp_code_block_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("Block of HTTP response codes to be excluded from being classified as an error."),
        required=True,
        update_allowed=False,
        constraints=[
            constraints.AllowedValues(['AP_HTTP_RSP_4XX', 'AP_HTTP_RSP_5XX']),
        ],
    )
    resp_code_block_schema = properties.Schema(
        properties.Schema.LIST,
        _("Block of HTTP response codes to be excluded from being classified as an error."),
        schema=resp_code_block_item_schema,
        required=False,
        update_allowed=True,
    )
    exclude_server_dns_error_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude server dns error response from the list of errors. (Default: False)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'description',
        'apdex_response_threshold',
        'apdex_response_tolerated_factor',
        'apdex_server_response_threshold',
        'apdex_server_response_tolerated_factor',
        'apdex_rtt_threshold',
        'apdex_rtt_tolerated_factor',
        'apdex_server_rtt_threshold',
        'apdex_server_rtt_tolerated_factor',
        'apdex_rum_threshold',
        'apdex_rum_tolerated_factor',
        'conn_lossy_total_rexmt_threshold',
        'conn_lossy_timeo_rexmt_threshold',
        'conn_lossy_ooo_threshold',
        'conn_lossy_zero_win_size_event_threshold',
        'conn_server_lossy_total_rexmt_threshold',
        'conn_server_lossy_timeo_rexmt_threshold',
        'conn_server_lossy_ooo_threshold',
        'conn_server_lossy_zero_win_size_event_threshold',
        'exclude_client_close_before_request_as_error',
        'exclude_tcp_reset_as_error',
        'exclude_server_tcp_reset_as_error',
        'exclude_persistence_change_as_error',
        'exclude_syn_retransmit_as_error',
        'exclude_invalid_dns_query_as_error',
        'exclude_invalid_dns_domain_as_error',
        'exclude_no_dns_record_as_error',
        'exclude_unsupported_dns_query_as_error',
        'hs_performance_boost',
        'hs_max_anomaly_penalty',
        'hs_max_resources_penalty',
        'hs_max_security_penalty',
        'hs_security_nonpfs_penalty',
        'hs_security_weak_signature_algo_penalty',
        'hs_security_ssl30_score',
        'hs_security_tls10_score',
        'hs_security_tls11_score',
        'hs_security_tls12_score',
        'hs_event_throttle_window',
        'hs_min_dos_rate',
        'hs_security_certscore_expired',
        'hs_security_certscore_le07d',
        'hs_security_certscore_le30d',
        'hs_security_certscore_gt30d',
        'hs_security_cipherscore_eq000b',
        'hs_security_cipherscore_lt128b',
        'hs_security_cipherscore_ge128b',
        'hs_security_selfsignedcert_penalty',
        'hs_security_encalgo_score_rc4',
        'hs_security_encalgo_score_none',
        'hs_security_chain_invalidity_penalty',
        'hs_security_hsts_penalty',
        'disable_server_analytics',
        'disable_se_analytics',
        'hs_pscore_traffic_threshold_l4_client',
        'hs_pscore_traffic_threshold_l4_server',
        'exclude_gs_down_as_error',
        'exclude_no_valid_gs_member_as_error',
        'client_log_config',
        'client_log_streaming_config',
        'exclude_http_error_codes',
        'ranges',
        'resp_code_block',
        'exclude_server_dns_error_as_error',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'description': description_schema,
        'apdex_response_threshold': apdex_response_threshold_schema,
        'apdex_response_tolerated_factor': apdex_response_tolerated_factor_schema,
        'apdex_server_response_threshold': apdex_server_response_threshold_schema,
        'apdex_server_response_tolerated_factor': apdex_server_response_tolerated_factor_schema,
        'apdex_rtt_threshold': apdex_rtt_threshold_schema,
        'apdex_rtt_tolerated_factor': apdex_rtt_tolerated_factor_schema,
        'apdex_server_rtt_threshold': apdex_server_rtt_threshold_schema,
        'apdex_server_rtt_tolerated_factor': apdex_server_rtt_tolerated_factor_schema,
        'apdex_rum_threshold': apdex_rum_threshold_schema,
        'apdex_rum_tolerated_factor': apdex_rum_tolerated_factor_schema,
        'conn_lossy_total_rexmt_threshold': conn_lossy_total_rexmt_threshold_schema,
        'conn_lossy_timeo_rexmt_threshold': conn_lossy_timeo_rexmt_threshold_schema,
        'conn_lossy_ooo_threshold': conn_lossy_ooo_threshold_schema,
        'conn_lossy_zero_win_size_event_threshold': conn_lossy_zero_win_size_event_threshold_schema,
        'conn_server_lossy_total_rexmt_threshold': conn_server_lossy_total_rexmt_threshold_schema,
        'conn_server_lossy_timeo_rexmt_threshold': conn_server_lossy_timeo_rexmt_threshold_schema,
        'conn_server_lossy_ooo_threshold': conn_server_lossy_ooo_threshold_schema,
        'conn_server_lossy_zero_win_size_event_threshold': conn_server_lossy_zero_win_size_event_threshold_schema,
        'exclude_client_close_before_request_as_error': exclude_client_close_before_request_as_error_schema,
        'exclude_tcp_reset_as_error': exclude_tcp_reset_as_error_schema,
        'exclude_server_tcp_reset_as_error': exclude_server_tcp_reset_as_error_schema,
        'exclude_persistence_change_as_error': exclude_persistence_change_as_error_schema,
        'exclude_syn_retransmit_as_error': exclude_syn_retransmit_as_error_schema,
        'exclude_invalid_dns_query_as_error': exclude_invalid_dns_query_as_error_schema,
        'exclude_invalid_dns_domain_as_error': exclude_invalid_dns_domain_as_error_schema,
        'exclude_no_dns_record_as_error': exclude_no_dns_record_as_error_schema,
        'exclude_unsupported_dns_query_as_error': exclude_unsupported_dns_query_as_error_schema,
        'hs_performance_boost': hs_performance_boost_schema,
        'hs_max_anomaly_penalty': hs_max_anomaly_penalty_schema,
        'hs_max_resources_penalty': hs_max_resources_penalty_schema,
        'hs_max_security_penalty': hs_max_security_penalty_schema,
        'hs_security_nonpfs_penalty': hs_security_nonpfs_penalty_schema,
        'hs_security_weak_signature_algo_penalty': hs_security_weak_signature_algo_penalty_schema,
        'hs_security_ssl30_score': hs_security_ssl30_score_schema,
        'hs_security_tls10_score': hs_security_tls10_score_schema,
        'hs_security_tls11_score': hs_security_tls11_score_schema,
        'hs_security_tls12_score': hs_security_tls12_score_schema,
        'hs_event_throttle_window': hs_event_throttle_window_schema,
        'hs_min_dos_rate': hs_min_dos_rate_schema,
        'hs_security_certscore_expired': hs_security_certscore_expired_schema,
        'hs_security_certscore_le07d': hs_security_certscore_le07d_schema,
        'hs_security_certscore_le30d': hs_security_certscore_le30d_schema,
        'hs_security_certscore_gt30d': hs_security_certscore_gt30d_schema,
        'hs_security_cipherscore_eq000b': hs_security_cipherscore_eq000b_schema,
        'hs_security_cipherscore_lt128b': hs_security_cipherscore_lt128b_schema,
        'hs_security_cipherscore_ge128b': hs_security_cipherscore_ge128b_schema,
        'hs_security_selfsignedcert_penalty': hs_security_selfsignedcert_penalty_schema,
        'hs_security_encalgo_score_rc4': hs_security_encalgo_score_rc4_schema,
        'hs_security_encalgo_score_none': hs_security_encalgo_score_none_schema,
        'hs_security_chain_invalidity_penalty': hs_security_chain_invalidity_penalty_schema,
        'hs_security_hsts_penalty': hs_security_hsts_penalty_schema,
        'disable_server_analytics': disable_server_analytics_schema,
        'disable_se_analytics': disable_se_analytics_schema,
        'hs_pscore_traffic_threshold_l4_client': hs_pscore_traffic_threshold_l4_client_schema,
        'hs_pscore_traffic_threshold_l4_server': hs_pscore_traffic_threshold_l4_server_schema,
        'exclude_gs_down_as_error': exclude_gs_down_as_error_schema,
        'exclude_no_valid_gs_member_as_error': exclude_no_valid_gs_member_as_error_schema,
        'client_log_config': client_log_config_schema,
        'client_log_streaming_config': client_log_streaming_config_schema,
        'exclude_http_error_codes': exclude_http_error_codes_schema,
        'ranges': ranges_schema,
        'resp_code_block': resp_code_block_schema,
        'exclude_server_dns_error_as_error': exclude_server_dns_error_as_error_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ranges': getattr(HTTPStatusRange, 'field_references', {}),
        'client_log_config': getattr(ClientLogConfiguration, 'field_references', {}),
        'client_log_streaming_config': getattr(ClientLogStreamingConfig, 'field_references', {}),
    }

    unique_keys = {
        'ranges': getattr(HTTPStatusRange, 'unique_keys', {}),
        'client_log_config': getattr(ClientLogConfiguration, 'unique_keys', {}),
        'client_log_streaming_config': getattr(ClientLogStreamingConfig, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::AnalyticsProfile': AnalyticsProfile,
    }

