---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_property
title: "JSM - Get property"
kind: request
request: "[[JSM - Get property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey} · Get property. Returns the value of an organization property. Use this method to obtain the JSON content for an organization's property. Organization properties are a type of entity property which are available to the API only, and not shown in Jira Service Management. Learn more. Writes data: no."
params:
  "organizationId":
    type: string
    required: true
    description: "The ID of the organization from which the property will be returned."
  "propertyKey":
    type: string
    required: true
    description: "The key of the property to return."
writes: false
expose: false
---
# jsm_get_property

`GET /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}` — Get property

- Request: [[JSM - Get property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
