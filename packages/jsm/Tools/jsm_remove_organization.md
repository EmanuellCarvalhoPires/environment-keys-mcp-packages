---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_remove_organization
title: "JSM - Remove organization"
kind: request
request: "[[JSM - Remove organization]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization · Remove organization. This method removes an organization from a service desk. If the organization ID does not match an organization associated with the service desk, no change is made and the resource returns a 204 success code. Permissions required: Service desk's agent. Writes data: yes."
params:
  "serviceDeskId":
    type: string
    required: true
    description: "The ID of the service desk from which the organization will be removed. This can alternatively be a project identifier."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_remove_organization

`DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization` — Remove organization

- Request: [[JSM - Remove organization]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
