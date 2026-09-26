---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/update
  - api/effect/write
up: "[[MCP - Automation]]"
tool: automation_update_rule_scope
title: "Automation - Update rule scope"
kind: request
request: "[[Automation - Update rule scope]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · PUT /rest/v1/rule/{ruleUuid}/rule-scope · Update rule scope. Update the scope of a rule by UUID. Writes data: yes."
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
# automation_update_rule_scope

`PUT /rest/v1/rule/{ruleUuid}/rule-scope` — Update rule scope

- Request: [[Automation - Update rule scope]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
