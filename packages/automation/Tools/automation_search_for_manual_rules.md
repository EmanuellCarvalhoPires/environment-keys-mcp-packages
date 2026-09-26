---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/manual-rules
  - api/operation/search
  - api/effect/read
up: "[[MCP - Automation]]"
tool: automation_search_for_manual_rules
title: "Automation - Search for manual rules"
kind: request
request: "[[Automation - Search for manual rules]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · GET /rest/v1/rule/manual/search · Search for manual rules. Search for manually-triggered rules using the given query params. Note: Currently only cursor is allowed as parameter for the GET operation. Use the POST operation to perform the initial search. Writes data: no."
params:
  "product":
    type: string
    required: true
    enum: ["jira", "confluence"]
    description: "Product where the rule runs: jira or confluence."
  "cursor":
    type: string
    required: true
    description: "The pagination cursor to use to fetch a page of results. Cursors are obtained via requests to the search API and should not be constructed manually."
  "limit":
    type: string
    required: false
    description: "Optional page size limit"
writes: false
expose: false
---
# automation_search_for_manual_rules

`GET /rest/v1/rule/manual/search` — Search for manual rules

- Request: [[Automation - Search for manual rules]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
