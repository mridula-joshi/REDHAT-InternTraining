**Setup Devstack** : 
      VM :CentOS
      Add a stack user
      Clone the git repo:git clone https://opendev.org/openstack/devstack/ 
      cd devstack
      Configure local.conf and start installation by runing ./stack.sh
**Working on Devstack**:
    source devstack/openrc username project_name
    Issue a token to communicate with the services: openstack issue token 
    
**API_REFRENCE GUIDE USED**:
    https://docs.openstack.org/api-ref/block-storage/

**CURL-COMMANDS**:
**1.GET:show a volumes details**
**Command:** curl -i -X GET -H "X-Auth-Token: gAAAAABg7slo9xlNBFvD_kYMhFi3LmHxvqrIz0ahgvvKlb8x585QvNVcHGikQDW4LnY2IiTIoKCUsrqkltyDnTCen6unrQ3TJvZHubAYuTv8jlfObS-AXub9UVLoRX70IfxcP_ezjbxujcL8d8NTLrW3X7NQhxtR0Di8EYQ4P990mQ0PtQ69R-8" http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes/9712a5c9-0efc-4eda-9ad6-d39007751fa4
HTTP/1.1 200 OK
Date: Wed, 14 Jul 2021 12:08:35 GMT
Server: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_wsgi/4.6.4 Python/3.6
Content-Type: application/json
x-compute-request-id: req-6f761de5-01cd-46ae-ad01-eccc7165adfb
Content-Length: 1498
OpenStack-API-Version: volume 3.0
Vary: OpenStack-API-Version
x-openstack-request-id: req-6f761de5-01cd-46ae-ad01-eccc7165adfb
Connection: close
**RESPONSE:**
{"volume": {"id": "9712a5c9-0efc-4eda-9ad6-d39007751fa4", "status": "available", "size": 8, "availability_zone": "nova", "created_at": "2021-07-14T09:30:46.000000", "updated_at": "2021-07-14T09:30:48.000000", "name": "my-new-volume", "description": null, "volume_type": "lvmdriver-1", "snapshot_id": null, "source_volid": null, "metadata": {}, "links": [{"rel": "self", "href": "http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes/9712a5c9-0efc-4eda-9ad6-d39007751fa4"}, {"rel": "bookmark", "href": "http://10.0.78.192/volume/bde05f7e96b244d598f3f1c0a44ea088/volumes/9712a5c9-0efc-4eda-9ad6-d39007751fa4"}], "user_id": "a8fc74c7eba540b1bad62914f49e9336", "bootable": "true", "encrypted": false, "replication_status": null, "consistencygroup_id": null, "multiattach": false, "attachments": [], "migration_status": null, "os-vol-tenant-attr:tenant_id": "bde05f7e96b244d598f3f1c0a44ea088", "os-vol-mig-status-attr:migstat": null, "os-vol-mig-status-attr:name_id": null, "volume_image_metadata": {"hw_rng_model": "virtio", "owner_specified.openstack.md5": "", "owner_specified.openstack.sha256": "", "owner_specified.openstack.object": "images/cirros-0.5.2-x86_64-disk", "image_id": "01130109-0a8b-4001-9ee7-dad4028951da", "image_name": "cirros-0.5.2-x86_64-disk", "checksum": "b874c39491a2377b8490f5f1e89761a4", "container_format": "bare", "disk_format": "qcow2", "min_disk": "0", "min_ram": "0", "size": "16300544"}, "os-vol-host-attr:host": "mridula-test@lvmdriver-1#lvmdriver-1"}}

**2.GET:list all accessible volumes**
**COMMAND:** curl -i -X GET -H "X-Auth-Token: gAAAAABg776IK3-_5Ml0JIjSOF42JeFPfiNRoEgxs0JbrL-chKzkg_7ccUv6wOyOuMdp6nXi6drWOuslJ2ruvbe5_kVEHQXjYO6xMmZd4151DAR26MPFuY33XtBhrmvOnt-uNSSndNoRHt3ULFFpSuuwl3sCDYEKOrmuR9AiKL3-S6oQpzJkCvw"  http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes
HTTP/1.1 200 OK
Date: Thu, 15 Jul 2021 04:53:52 GMT
Server: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_wsgi/4.6.4 Python/3.6
Content-Type: application/json
x-compute-request-id: req-a6a92165-5dc6-4ace-b856-4e020487bda8
Content-Length: 368
OpenStack-API-Version: volume 3.0
Vary: OpenStack-API-Version
x-openstack-request-id: req-a6a92165-5dc6-4ace-b856-4e020487bda8
Connection: close
**RESPONSE:**
{"volumes": [{"id": "9712a5c9-0efc-4eda-9ad6-d39007751fa4", "name": "my-new-volume", "links": [{"rel": "self", "href": "http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes/9712a5c9-0efc-4eda-9ad6-d39007751fa4"}, {"rel": "bookmark", "href": "http://10.0.78.192/volume/bde05f7e96b244d598f3f1c0a44ea088/volumes/9712a5c9-0efc-4eda-9ad6-d39007751fa4"}]}]}



**3.POST: create volume**
**COMMAND:** curl -i -X POST -H "X-Auth-Token: gAAAAABg7yE1KBg3XiQRLn-8KpjGnkrjO_bSCN9WTZhKHcT2AR3ip7-eVIEL5_IOc_tgVfxsG-0dAAxwsFo9JhUlGh6R5Ns1tksKvJlh2SWIXsaXT00NDIPVgs9h3fnb1i6oLzgQgULJ56PCk-6-iUnWQONUut2wS4UBsu21a476ABkMVh4dIZQ" -H "Content-Type: application/json" -d '{"volume":{"size":8}}' http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes

HTTP/1.1 202 Accepted
Date: Wed, 14 Jul 2021 17:45:11 GMT
Server: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_wsgi/4.6.4 Python/3.6
Content-Type: application/json
x-compute-request-id: req-c8a36914-4452-4f0f-b1d6-5fc6999a2847
Content-Length: 802
OpenStack-API-Version: volume 3.0
Vary: OpenStack-API-Version
x-openstack-request-id: req-c8a36914-4452-4f0f-b1d6-5fc6999a2847
Connection: close
**RESPONSE:**
{"volume": {"id": "764839e2-7b19-4368-97fc-afd8c7d62784", "status": "creating", "size": 8, "availability_zone": "nova", "created_at": "2021-07-14T17:45:12.007078", "updated_at": null, "name": null, "description": null, "volume_type": "lvmdriver-1", "snapshot_id": null, "source_volid": null, "metadata": {}, "links": [{"rel": "self", "href": "http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes/764839e2-7b19-4368-97fc-afd8c7d62784"}, {"rel": "bookmark", "href": "http://10.0.78.192/volume/bde05f7e96b244d598f3f1c0a44ea088/volumes/764839e2-7b19-4368-97fc-afd8c7d62784"}], "user_id": "a8fc74c7eba540b1bad62914f49e9336", "bootable": "false", "encrypted": false, "replication_status": null, "consistencygroup_id": null, "multiattach": false, "attachments": [], "migration_status": null}}

**4.POST: create metadata for volume:**
**COMMAND:** curl -i -X POST -H "X-Auth-Token: gAAAAABg776IK3-_5Ml0JIjSOF42JeFPfiNRoEgxs0JbrL-chKzkg_7ccUv6wOyOuMdp6nXi6drWOuslJ2ruvbe5_kVEHQXjYO6xMmZd4151DAR26MPFuY33XtBhrmvOnt-uNSSndNoRHt3ULFFpSuuwl3sCDYEKOrmuR9AiKL3-S6oQpzJkCvw" -H "Content-Type: application/json" -d '{"metadata":{"name":"metadata0"}}' http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes/5188e9ce-f02d-4626-979f-fc25534eebb9/metadata
HTTP/1.1 200 OK
Date: Thu, 15 Jul 2021 05:05:31 GMT
Server: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_wsgi/4.6.4 Python/3.6
Content-Type: application/json
x-compute-request-id: req-d1a45b61-c3bf-4eff-ae83-6c8f4b9bca11
Content-Length: 35
OpenStack-API-Version: volume 3.0
Vary: OpenStack-API-Version
x-openstack-request-id: req-d1a45b61-c3bf-4eff-ae83-6c8f4b9bca11
Connection: close
**RESPONSE:**
{"metadata": {"name": "metadata0"}}



**5.PUT: update volume**
**COMMAND:** curl -i -X PUT -H "X-Auth-Token: gAAAAABg7yE1KBg3XiQRLn-8KpjGnkrjO_bSCN9WTZhKHcT2AR3ip7-eVIEL5_IOc_tgVfxsG-0dAAxwsFo9JhUlGh6R5Ns1tksKvJlh2SWIXsaXT00NDIPVgs9h3fnb1i6oLzgQgULJ56PCk-6-iUnWQONUut2wS4UBsu21a476ABkMVh4dIZQ" -H "Content-Type: application/json" -d '{"volume":{"name":"new"}}' http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes/764839e2-7b19-4368-97fc-afd8c7d62784
HTTP/1.1 200 OK
Date: Wed, 14 Jul 2021 17:55:04 GMT
Server: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_wsgi/4.6.4 Python/3.6
Content-Type: application/json
x-compute-request-id: req-ff1b055a-7d0b-4b16-a0e9-14f5c54939f7
Content-Length: 828
OpenStack-API-Version: volume 3.0
Vary: OpenStack-API-Version
x-openstack-request-id: req-ff1b055a-7d0b-4b16-a0e9-14f5c54939f7
Connection: close
**RESPONSE:**
{"volume": {"id": "764839e2-7b19-4368-97fc-afd8c7d62784", "status": "available", "size": 8, "availability_zone": "nova", "created_at": "2021-07-14T17:45:12.000000", "updated_at": "2021-07-14T17:45:12.000000", "name": "new", "description": null, "volume_type": "lvmdriver-1", "snapshot_id": null, "source_volid": null, "metadata": {}, "links": [{"rel": "self", "href": "http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes/764839e2-7b19-4368-97fc-afd8c7d62784"}, {"rel": "bookmark", "href": "http://10.0.78.192/volume/bde05f7e96b244d598f3f1c0a44ea088/volumes/764839e2-7b19-4368-97fc-afd8c7d62784"}], "user_id": "a8fc74c7eba540b1bad62914f49e9336", "bootable": "false", "encrypted": false, "replication_status": null, "consistencygroup_id": null, "multiattach": false, "attachments": [], "migration_status": null}}

**6.PUT: update metadata **  

**COMMAND:** curl -i -X PUT -H "X-Auth-Token: gAAAAABg776IK3-_5Ml0JIjSOF42JeFPfiNRoEgxs0JbrL-chKzkg_7ccUv6wOyOuMdp6nXi6drWOuslJ2ruvbe5_kVEHQXjYO6xMmZd4151DAR26MPFuY33XtBhrmvOnt-uNSSndNoRHt3ULFFpSuuwl3sCDYEKOrmuR9AiKL3-S6oQpzJkCvw" -H "Content-Type: application/json" -d '{"metadata":{"name":"metadata1"}}' http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes/5188e9ce-f02d-4626-979f-fc25534eebb9/metadata
HTTP/1.1 200 OK
Date: Thu, 15 Jul 2021 05:11:57 GMT
Server: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_wsgi/4.6.4 Python/3.6
Content-Type: application/json
x-compute-request-id: req-640e9957-ae78-406e-bfdf-db2fe8f3c740
Content-Length: 35
OpenStack-API-Version: volume 3.0
Vary: OpenStack-API-Version
x-openstack-request-id: req-640e9957-ae78-406e-bfdf-db2fe8f3c740
Connection: close
**RESPONSE**
{"metadata": {"name": "metadata1"}}


**DELETE:**

Before delete:
cinder list
+--------------------------------------+-----------+---------------+------+-------------+----------+-------------+
| ID                                   | Status    | Name          | Size | Volume Type | Bootable | Attached to |
+--------------------------------------+-----------+---------------+------+-------------+----------+-------------+
| 764839e2-7b19-4368-97fc-afd8c7d62784 | available | -             | 8    | lvmdriver-1 | false    |             |
| 9712a5c9-0efc-4eda-9ad6-d39007751fa4 | available | my-new-volume | 8    | lvmdriver-1 | true     |             |
+--------------------------------------+-----------+---------------+------+-------------+----------+-------------+


curl -i -X DELETE -H "X-Auth-Token: gAAAAABg7yE1KBg3XiQRLn-8KpjGnkrjO_bSCN9WTZhKHcT2AR3ip7-eVIEL5_IOc_tgVfxsG-0dAAxwsFo9JhUlGh6R5Ns1tksKvJlh2SWIXsaXT00NDIPVgs9h3fnb1i6oLzgQgULJ56PCk-6-iUnWQONUut2wS4UBsu21a476ABkMVh4dIZQ"  http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes/764839e2-7b19-4368-97fc-afd8c7d62784
HTTP/1.1 202 Accepted
Date: Wed, 14 Jul 2021 17:59:26 GMT
Server: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_wsgi/4.6.4 Python/3.6
Content-Length: 0
Content-Type: text/html; charset=UTF-8
OpenStack-API-Version: volume 3.0
Vary: OpenStack-API-Version
x-openstack-request-id: req-8ecc92f4-b051-4147-9e90-90797a91bc42
Connection: close



After DELETE:

cinder list
+--------------------------------------+-----------+---------------+------+-------------+----------+-------------+
| ID                                   | Status    | Name          | Size | Volume Type | Bootable | Attached to |
+--------------------------------------+-----------+---------------+------+-------------+----------+-------------+
| 9712a5c9-0efc-4eda-9ad6-d39007751fa4 | available | my-new-volume | 8    | lvmdriver-1 | true     |             |
+--------------------------------------+-----------+---------------+------+-------------+----------+-------------+



