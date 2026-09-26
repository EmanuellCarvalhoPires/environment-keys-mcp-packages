---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/relation
  - api/operation/search
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/relation/{relationName}/to/{targetType}/{targetKey}/from/{sourceType}"
category: "Relation"
writes_data: false
tool_note: "[[confluence_v1_find_source_entities_related_to_a_target_entity]]"
---
# Confluence v1 - Find source entities related to a target entity

**Find source entities related to a target entity** — `GET /wiki/rest/api/relation/{relationName}/to/{targetType}/{targetKey}/from/{sourceType}`

- Run by the tool [[confluence_v1_find_source_entities_related_to_a_target_entity]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/relation/{{param:relationName}}/to/{{param:targetType}}/{{param:targetKey}}/from/{{param:sourceType}}?sourceStatus={{param:sourceStatus}}&targetStatus={{param:targetStatus}}&sourceVersion={{param:sourceVersion}}&targetVersion={{param:targetVersion}}&expand={{param:expand}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `relationName` (path, string, required) — The name of the relationship. This method supports relationships created via Create relationship. Note, this method does not support 'like' or 'favourite' relationships.
- `targetType` (path, string, required) — The target entity type of the relationship.
- `targetKey` (path, string, required) — The identifier for the target entity: - If targetType is user, then specify either current (logged-in user), the user key of the user, or the account ID of the user.
- `sourceType` (path, string, required) — The source entity type of the relationship.
- `sourceStatus` (query, string, optional) — The status of the source. This parameter is only used when the sourceType is 'content'.
- `targetStatus` (query, string, optional) — The status of the target. This parameter is only used when the targetType is 'content'.
- `sourceVersion` (query, string, optional) — The version of the source. This parameter is only used when the sourceType is 'content' and the sourceStatus is 'historical'.
- `targetVersion` (query, string, optional) — The version of the target. This parameter is only used when the targetType is 'content' and the targetStatus is 'historical'.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the response object to expand. - relationData returns information about the relationship, such as who created it and when it was created.
- `start` (query, string, optional) — The starting index of the returned relationships.
- `limit` (query, string, optional) — The maximum number of relationships to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns all target entities that have a particular relationship to the
source entity. Note, relationships are one way.

For example, the following method finds all users that have a 'collaborator'
relationship to a piece of content with an ID of '1234':
`GET /wiki/rest/api/relation/collaborator/to/content/1234/from/user`
Note, 'collaborator' is an example custom relationship type.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view both the target entity and source entity.
