---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_set_property
title: "JSM - Set property"
kind: request
request: "[[JSM - Set property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · PUT /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey} · Set property. Sets the value of an organization property. Use this resource to store custom data against an organization. Organization properties are a type of entity property which are available to the API only, and not shown in Jira Service Management. Learn more. Writes data: yes."
params:
  "organizationId":
    type: string
    required: true
    description: "The ID of the organization on which the property will be set."
  "propertyKey":
    type: string
    required: true
    description: "The key of the organization's property. The maximum length of the key is 255 bytes."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_set_property

`PUT /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}` — Set property

- Request: [[JSM - Set property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
