---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_the_user_s_default_workflow_editor
title: "Jira v3 - Get the user's default workflow editor"
kind: request
request: "[[Jira v3 - Get the user's default workflow editor]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflows/defaultEditor · Get the user's default workflow editor. Get the user's default workflow editor. This can be either the new editor or the legacy editor. Writes data: no."
writes: false
expose: false
---
# jira_get_the_user_s_default_workflow_editor

`GET /rest/api/3/workflows/defaultEditor` — Get the user's default workflow editor

- Request: [[Jira v3 - Get the user's default workflow editor]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
