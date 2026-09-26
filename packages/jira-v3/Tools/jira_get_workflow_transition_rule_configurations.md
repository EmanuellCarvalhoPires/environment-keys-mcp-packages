---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-transition-rules
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_workflow_transition_rule_configurations
title: "Jira v3 - Get workflow transition rule configurations (GET)"
kind: request
request: "[[Jira v3 - Get workflow transition rule configurations (GET)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflow/rule/config · Get workflow transition rule configurations. Returns a paginated list of workflows with transition rules. The workflows can be filtered to return only those containing workflow transition rules: of one or more transition rule types, such as workflow post functions. matching one or more transition rule keys. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "types":
    type: string
    required: true
    description: "The types of the transition rules to return."
  "keys":
    type: string
    required: false
    description: "The transition rule class keys, as defined in the Connect or the Forge app descriptor, of the transition rules to return."
  "workflowNames":
    type: string
    required: false
    description: "The list of workflow names to filter by."
  "withTags":
    type: string
    required: false
    description: "The list of tags to filter by."
  "draft":
    type: string
    required: false
    description: "Deprecated: Whether draft or published workflows are returned. If not provided, both workflow types are returned. The 'draft' parameter will be removed from this API on November 2, 2026."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts transition, which, for each rule, returns information about the transition the rule is assigned to."
writes: false
expose: false
---
# jira_get_workflow_transition_rule_configurations

`GET /rest/api/3/workflow/rule/config` — Get workflow transition rule configurations

- Request: [[Jira v3 - Get workflow transition rule configurations (GET)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
