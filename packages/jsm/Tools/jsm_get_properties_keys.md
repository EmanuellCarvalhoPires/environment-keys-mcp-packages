---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_properties_keys
title: "JSM - Get properties keys"
kind: request
request: "[[JSM - Get properties keys]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/organization/{organizationId}/property · Get properties keys. Returns the keys of all organization properties. Organization properties are a type of entity property which are available to the API only, and not shown in Jira Service Management. Learn more. Writes data: no."
params:
  "organizationId":
    type: string
    required: true
    description: "The ID of the organization from which keys will be returned."
writes: false
expose: false
---
# jsm_get_properties_keys

`GET /rest/servicedeskapi/organization/{organizationId}/property` — Get properties keys

- Request: [[JSM - Get properties keys]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
