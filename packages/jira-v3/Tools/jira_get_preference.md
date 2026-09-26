---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/myself
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_preference
title: "Jira v3 - Get preference"
kind: request
request: "[[Jira v3 - Get preference]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/mypreferences · Get preference. Returns the value of a preference of the current user. Note that these keys are deprecated: jira.user.locale The locale of the user. By default this is not set and the user takes the locale of the instance. jira.user.timezone The time zone of the user. Writes data: no."
params:
  "key":
    type: string
    required: true
    description: "The key of the preference."
writes: false
expose: false
---
# jira_get_preference

`GET /rest/api/3/mypreferences` — Get preference

- Request: [[Jira v3 - Get preference]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
