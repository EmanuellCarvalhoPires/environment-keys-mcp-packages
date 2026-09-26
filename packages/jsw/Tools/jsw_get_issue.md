---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/issue
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_issue
title: "JSW - Get issue"
kind: request
request: "[[JSW - Get issue]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/issue/{issueIdOrKey} · Get issue. Returns a single issue, for a given issue ID or issue key. Issues returned from this resource include Agile fields, like sprint, closedSprints, flagged, and epic. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the requested issue."
  "fields":
    type: string
    required: false
    description: "The list of fields to return for each issue. By default, all navigable and Agile fields are returned."
  "expand":
    type: string
    required: false
    description: "A comma-separated list of the parameters to expand."
  "updateHistory":
    type: string
    required: false
    description: "A boolean indicating whether the issue retrieved by this method should be added to the current user's issue history"
writes: false
expose: false
---
# jsw_get_issue

`GET /rest/agile/1.0/issue/{issueIdOrKey}` — Get issue

- Request: [[JSW - Get issue]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
