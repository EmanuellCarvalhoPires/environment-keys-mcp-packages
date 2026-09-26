---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_create_organization
title: "JSM - Create organization"
kind: request
request: "[[JSM - Create organization]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/organization · Create organization. This method creates an organization by passing the name of the organization. Permissions required: Service desk administrator or agent. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_create_organization

`POST /rest/servicedeskapi/organization` — Create organization

- Request: [[JSM - Create organization]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
