---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-properties
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_type_property
title: "Jira v3 - Get issue type property"
kind: request
request: "[[Jira v3 - Get issue type property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey} · Get issue type property. Returns the key and value of the issue type property. This operation can be accessed anonymously. Permissions required: Administer Jira global permission to get the details of any issue type. Writes data: no."
params:
  "issueTypeId":
    type: string
    required: true
    description: "The ID of the issue type."
  "propertyKey":
    type: string
    required: true
    description: "The key of the property. Use Get issue type property keys to get a list of all issue type property keys."
writes: false
expose: false
---
# jira_get_issue_type_property

`GET /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}` — Get issue type property

- Request: [[Jira v3 - Get issue type property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
