---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_worklog
title: "Jira v3 - Get worklog"
kind: request
request: "[[Jira v3 - Get worklog]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/worklog/{id} · Get worklog. Returns a worklog. Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see Configuring time tracking. This operation can be accessed anonymously. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "id":
    type: string
    required: true
    description: "The ID of the worklog."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about work logs in the response. This parameter accepts properties, which returns worklog properties."
writes: false
expose: false
---
# jira_get_worklog

`GET /rest/api/3/issue/{issueIdOrKey}/worklog/{id}` — Get worklog

- Request: [[Jira v3 - Get worklog]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
