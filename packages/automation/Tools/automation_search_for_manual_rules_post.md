---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/manual-rules
  - api/operation/search
  - api/effect/read
up: "[[MCP - Automation]]"
tool: automation_search_for_manual_rules_post
title: "Automation - Search for manual rules (POST)"
kind: request
request: "[[Automation - Search for manual rules (POST)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · POST /rest/v1/rule/manual/search · Search for manual rules. Search for manually-triggered rules using the given criteria via POST. Currently only issue and alert objects are supported. Deprecated: The links field in the response body has recently changed to return just the query parameters instead of absolute links. Writes data: no."
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
expose: true
---
# automation_search_for_manual_rules_post

`POST /rest/v1/rule/manual/search` — Search for manual rules

- Request: [[Automation - Search for manual rules (POST)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
