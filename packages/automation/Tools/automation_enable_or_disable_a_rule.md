---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/update
  - api/effect/write
up: "[[MCP - Automation]]"
tool: automation_enable_or_disable_a_rule
title: "Automation - Enable or disable a rule"
kind: request
request: "[[Automation - Enable or disable a rule]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · PUT /rest/v1/rule/{ruleUuid}/state · Enable or disable a rule. Enable or disable a rule by rule UUID. Writes data: yes."
params:
  "ruleUuid":
    type: string
    required: true
    description: "Value of ruleUuid in the path."
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
# automation_enable_or_disable_a_rule

`PUT /rest/v1/rule/{ruleUuid}/state` — Enable or disable a rule

- Request: [[Automation - Enable or disable a rule]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
