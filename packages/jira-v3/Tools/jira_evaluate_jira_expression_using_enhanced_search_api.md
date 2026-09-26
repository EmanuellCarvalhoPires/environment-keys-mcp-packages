---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/jira-expressions
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_evaluate_jira_expression_using_enhanced_search_api
title: "Jira v3 - Evaluate Jira expression using enhanced search API"
kind: request
request: "[[Jira v3 - Evaluate Jira expression using enhanced search API]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/expression/evaluate · Evaluate Jira expression using enhanced search API. Evaluates a Jira expression and returns its value. The difference between this and eval is that this endpoint uses the enhanced search API when evaluating JQL queries. This API is eventually consistent, unlike the strongly consistent eval API. Writes data: no."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts meta.complexity that returns information about the expression complexity."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_evaluate_jira_expression_using_enhanced_search_api

`POST /rest/api/3/expression/evaluate` — Evaluate Jira expression using enhanced search API

- Request: [[Jira v3 - Evaluate Jira expression using enhanced search API]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
