---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_component_issues_count
title: "Jira v3 - Get component issues count"
kind: request
request: "[[Jira v3 - Get component issues count]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/component/{id}/relatedIssueCounts · Get component issues count. Returns the counts of issues assigned to the component. This operation can be accessed anonymously. Deprecation notice: The required OAuth 2.0 scopes will be updated on June 15, 2024. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the component."
writes: false
expose: false
---
# jira_get_component_issues_count

`GET /rest/api/3/component/{id}/relatedIssueCounts` — Get component issues count

- Request: [[Jira v3 - Get component issues count]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
