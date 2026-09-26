---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/permissions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_my_permissions
title: "Jira v3 - Get my permissions"
kind: request
request: "[[Jira v3 - Get my permissions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/mypermissions · Get my permissions. Returns a list of permissions indicating which permissions the user has. Details of the user's permissions can be obtained in a global, project, issue or comment context. Writes data: no."
params:
  "projectKey":
    type: string
    required: false
    description: "The key of project. Ignored if projectId is provided."
  "projectId":
    type: string
    required: false
    description: "The ID of project."
  "issueKey":
    type: string
    required: false
    description: "The key of the issue. Ignored if issueId is provided."
  "issueId":
    type: string
    required: false
    description: "The ID of the issue."
  "permissions":
    type: string
    required: false
    description: "A list of permission keys. (Required) This parameter accepts a comma-separated list. To get the list of available permissions, use Get all permissions."
  "projectUuid":
    type: string
    required: false
    description: "Query parameter projectUuid."
  "projectConfigurationUuid":
    type: string
    required: false
    description: "Query parameter projectConfigurationUuid."
  "commentId":
    type: string
    required: false
    description: "The ID of the comment."
writes: false
expose: false
---
# jira_get_my_permissions

`GET /rest/api/3/mypermissions` — Get my permissions

- Request: [[Jira v3 - Get my permissions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
