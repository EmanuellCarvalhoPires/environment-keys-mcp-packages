---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/myself
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_preference
title: "Jira v3 - Delete preference"
kind: request
request: "[[Jira v3 - Delete preference]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/mypreferences · Delete preference. Deletes a preference of the user, which restores the default value of system defined settings. Note that these keys are deprecated: jira.user.locale The locale of the user. By default, not set. The user takes the instance locale. jira.user.timezone The time zone of the user. Writes data: yes."
params:
  "key":
    type: string
    required: true
    description: "The key of the preference."
writes: true
expose: false
---
# jira_delete_preference

`DELETE /rest/api/3/mypreferences` — Delete preference

- Request: [[Jira v3 - Delete preference]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
