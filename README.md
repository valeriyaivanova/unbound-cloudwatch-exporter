# Unbound to AWS CloudWatch stats exporter

Fetch stats from Unbound remote control interface and push to AWS CloudWatch

## How to get running

Clone the repository and run :

`pip install -r requirements.txt`

Open the script and configure the Unbound binaries path, the AWS CloudWatch custom namespace and the metrics mapping:

```python
###################
# Configure here
###################
# AWS CloudWatch Custom Namespace
aws_namespace = "MyNamespace/Unbound"

# Map Unbound individual stats to AWS CloudWatch metrics
aws_metrics_mapping = {
    "total.num.recursivereplies": "RecursiveReplies",
    "total.tcpusage": "TcpUsage",
    "total.num.queries": "NumQueries",
}
# Unbound binaries path
ub_path = "/usr/local/sbin"
```

In the examples folder, you can find the complete list of stats exported by Unbound and the associated AWS CloudWatch metrics.
You can also find an example policy file to set as a role on AWS in order to give the right permissions to this script for pushing data to CloudWatch.

## License

Copyright 2017 Technofy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.