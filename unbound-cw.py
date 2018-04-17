#!/usr/bin/env python

"""
unbound-cw.py: Fetch stats from Unbound remote control interface and push to AWS CloudWatch
Author: Anthony Teisseire @ Technofy
License: MIT
"""

import subprocess
import os
import boto3
import requests
import sys
import datetime

###################
# Configure here
###################
# AWS CloudWatch Custom Namespace
aws_namespace = "MyNamespace/Unbound"

# Map Unbound individual stats to AWS CloudWatch metrics
aws_metrics_mapping = {
    "total.num.queries": "NumQueries",
    "total.num.queries_ip_ratelimited": "NumQueriesIPRateLimited",
    "total.num.cachehits": "NumCacheHits",
    "total.num.cachemiss": "NumCacheMiss",
    "total.num.prefetch": "NumPrefetch",
    "total.num.zero_ttl": "NumZeroTTL",
    "total.num.recursivereplies": "RecursiveReplies",
    "total.requestlist.avg": "RequestListsAverage",
    "total.requestlist.max": "RequestListsMax",
    "total.requestlist.overwritten": "RequestListsOverwritten",
    "total.requestlist.exceeded": "RequestListsExceeded",
    "total.requestlist.current.all": "RequestListsCurrentAll",
    "total.requestlist.current.user": "RequestListsCurrentUser",
    "total.recursion.time.avg": "RecursionTimeAverage",
    "total.recursion.time.median": "RecursionTimeMedian",
    "total.tcpusage": "TcpUsage",
    "time.now": "TimeNow",
    "time.up": "TimeUp",
    "time.elapsed": "TimeElapsed"
}
# Unbound binaries path
ub_path = "/usr/sbin"


###################
# Program runs here
###################
# Call unbound control
ubct = os.path.join(ub_path, "unbound-control")
ub_stats_raw = subprocess.check_output(ubct + " stats", shell=True)
ub_stats = ub_stats_raw.split('\n')

# Try to get instance region
region_mdata_req = requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document')
region_mdata = region_mdata_req.json()['region']

# Raise an exception if something went wrong
region_mdata_req.raise_for_status()

# Try to get instance ID
inst_id_req = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
inst_id = inst_id_req.text

# Raise an exception if something went wrong
inst_id_req.raise_for_status()

# Connect to AWS CloudWatch
cw = boto3.client("cloudwatch", region_name=region_mdata)

# Iterate through gathered stats
for ub_stat in ub_stats:
    # Ignore empty lines
    if ub_stat.find('=') == -1:
        continue

    ubs_name, ubs_value = ub_stat.split('=')

    # Check if the metric is present in the mapping
    if ubs_name in aws_metrics_mapping:
        # Put metric on CloudWatch
        cw.put_metric_data(
            Namespace=aws_namespace,
            MetricData=[
                {
                    'MetricName': aws_metrics_mapping[ubs_name],
                    'Dimensions': [
                        {
                            'Name': 'InstanceId',
                            'Value': inst_id
                        }
                    ],
                    'Value': float(ubs_value),
                    'Timestamp': datetime.datetime.utcnow()
                }
            ]
        )