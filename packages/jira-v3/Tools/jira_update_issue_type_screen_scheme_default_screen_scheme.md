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
tool: jira_update_issue_type_screen_scheme_default_screen_scheme
title: "Jira v3 - Update issue type screen scheme default screen scheme"
kind: request
request: "[[Jira v3 - Update issue type screen scheme default screen scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default · Update issue type screen scheme default screen scheme. Updates the default screen scheme of an issue type screen scheme. The default screen scheme is used for all unmapped issue types. Permissions required: Administer Jira global permission. Writes data: yes."
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
# jira_update_issue_type_screen_scheme_default_screen_scheme

`PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default` — Update issue type screen scheme default screen scheme

- Request: [[Jira v3 - Update issue type screen scheme default screen scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
