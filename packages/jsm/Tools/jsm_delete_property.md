---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_delete_property
title: "JSM - Delete property"
kind: request
request: "[[JSM - Delete property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · DELETE /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey} · Delete property. Removes an organization property. Organization properties are a type of entity property which are available to the API only, and not shown in Jira Service Management. Learn more. Writes data: yes."
params:
  "organizationId":
    type: string
    required: true
    description: "The ID of the organization from which the property will be removed."
  "propertyKey":
    type: string
    required: true
    description: "The key of the property to remove."
writes: true
expose: false
---
# jsm_delete_property

`DELETE /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}` — Delete property

- Request: [[JSM - Delete property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
