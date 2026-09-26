---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_edit_issue_metadata
title: "Jira v3 - Get edit issue metadata"
kind: request
request: "[[Jira v3 - Get edit issue metadata]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/editmeta · Get edit issue metadata. Returns the edit screen fields for an issue that are visible to and editable by the user. Use the information to populate the requests in Edit issue. This endpoint will check for these conditions: 1. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "overrideScreenSecurity":
    type: string
    required: false
    description: "Whether hidden fields are returned. Available to Connect and Forge app users with Administer Jira global permission and Forge apps acting on behalf of users with Administer Jira global permission."
  "overrideEditableFlag":
    type: string
    required: false
    description: "Whether non-editable fields are returned. Available to Connect and Forge app users with Administer Jira global permission and Forge apps acting on behalf of users with Administer Jira global permissio…"
writes: false
expose: false
---
# jira_get_edit_issue_metadata

`GET /rest/api/3/issue/{issueIdOrKey}/editmeta` — Get edit issue metadata

- Request: [[Jira v3 - Get edit issue metadata]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
