---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/app-data-policies
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_data_policy_for_projects
title: "Jira v3 - Get data policy for projects"
kind: request
request: "[[Jira v3 - Get data policy for projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/data-policy/project · Get data policy for projects. Returns data policies for the projects specified in the request. Writes data: no."
params:
  "ids":
    type: string
    required: false
    description: "A list of project identifiers. This parameter accepts a comma-separated list."
writes: false
expose: false
---
# jira_get_data_policy_for_projects

`GET /rest/api/3/data-policy/project` — Get data policy for projects

- Request: [[Jira v3 - Get data policy for projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
