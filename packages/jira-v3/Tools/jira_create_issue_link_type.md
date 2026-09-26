---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-link-types
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_issue_link_type
title: "Jira v3 - Create issue link type"
kind: request
request: "[[Jira v3 - Create issue link type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issueLinkType · Create issue link type. Creates an issue link type. Use this operation to create descriptions of the reasons why issues are linked. The issue link type consists of a name and descriptions for a link's inward and outward relationships. To use this operation, the site must have issue linking enabled. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_issue_link_type

`POST /rest/api/3/issueLinkType` — Create issue link type

- Request: [[Jira v3 - Create issue link type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
