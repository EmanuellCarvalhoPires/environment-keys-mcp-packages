---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/application-roles
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_all_application_roles
title: "Jira v3 - Get all application roles"
kind: request
request: "[[Jira v3 - Get all application roles]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/applicationrole · Get all application roles. Returns all application roles. In Jira, application roles are managed using the Application access configuration page. Permissions required: Administer Jira global permission. Writes data: no."
writes: false
expose: false
---
# jira_get_all_application_roles

`GET /rest/api/3/applicationrole` — Get all application roles

- Request: [[Jira v3 - Get all application roles]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
