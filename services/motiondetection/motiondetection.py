#!/usr/bin/env python
import angus

conn = angus.connect()
service = conn.services.get_service('motion_detection', version=1)

service.enable_session()

for i in range(200):
    job = service.process({'image': open('./photo-%s.jpg' % (i))})
    print job.result

service.disable_session()
