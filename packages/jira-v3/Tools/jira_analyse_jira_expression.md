---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/jira-expressions
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_analyse_jira_expression
title: "Jira v3 - Analyse Jira expression"
kind: request
request: "[[Jira v3 - Analyse Jira expression]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/expression/analyse · Analyse Jira expression. Analyses and validates Jira expressions. As an experimental feature, this operation can also attempt to type-check the expressions. Learn more about Jira expressions in the documentation. Permissions required: None. Writes data: no."
params:
  "check":
    type: string
    required: false
    description: "The check to perform: syntax Each expression's syntax is checked to ensure the expression can be parsed. Also, syntactic limits are validated. For example, the expression's length. type EXPERIMENTAL."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_analyse_jira_expression

`POST /rest/api/3/expression/analyse` — Analyse Jira expression

- Request: [[Jira v3 - Analyse Jira expression]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
