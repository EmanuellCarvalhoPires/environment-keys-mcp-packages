---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_edit_issue
title: "Jira v3 - Edit issue"
kind: request
request: "[[Jira v3 - Edit issue]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issue/{issueIdOrKey} · Edit issue. Edits an issue. Issue properties may be updated as part of the edit. Please note that issue transition is not supported and is ignored here. To transition an issue, please use Transition issue. The edits to the issue's fields are defined using update and fields. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "notifyUsers":
    type: string
    required: false
    description: "Whether a notification email about the issue update is sent to all watchers. To disable the notification, administer Jira or administer project permissions are required."
  "overrideScreenSecurity":
    type: string
    required: false
    description: "Whether screen security is overridden to enable hidden fields to be edited. Available to Connect and Forge app users with Administer Jira global permission and Forge apps acting on behalf of users wit…"
  "overrideEditableFlag":
    type: string
    required: false
    description: "Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect and Forge app users with Administer Jira global permission and Forge apps acting on behalf of users…"
  "returnIssue":
    type: string
    required: false
    description: "Whether the response should contain the issue with fields edited in this request. The returned issue will have the same format as in the Get issue API."
  "expand":
    type: string
    required: false
    description: "The Get issue API expand parameter to use in the response if the returnIssue parameter is true."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: true
---
# jira_edit_issue

`PUT /rest/api/3/issue/{issueIdOrKey}` — Edit issue

- Request: [[Jira v3 - Edit issue]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
