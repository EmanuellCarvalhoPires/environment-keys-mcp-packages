---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-email
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_set_project_s_sender_email
title: "Jira v3 - Set project's sender email"
kind: request
request: "[[Jira v3 - Set project's sender email]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/project/{projectId}/email · Set project's sender email. Sets the project's sender email address. If emailAddress is an empty string, the default email address is restored. Permissions required: Administer Jira global permission or Administer Projects project permission. Writes data: yes."
params:
  "projectId":
    type: string
    required: true
    description: "The project ID."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_project_s_sender_email

`PUT /rest/api/3/project/{projectId}/email` — Set project's sender email

- Request: [[Jira v3 - Set project's sender email]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
