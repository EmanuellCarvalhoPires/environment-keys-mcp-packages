---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_issue_type
title: "Jira v3 - Delete issue type"
kind: request
request: "[[Jira v3 - Delete issue type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issuetype/{id} · Delete issue type. Deletes the issue type. If the issue type is in use, all uses are updated with the alternative issue type (alternativeIssueTypeId). A list of alternative issue types are obtained from the Get alternative issue types resource. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue type."
  "alternativeIssueTypeId":
    type: string
    required: false
    description: "The ID of the replacement issue type."
writes: true
expose: false
---
# jira_delete_issue_type

`DELETE /rest/api/3/issuetype/{id}` — Delete issue type

- Request: [[Jira v3 - Delete issue type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
