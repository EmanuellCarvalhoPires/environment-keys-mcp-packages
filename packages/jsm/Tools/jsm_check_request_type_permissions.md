---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/search
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_check_request_type_permissions
title: "JSM - Check request type permissions"
kind: request
request: "[[JSM - Check request type permissions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/permissions/check · Check request type permissions. Returns: a list of request type IDs where the given user has permission to administer. a list of request type IDs where the given user has permission to submit the request. If no account ID is provided, the operation returns details for the logged in user. Writes data: no."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "Value of serviceDeskId in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jsm_check_request_type_permissions

`POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/permissions/check` — Check request type permissions

- Request: [[JSM - Check request type permissions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
