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
path: "/wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}/{targetKey}"
category: "Relation"
writes_data: false
tool_note: "[[confluence_v1_find_relationship_from_source_to_target]]"
---
# Confluence v1 - Find relationship from source to target

**Find relationship from source to target** — `GET /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}/{targetKey}`

- Run by the tool [[confluence_v1_find_relationship_from_source_to_target]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/relation/{{param:relationName}}/from/{{param:sourceType}}/{{param:sourceKey}}/to/{{param:targetType}}/{{param:targetKey}}?sourceStatus={{param:sourceStatus}}&targetStatus={{param:targetStatus}}&sourceVersion={{param:sourceVersion}}&targetVersion={{param:targetVersion}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `relationName` (path, string, required) — The name of the relationship. This method supports the 'favourite' (i.e. 'save for later') relationship as well as any other relationship types created via Create relationship.
- `sourceType` (path, string, required) — The source entity type of the relationship. This must be 'user', if the relationName is 'favourite'.
- `sourceKey` (path, string, required) — - The identifier for the source entity: - If sourceType is user, then specify either current (logged-in user), the user key of the user, or the account ID of the user.
- `targetType` (path, string, required) — The target entity type of the relationship. This must be 'space' or 'content', if the relationName is 'favourite'.
- `targetKey` (path, string, required) — The identifier for the target entity: - If targetType is user, then specify either current (logged-in user), the user key of the user, or the account ID of the user.
- `sourceStatus` (query, string, optional) — The status of the source. This parameter is only used when the sourceType is 'content'.
- `targetStatus` (query, string, optional) — The status of the target. This parameter is only used when the targetType is 'content'.
- `sourceVersion` (query, string, optional) — The version of the source. This parameter is only used when the sourceType is 'content' and the sourceStatus is 'historical'.
- `targetVersion` (query, string, optional) — The version of the target. This parameter is only used when the targetType is 'content' and the targetStatus is 'historical'.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the response object to expand. - relationData returns information about the relationship, such as who created it and when it was created.

## Original description

Find whether a particular type of relationship exists from a source
entity to a target entity. Note, relationships are one way.

For example, you can use this method to find whether the current user has
selected a particular page as a favorite (i.e. 'save for later'):
`GET /wiki/rest/api/relation/favourite/from/user/current/to/content/123`

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view both the target entity and source entity.
