# DevStack

In case of devstack, the configuration files are in the path `/etc/ceilometer`.

```bash
$ sudo -u stack
$ cd /etc/ceilometer
# (list the files)
stack@devstack:/etc/ceilometer$ ls -la
total 52
drwxr-xr-x   2 stack stack  4096 Jul 23 12:20 .
drwxr-xr-x 121 root  root  12288 Jul 23 12:13 ..
-rw-r--r--   1 stack stack  1043 Jul 23 12:20 ceilometer.conf
-rw-r--r--   1 stack stack 18091 Jul 23 12:20 event_definitions.yaml
-rw-r--r--   1 stack stack   223 Jul 23 12:20 event_pipeline.yaml
-rw-r--r--   1 stack stack  3225 Jul 23 12:20 pipeline.yaml
-rw-r--r--   1 stack stack    87 Jul 23 12:20 polling.yaml
```

For more details, check the original guidelines
 [here](https://docs.openstack.org/mitaka/config-reference/telemetry/sample-configuration-files.html).