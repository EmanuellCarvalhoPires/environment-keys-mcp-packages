---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/relation
  - api/operation/search
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_find_relationship_from_source_to_target
title: "Confluence v1 - Find relationship from source to target"
kind: request
request: "[[Confluence v1 - Find relationship from source to target]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}/{targetKey} · Find relationship from source to target. Find whether a particular type of relationship exists from a source entity to a target entity. Note, relationships are one way. For example, you can use this method to find whether the current user has selected a particular page as a favorite (i.e. Writes data: no."
params:
  "relationName":
    type: string
    required: true
    description: "The name of the relationship. This method supports the 'favourite' (i.e. 'save for later') relationship as well as any other relationship types created via Create relationship."
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
    description: "The identifier for the target entity: - If targetType is user, then specify either current (logged-in user), the user key of the user, or the account ID of the user."
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
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the response object to expand. - relationData returns information about the relationship, such as who created it and when it was created."
writes: false
expose: false
---
# confluence_v1_find_relationship_from_source_to_target

`GET /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}/{targetKey}` — Find relationship from source to target

- Request: [[Confluence v1 - Find relationship from source to target]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
