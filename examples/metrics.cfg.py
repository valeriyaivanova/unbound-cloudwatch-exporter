"""
metrics.cfg.py: Contains the complete mapping of the Unbound stats to CloudWatch metrics
Author: Anthony Teisseire @ Technofy
License: MIT
"""

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