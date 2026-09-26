---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/relation
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_delete_relationship
title: "Confluence v1 - Delete relationship"
kind: request
request: "[[Confluence v1 - Delete relationship]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}/{targetKey} · Delete relationship. Deletes a relationship between two entities (user, space, content). Permissions required: Permission to access the Confluence site ('Can use' global permission). For favourite relationships, the current user can only delete their own favourite relationships. Writes data: yes."
params:
  "relationName":
    type: string
    required: true
    description: "The name of the relationship."
  "sourceType":
    type: string
    required: true
    description: "The source entity type of the relationship. This must be 'user', if the relationName is 'favourite'."
  "sourceKey":
    type: string
    required: true
    description: "- The identifier for the source entity: - If sourceType is user, then specify either current (logged-in user), the user key of the user, or the account ID of the user."
  "targetType":
    type: string
    required: true
    description: "The target entity type of the relationship. This must be 'space' or 'content', if the relationName is 'favourite'."
  "targetKey":
    type: string
    required: true
    description: "- The identifier for the target entity: - If targetType is user, then specify either current (logged-in user), the user key of the user, or the account ID of the user."
  "sourceStatus":
    type: string
    required: false
    description: "The status of the source. This parameter is only used when the sourceType is 'content'."
  "targetStatus":
    type: string
    required: false
    description: "The status of the target. This parameter is only used when the targetType is 'content'."
  "sourceVersion":
    type: string
    required: false
    description: "The version of the source. This parameter is only used when the sourceType is 'content' and the sourceStatus is 'historical'."
  "targetVersion":
    type: string
    required: false
    description: "The version of the target. This parameter is only used when the targetType is 'content' and the targetStatus is 'historical'."
writes: true
expose: false
---
# confluence_v1_delete_relationship

`DELETE /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}/{targetKey}` — Delete relationship

- Request: [[Confluence v1 - Delete relationship]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
