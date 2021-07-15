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
 1.Show  volumes details
  command:curl -i -X GET -H "X-Auth-Token: gAAAAABg7slo9xlNBFvD_kYMhFi3LmHxvqrIz0ahgvvKlb8x585QvNVcHGikQDW4LnY2IiTIoKCUsrqkltyDnTCen6unrQ3TJvZHubAYuTv8jlfObS-AXub9UVLoRX70IfxcP_ezjbxujcL8d8NTLrW3X7NQhxtR0Di8EYQ4P990mQ0PtQ69R-8" http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes/9712a5c9-0efc-4eda-9ad6-d39007751fa4
 Response Headers
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

  
  Request:
  {}
  Response:
  {"volume": {"id": "9712a5c9-0efc-4eda-9ad6-d39007751fa4", "status": "available", "size": 8, "availability_zone": "nova", "created_at": "2021-07-14T09:30:46.000000", "updated_at": "2021-07-14T09:30:48.000000", "name": "my-new-volume", "description": null, "volume_type": "lvmdriver-1", "snapshot_id": null, "source_volid": null, "metadata": {}, "links": [{"rel": "self", "href": "http://10.0.78.192/volume/v3/bde05f7e96b244d598f3f1c0a44ea088/volumes/9712a5c9-0efc-4eda-9ad6-d39007751fa4"}, {"rel": "bookmark", "href": "http://10.0.78.192/volume/bde05f7e96b244d598f3f1c0a44ea088/volumes/9712a5c9-0efc-4eda-9ad6-d39007751fa4"}], "user_id": "a8fc74c7eba540b1bad62914f49e9336", "bootable": "true", "encrypted": false, "replication_status": null, "consistencygroup_id": null, "multiattach": false, "attachments": [], "migration_status": null, "os-vol-tenant-attr:tenant_id": "bde05f7e96b244d598f3f1c0a44ea088", "os-vol-mig-status-attr:migstat": null, "os-vol-mig-status-attr:name_id": null, "volume_image_metadata": {"hw_rng_model": "virtio", "owner_specified.openstack.md5": "", "owner_specified.openstack.sha256": "", "owner_specified.openstack.object": "images/cirros-0.5.2-x86_64-disk", "image_id": "01130109-0a8b-4001-9ee7-dad4028951da", "image_name": "cirros-0.5.2-x86_64-disk", "checksum": "b874c39491a2377b8490f5f1e89761a4", "container_format": "bare", "disk_format": "qcow2", "min_disk": "0", "min_ram": "0", "size": "16300544"}, "os-vol-host-attr:host": "mridula-test@lvmdriver-1#lvmdriver-1"}}

