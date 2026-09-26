---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/list
  - api/effect/read
up: "[[MCP - Automation]]"
tool: automation_list_rule_summaries
title: "Automation - List rule summaries"
kind: request
request: "[[Automation - List rule summaries]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · GET /rest/v1/rule/summary · List rule summaries. Get rule summaries for all rules. Deprecated: The links field in the response body has recently changed to return just the query parameters instead of absolute links. See the changelog notice. Writes data: no."
params:
  "product":
    type: string
    required: true
    enum: ["jira", "confluence"]
    description: "Product where the rule runs: jira or confluence."
  "cursor":
    type: string
    required: false
    description: "The pagination cursor to use to fetch a page of results. The first call should be made without a cursor. Cursors are returned in the response body and should not be constructed manually."
  "limit":
    type: string
    required: false
    description: "Optional page size limit"
writes: false
expose: true
---
# automation_list_rule_summaries

`GET /rest/v1/rule/summary` — List rule summaries

- Request: [[Automation - List rule summaries]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
