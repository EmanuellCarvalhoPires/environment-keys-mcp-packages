---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-link-types
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_link_type
title: "Jira v3 - Get issue link type"
kind: request
request: "[[Jira v3 - Get issue link type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issueLinkType/{issueLinkTypeId} · Get issue link type. Returns an issue link type. To use this operation, the site must have issue linking enabled. This operation can be accessed anonymously. Permissions required: Browse projects project permission for a project in the site. Writes data: no."
params:
  "issueLinkTypeId":
    type: string
    required: true
    description: "The ID of the issue link type."
writes: false
expose: false
---
# jira_get_issue_link_type

`GET /rest/api/3/issueLinkType/{issueLinkTypeId}` — Get issue link type

- Request: [[Jira v3 - Get issue link type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
