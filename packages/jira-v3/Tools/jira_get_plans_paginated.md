---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/plans
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_plans_paginated
title: "Jira v3 - Get plans paginated"
kind: request
request: "[[Jira v3 - Get plans paginated]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/plans/plan · Get plans paginated. Returns a paginated list of plans. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "includeTrashed":
    type: string
    required: false
    description: "Whether to include trashed plans in the results."
  "includeArchived":
    type: string
    required: false
    description: "Whether to include archived plans in the results."
  "cursor":
    type: string
    required: false
    description: "The cursor to start from. If not provided, the first page will be returned."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of plans to return per page. The maximum value is 50. The default value is 50."
writes: false
expose: false
---
# jira_get_plans_paginated

`GET /rest/api/3/plans/plan` — Get plans paginated

- Request: [[Jira v3 - Get plans paginated]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
