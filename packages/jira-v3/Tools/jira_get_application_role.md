---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/application-roles
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_application_role
title: "Jira v3 - Get application role"
kind: request
request: "[[Jira v3 - Get application role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/applicationrole/{key} · Get application role. Returns an application role. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "key":
    type: string
    required: true
    description: "The key of the application role. Use the Get all application roles operation to get the key for each application role."
writes: false
expose: false
---
# jira_get_application_role

`GET /rest/api/3/applicationrole/{key}` — Get application role

- Request: [[Jira v3 - Get application role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
