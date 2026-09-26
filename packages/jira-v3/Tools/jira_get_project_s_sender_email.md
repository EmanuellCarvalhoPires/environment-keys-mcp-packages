---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-email
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_s_sender_email
title: "Jira v3 - Get project's sender email"
kind: request
request: "[[Jira v3 - Get project's sender email]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectId}/email · Get project's sender email. Returns the project's sender email address. Permissions required: Browse projects project permission for the project. Writes data: no."
params:
  "projectId":
    type: string
    required: true
    description: "The project ID."
writes: false
expose: false
---
# jira_get_project_s_sender_email

`GET /rest/api/3/project/{projectId}/email` — Get project's sender email

- Request: [[Jira v3 - Get project's sender email]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
