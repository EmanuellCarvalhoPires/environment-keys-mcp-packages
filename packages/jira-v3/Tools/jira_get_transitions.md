---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_transitions
title: "Jira v3 - Get transitions"
kind: request
request: "[[Jira v3 - Get transitions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/transitions · Get transitions. Returns either all transitions or a transition that can be performed by the user on an issue, based on the issue's status. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about transitions in the response. This parameter accepts transitions.fields, which returns information about the fields in the transition screen for each…"
  "transitionId":
    type: string
    required: false
    description: "The ID of the transition."
  "skipRemoteOnlyCondition":
    type: string
    required: false
    description: "Whether transitions with the condition Hide From User Condition are included in the response."
  "includeUnavailableTransitions":
    type: string
    required: false
    description: "Whether details of transitions that fail a condition are included in the response"
  "sortByOpsBarAndStatus":
    type: string
    required: false
    description: "Whether the transitions are sorted by ops-bar sequence value first then category order (Todo, In Progress, Done) or only by ops-bar sequence value."
writes: false
expose: true
---
# jira_get_transitions

`GET /rest/api/3/issue/{issueIdOrKey}/transitions` — Get transitions

- Request: [[Jira v3 - Get transitions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
