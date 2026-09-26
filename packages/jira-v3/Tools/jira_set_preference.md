---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/myself
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_set_preference
title: "Jira v3 - Set preference"
kind: request
request: "[[Jira v3 - Set preference]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/mypreferences · Set preference. Creates a preference for the user or updates a preference's value by sending a plain text string. For example, false. An arbitrary preference can be created with the value containing up to 255 characters. Writes data: yes."
params:
  "key":
    type: string
    required: true
    description: "The key of the preference. The maximum length is 255 characters."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_preference

`PUT /rest/api/3/mypreferences` — Set preference

- Request: [[Jira v3 - Set preference]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
