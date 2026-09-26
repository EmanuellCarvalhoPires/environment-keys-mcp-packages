---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_type_scheme_items
title: "Jira v3 - Get issue type scheme items"
kind: request
request: "[[Jira v3 - Get issue type scheme items]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuetypescheme/mapping · Get issue type scheme items. Returns a paginated list of issue type scheme items. Only issue type scheme items used in classic projects are returned. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "issueTypeSchemeId":
    type: string
    required: false
    description: "The list of issue type scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, issueTypeSchemeId=10000&issueTypeSchemeId=10001."
writes: false
expose: false
---
# jira_get_issue_type_scheme_items

`GET /rest/api/3/issuetypescheme/mapping` — Get issue type scheme items

- Request: [[Jira v3 - Get issue type scheme items]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
