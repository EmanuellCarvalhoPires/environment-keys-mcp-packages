---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/search
  - api/effect/read
up: "[[MCP - Automation]]"
tool: automation_search_for_rule_summaries
title: "Automation - Search for rule summaries"
kind: request
request: "[[Automation - Search for rule summaries]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · POST /rest/v1/rule/summary · Search for rule summaries. Get rule summaries for rules that match the given criteria via POST. Supports filtering by trigger, rule state, and rule scope (single ARI). Deprecated: The links field in the response body has recently changed to return just the query parameters instead of absolute links. Writes data: no."
params:
  "product":
    type: string
    required: true
    enum: ["jira", "confluence"]
    description: "Product where the rule runs: jira or confluence."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# automation_search_for_rule_summaries

`POST /rest/v1/rule/summary` — Search for rule summaries

- Request: [[Automation - Search for rule summaries]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
