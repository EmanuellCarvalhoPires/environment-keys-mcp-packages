---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_add_organization
title: "JSM - Add organization"
kind: request
request: "[[JSM - Add organization]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization · Add organization. This method adds an organization to a service desk. If the organization ID is already associated with the service desk, no change is made and the resource returns a 204 success code. Permissions required: Service desk's agent. Writes data: yes."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk to which the organization will be added. This can alternatively be a project identifier."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_add_organization

`POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization` — Add organization

- Request: [[JSM - Add organization]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
