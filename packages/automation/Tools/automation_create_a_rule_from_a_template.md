---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/templates
  - api/operation/create
  - api/effect/write
up: "[[MCP - Automation]]"
tool: automation_create_a_rule_from_a_template
title: "Automation - Create a rule from a template"
kind: request
request: "[[Automation - Create a rule from a template]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · POST /rest/v1/template/create · Create a rule from a template. Create a rule from a template. This template may optionally accept parameters. Writes data: yes."
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
writes: true
expose: false
---
# automation_create_a_rule_from_a_template

`POST /rest/v1/template/create` — Create a rule from a template

- Request: [[Automation - Create a rule from a template]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
