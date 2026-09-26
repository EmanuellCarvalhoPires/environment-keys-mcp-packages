---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-key-and-name-validation
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_valid_project_name
title: "Jira v3 - Get valid project name"
kind: request
request: "[[Jira v3 - Get valid project name]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/projectvalidate/validProjectName · Get valid project name. Checks that a project name isn't in use. If the name isn't in use, the passed string is returned. If the name is in use, this operation attempts to generate a valid project name based on the one supplied, usually by adding a sequence number. Writes data: no."
params:
  "name":
    type: string
    required: true
    description: "The project name."
writes: false
expose: false
---
# jira_get_valid_project_name

`GET /rest/api/3/projectvalidate/validProjectName` — Get valid project name

- Request: [[Jira v3 - Get valid project name]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
