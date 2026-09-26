---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-screen-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_append_mappings_to_issue_type_screen_scheme
title: "Jira v3 - Append mappings to issue type screen scheme"
kind: request
request: "[[Jira v3 - Append mappings to issue type screen scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping · Append mappings to issue type screen scheme. Appends issue type to screen scheme mappings to an issue type screen scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "issueTypeScreenSchemeId":
    type: string
    required: true
    description: "The ID of the issue type screen scheme."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_append_mappings_to_issue_type_screen_scheme

`PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping` — Append mappings to issue type screen scheme

- Request: [[Jira v3 - Append mappings to issue type screen scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
