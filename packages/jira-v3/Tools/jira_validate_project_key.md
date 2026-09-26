---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-key-and-name-validation
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_validate_project_key
title: "Jira v3 - Validate project key"
kind: request
request: "[[Jira v3 - Validate project key]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/projectvalidate/key · Validate project key. Validates a project key by confirming the key is a valid string and not in use. Permissions required: None. Writes data: no."
params:
  "key":
    type: string
    required: false
    description: "The project key."
writes: false
expose: false
---
# jira_validate_project_key

`GET /rest/api/3/projectvalidate/key` — Validate project key

- Request: [[Jira v3 - Validate project key]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
