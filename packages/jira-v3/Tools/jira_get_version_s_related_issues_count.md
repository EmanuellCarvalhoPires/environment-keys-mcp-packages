---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_version_s_related_issues_count
title: "Jira v3 - Get version's related issues count"
kind: request
request: "[[Jira v3 - Get version's related issues count]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/version/{id}/relatedIssueCounts · Get version's related issues count. Returns the following counts for a version: Number of issues where the fixVersion is set to the version. Number of issues where the affectedVersion is set to the version. Number of issues where a version custom field is set to the version. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the version."
writes: false
expose: false
---
# jira_get_version_s_related_issues_count

`GET /rest/api/3/version/{id}/relatedIssueCounts` — Get version's related issues count

- Request: [[Jira v3 - Get version's related issues count]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
