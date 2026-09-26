---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/templates
  - api/operation/search
  - api/effect/read
up: "[[MCP - Automation]]"
tool: automation_search_for_templates_post
title: "Automation - Search for templates (POST)"
kind: request
request: "[[Automation - Search for templates (POST)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · POST /rest/v1/template/search · Search for templates. Search for templates using the given criteria via POST. Currently categories and ruleHome ARI filters are supported. Deprecated: The links field in the response body has recently changed to return just the query parameters instead of absolute links. See the changelog notice. Writes data: no."
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
# automation_search_for_templates_post

`POST /rest/v1/template/search` — Search for templates

- Request: [[Automation - Search for templates (POST)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
