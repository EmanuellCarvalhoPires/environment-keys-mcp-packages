---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_organization
title: "JSM - Get organization"
kind: request
request: "[[JSM - Get organization]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/organization/{organizationId} · Get organization. This method returns details of an organization. Use this method to get organization details whenever your application component is passed an organization ID but needs to display other organization details. Writes data: no."
params:
  "organizationId":
    type: string
    required: true
    description: "The ID of the organization."
writes: false
expose: false
---
# jsm_get_organization

`GET /rest/servicedeskapi/organization/{organizationId}` — Get organization

- Request: [[JSM - Get organization]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
