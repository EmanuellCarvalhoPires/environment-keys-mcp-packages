---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_delete_organization
title: "JSM - Delete organization"
kind: request
request: "[[JSM - Delete organization]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · DELETE /rest/servicedeskapi/organization/{organizationId} · Delete organization. This method deletes an organization. Note that the organization is deleted regardless of other associations it may have. For example, associations with service desks. Permissions required: Jira administrator. Writes data: yes."
params:
  "organizationId":
    type: string
    required: true
    description: "The ID of the organization."
writes: true
expose: false
---
# jsm_delete_organization

`DELETE /rest/servicedeskapi/organization/{organizationId}` — Delete organization

- Request: [[JSM - Delete organization]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
