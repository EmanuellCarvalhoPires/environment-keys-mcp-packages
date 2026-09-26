---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_remove_filter_as_favorite
title: "Jira v3 - Remove filter as favorite"
kind: request
request: "[[Jira v3 - Remove filter as favorite]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/filter/{id}/favourite · Remove filter as favorite. Removes a filter as a favorite for the user. Note that this operation only removes filters visible to the user from the user's favorites list. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list."
writes: true
expose: false
---
# jira_remove_filter_as_favorite

`DELETE /rest/api/3/filter/{id}/favourite` — Remove filter as favorite

- Request: [[Jira v3 - Remove filter as favorite]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
