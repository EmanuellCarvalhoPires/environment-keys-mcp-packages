---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/update
  - api/effect/write
up: "[[MCP - Automation]]"
tool: automation_update_an_existing_rule
title: "Automation - Update an existing rule"
kind: request
request: "[[Automation - Update an existing rule]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · PUT /rest/v1/rule/{ruleUuid} · Update an existing rule. Updates an existing rule by accepting a rule payload, which has the same structure as the get a rule by UUID response. ComponentIds are only required for pre-existing components. New components will be created or deleted as needed. Writes data: yes."
params:
  "ruleUuid":
    type: string
    required: true
    description: "The UUID of the rule to update"
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
# automation_update_an_existing_rule

`PUT /rest/v1/rule/{ruleUuid}` — Update an existing rule

- Request: [[Automation - Update an existing rule]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
