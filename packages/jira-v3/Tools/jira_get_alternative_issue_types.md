---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_alternative_issue_types
title: "Jira v3 - Get alternative issue types"
kind: request
request: "[[Jira v3 - Get alternative issue types]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuetype/{id}/alternatives · Get alternative issue types. Returns a list of issue types that can be used to replace the issue type. The alternative issue types are those assigned to the same workflow scheme, field configuration scheme, and screen scheme. This operation can be accessed anonymously. Permissions required: None. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue type."
writes: false
expose: false
---
# jira_get_alternative_issue_types

`GET /rest/api/3/issuetype/{id}/alternatives` — Get alternative issue types

- Request: [[Jira v3 - Get alternative issue types]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
