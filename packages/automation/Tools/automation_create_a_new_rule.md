---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/create
  - api/effect/write
up: "[[MCP - Automation]]"
tool: automation_create_a_new_rule
title: "Automation - Create a new rule"
kind: request
request: "[[Automation - Create a new rule]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · POST /rest/v1/rule · Create a new rule. Create a new rule from the provided Rule Payload. If providing a UUID for your new rule, it must be unique and V7. The time-based nature of V7 will impact sorting and pagination of your rule. Accepts a rule payload, which has the same structure as the get a rule by UUID response. Writes data: yes."
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
# automation_create_a_new_rule

`POST /rest/v1/rule` — Create a new rule

- Request: [[Automation - Create a new rule]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
