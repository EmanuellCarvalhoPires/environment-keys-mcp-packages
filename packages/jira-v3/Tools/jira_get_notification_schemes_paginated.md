---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_notification_schemes_paginated
title: "Jira v3 - Get notification schemes paginated"
kind: request
request: "[[Jira v3 - Get notification schemes paginated]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/notificationscheme · Get notification schemes paginated. Returns a paginated list of notification schemes ordered by the display name. Note that you should allow for events without recipients to appear in responses. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "id":
    type: string
    required: false
    description: "The list of notification schemes IDs to be filtered by"
  "projectId":
    type: string
    required: false
    description: "The list of projects IDs to be filtered by"
  "onlyDefault":
    type: string
    required: false
    description: "When set to true, returns only the default notification scheme. If you provide project IDs not associated with the default, returns an empty page. The default value is false."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list."
writes: false
expose: false
---
# jira_get_notification_schemes_paginated

`GET /rest/api/3/notificationscheme` — Get notification schemes paginated

- Request: [[Jira v3 - Get notification schemes paginated]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
