---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_add_filter_as_favorite
title: "Jira v3 - Add filter as favorite"
kind: request
request: "[[Jira v3 - Add filter as favorite]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/filter/{id}/favourite · Add filter as favorite. Add a filter as a favorite for the user. Permissions required: Permission to access Jira, however, the user can only favorite: filters owned by the user. filters shared with a group that the user is a member of. Writes data: yes."
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
# jira_add_filter_as_favorite

`PUT /rest/api/3/filter/{id}/favourite` — Add filter as favorite

- Request: [[Jira v3 - Add filter as favorite]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
