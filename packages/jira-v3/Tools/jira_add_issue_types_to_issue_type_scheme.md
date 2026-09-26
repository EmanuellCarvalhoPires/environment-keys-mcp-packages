---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_add_issue_types_to_issue_type_scheme
title: "Jira v3 - Add issue types to issue type scheme"
kind: request
request: "[[Jira v3 - Add issue types to issue type scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype · Add issue types to issue type scheme. Adds issue types to an issue type scheme. The added issue types are appended to the issue types list. If any of the issue types exist in the issue type scheme, the operation fails and no issue types are added. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "issueTypeSchemeId":
    type: string
    required: true
    description: "The ID of the issue type scheme."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_add_issue_types_to_issue_type_scheme

`PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype` — Add issue types to issue type scheme

- Request: [[Jira v3 - Add issue types to issue type scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
