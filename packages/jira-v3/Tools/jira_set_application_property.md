---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/jira-settings
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_set_application_property
title: "Jira v3 - Set application property"
kind: request
request: "[[Jira v3 - Set application property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/application-properties/{id} · Set application property. Changes the value of an application property. For example, you can change the value of the jira.clone.prefix from its default value of CLONE - to Clone - if you prefer sentence case capitalization. Editable properties are described below along with their default values. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The key of the application property to update."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_application_property

`PUT /rest/api/3/application-properties/{id}` — Set application property

- Request: [[Jira v3 - Set application property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
