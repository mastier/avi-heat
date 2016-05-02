# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from options import *


class ControllerProperties(AviResource):
    resource_name = "controllerproperties"
    # all schemas
    dummy_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    unresponsive_se_reboot_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    crashed_se_reboot_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    se_offline_del_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    vs_se_create_fail_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    vs_se_vnic_fail_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    vs_se_bootup_fail_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    se_vnic_cooldown_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    vs_se_vnic_ip_fail_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    fatal_error_lease_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    upgrade_lease_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    query_host_fail_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    vnic_op_fail_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    dns_refresh_period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    se_create_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    max_dead_se_in_grp_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    dead_se_detection_timer_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    api_idle_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    allow_unauthenticated_nodes_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
    )
    cluster_ip_gratuitous_arp_period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    vs_key_rotate_period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    secure_channel_controller_token_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    secure_channel_se_token_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    max_seq_vnic_failures_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    vs_awaiting_se_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    vs_apic_scaleout_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Time to wait for the scaled out SE to become ready before marking the scaleout done, applies to APIC configuration only"),
        required=False,
    )
    secure_channel_cleanup_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    attach_ip_retry_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    attach_ip_retry_limit_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    persistence_key_rotate_period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'dummy',
        'unresponsive_se_reboot',
        'crashed_se_reboot',
        'se_offline_del',
        'vs_se_create_fail',
        'vs_se_vnic_fail',
        'vs_se_bootup_fail',
        'se_vnic_cooldown',
        'vs_se_vnic_ip_fail',
        'fatal_error_lease_time',
        'upgrade_lease_time',
        'query_host_fail',
        'vnic_op_fail_time',
        'dns_refresh_period',
        'se_create_timeout',
        'max_dead_se_in_grp',
        'dead_se_detection_timer',
        'api_idle_timeout',
        'allow_unauthenticated_nodes',
        'cluster_ip_gratuitous_arp_period',
        'vs_key_rotate_period',
        'secure_channel_controller_token_timeout',
        'secure_channel_se_token_timeout',
        'max_seq_vnic_failures',
        'vs_awaiting_se_timeout',
        'vs_apic_scaleout_timeout',
        'secure_channel_cleanup_timeout',
        'attach_ip_retry_interval',
        'attach_ip_retry_limit',
        'persistence_key_rotate_period',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'dummy': dummy_schema,
        'unresponsive_se_reboot': unresponsive_se_reboot_schema,
        'crashed_se_reboot': crashed_se_reboot_schema,
        'se_offline_del': se_offline_del_schema,
        'vs_se_create_fail': vs_se_create_fail_schema,
        'vs_se_vnic_fail': vs_se_vnic_fail_schema,
        'vs_se_bootup_fail': vs_se_bootup_fail_schema,
        'se_vnic_cooldown': se_vnic_cooldown_schema,
        'vs_se_vnic_ip_fail': vs_se_vnic_ip_fail_schema,
        'fatal_error_lease_time': fatal_error_lease_time_schema,
        'upgrade_lease_time': upgrade_lease_time_schema,
        'query_host_fail': query_host_fail_schema,
        'vnic_op_fail_time': vnic_op_fail_time_schema,
        'dns_refresh_period': dns_refresh_period_schema,
        'se_create_timeout': se_create_timeout_schema,
        'max_dead_se_in_grp': max_dead_se_in_grp_schema,
        'dead_se_detection_timer': dead_se_detection_timer_schema,
        'api_idle_timeout': api_idle_timeout_schema,
        'allow_unauthenticated_nodes': allow_unauthenticated_nodes_schema,
        'cluster_ip_gratuitous_arp_period': cluster_ip_gratuitous_arp_period_schema,
        'vs_key_rotate_period': vs_key_rotate_period_schema,
        'secure_channel_controller_token_timeout': secure_channel_controller_token_timeout_schema,
        'secure_channel_se_token_timeout': secure_channel_se_token_timeout_schema,
        'max_seq_vnic_failures': max_seq_vnic_failures_schema,
        'vs_awaiting_se_timeout': vs_awaiting_se_timeout_schema,
        'vs_apic_scaleout_timeout': vs_apic_scaleout_timeout_schema,
        'secure_channel_cleanup_timeout': secure_channel_cleanup_timeout_schema,
        'attach_ip_retry_interval': attach_ip_retry_interval_schema,
        'attach_ip_retry_limit': attach_ip_retry_limit_schema,
        'persistence_key_rotate_period': persistence_key_rotate_period_schema,
    }


def resource_mapping():
    return {
        'Avi::ControllerProperties': ControllerProperties,
    }
