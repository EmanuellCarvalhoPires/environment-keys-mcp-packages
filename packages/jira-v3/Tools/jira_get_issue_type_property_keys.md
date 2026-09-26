---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-properties
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_type_property_keys
title: "Jira v3 - Get issue type property keys"
kind: request
request: "[[Jira v3 - Get issue type property keys]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuetype/{issueTypeId}/properties · Get issue type property keys. Returns all the issue type property keys of the issue type. This operation can be accessed anonymously. Permissions required: Administer Jira global permission to get the property keys of any issue type. Writes data: no."
params:
  "issueTypeId":
    type: string
    required: true
    description: "The ID of the issue type."
writes: false
expose: false
---
# jira_get_issue_type_property_keys

`GET /rest/api/3/issuetype/{issueTypeId}/properties` — Get issue type property keys

- Request: [[Jira v3 - Get issue type property keys]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
