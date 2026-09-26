---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_merge_versions
title: "Jira v3 - Merge versions"
kind: request
request: "[[Jira v3 - Merge versions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/version/{id}/mergeto/{moveIssuesTo} · Merge versions. Merges two project versions. The merge is completed by deleting the version specified in id and replacing any occurrences of its ID in fixVersion with the version ID specified in moveIssuesTo. Consider using Delete and replace version instead. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the version to delete."
  "moveIssuesTo":
    type: string
    required: true
    description: "The ID of the version to merge into."
writes: true
expose: false
---
# jira_merge_versions

`PUT /rest/api/3/version/{id}/mergeto/{moveIssuesTo}` — Merge versions

- Request: [[Jira v3 - Merge versions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
