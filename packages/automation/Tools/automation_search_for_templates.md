---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/templates
  - api/operation/search
  - api/effect/read
up: "[[MCP - Automation]]"
tool: automation_search_for_templates
title: "Automation - Search for templates"
kind: request
request: "[[Automation - Search for templates]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · GET /rest/v1/template/search · Search for templates. Search for templates rules using the given query params. Accepts either a combination of filter parameters, or a cursor, but not both. Deprecated: The links field in the response body has recently changed to return just the query parameters instead of absolute links. Writes data: no."
params:
  "product":
    type: string
    required: true
    enum: ["jira", "confluence"]
    description: "Product where the rule runs: jira or confluence."
  "cursor":
    type: string
    required: false
    description: "The pagination cursor to use to fetch a page of results. Cursors are obtained via requests to the search API and should not be constructed manually."
  "limit":
    type: string
    required: false
    description: "Optional page size limit"
  "categories":
    type: string
    required: false
    description: "Optional categories filter parameter"
  "ruleHome":
    type: string
    required: false
    description: "If provided, only templates that apply to the ruleHome represented by the ARI will be returned. Used to limit results to templates applicable for a given project or product etc."
writes: false
expose: false
---
# automation_search_for_templates

`GET /rest/v1/template/search` — Search for templates

- Request: [[Automation - Search for templates]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
