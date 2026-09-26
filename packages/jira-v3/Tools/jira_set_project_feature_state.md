---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-features
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_set_project_feature_state
title: "Jira v3 - Set project feature state"
kind: request
request: "[[Jira v3 - Set project feature state]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/project/{projectIdOrKey}/features/{featureKey} · Set project feature state. Sets the state of a project feature. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The ID or (case-sensitive) key of the project."
  "featureKey":
    type: string
    required: true
    description: "The key of the feature."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_project_feature_state

`PUT /rest/api/3/project/{projectIdOrKey}/features/{featureKey}` — Set project feature state

- Request: [[Jira v3 - Set project feature state]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
