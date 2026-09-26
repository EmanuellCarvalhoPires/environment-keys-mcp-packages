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
tool: confluence_v1_find_target_entities_related_to_a_source_entity
title: "Confluence v1 - Find target entities related to a source entity"
kind: request
request: "[[Confluence v1 - Find target entities related to a source entity]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType} · Find target entities related to a source entity. Returns all target entities that have a particular relationship to the source entity. Note, relationships are one way. Writes data: no."
params:
  "relationName":
    type: string
    required: true
    description: "The name of the relationship. This method supports relationships created via Create relationship. Note, this method does not support 'like' or 'favourite' relationships."
  "sourceType":
    type: string
    required: true
    description: "The source entity type of the relationship."
  "sourceKey":
    type: string
    required: true
    description: "The identifier for the source entity: - If sourceType is user, then specify either current (logged-in user), the user key of the user, or the account ID of the user."
  "targetType":
    type: string
    required: true
    description: "The target entity type of the relationship."
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
  "start":
    type: string
    required: false
    description: "The starting index of the returned relationships."
  "limit":
    type: string
    required: false
    description: "The maximum number of relationships to return per page. Note, this may be restricted by fixed system limits."
writes: false
expose: false
---
# confluence_v1_find_target_entities_related_to_a_source_entity

`GET /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}` — Find target entities related to a source entity

- Request: [[Confluence v1 - Find target entities related to a source entity]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
