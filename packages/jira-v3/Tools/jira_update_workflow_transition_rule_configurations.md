---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-transition-rules
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_update_workflow_transition_rule_configurations
title: "Jira v3 - Update workflow transition rule configurations"
kind: request
request: "[[Jira v3 - Update workflow transition rule configurations]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/workflow/rule/config · Update workflow transition rule configurations. Updates configuration of workflow transition rules. The following rule types are supported: post functions conditions validators Only rules created by the calling Connect or Forge app can be updated. To assist with app migration, this operation can be used to: Disable a rule. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_workflow_transition_rule_configurations

`PUT /rest/api/3/workflow/rule/config` — Update workflow transition rule configurations

- Request: [[Jira v3 - Update workflow transition rule configurations]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
