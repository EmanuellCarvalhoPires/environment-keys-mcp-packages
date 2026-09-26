---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_changelogs_by_ids
title: "Jira v3 - Get changelogs by IDs"
kind: request
request: "[[Jira v3 - Get changelogs by IDs]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/{issueIdOrKey}/changelog/list · Get changelogs by IDs. Returns changelogs for an issue specified by a list of changelog IDs. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project that the issue is in. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_get_changelogs_by_ids

`POST /rest/api/3/issue/{issueIdOrKey}/changelog/list` — Get changelogs by IDs

- Request: [[Jira v3 - Get changelogs by IDs]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
