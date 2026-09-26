---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-link-types
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_link_types
title: "Jira v3 - Get issue link types"
kind: request
request: "[[Jira v3 - Get issue link types]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issueLinkType · Get issue link types. Returns a list of all issue link types. To use this operation, the site must have issue linking enabled. This operation can be accessed anonymously. Permissions required: Browse projects project permission for a project in the site. Writes data: no."
writes: false
expose: false
---
# jira_get_issue_link_types

`GET /rest/api/3/issueLinkType` — Get issue link types

- Request: [[Jira v3 - Get issue link types]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
