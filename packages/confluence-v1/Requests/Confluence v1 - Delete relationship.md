---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/relation
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}/{targetKey}"
category: "Relation"
writes_data: true
tool_note: "[[confluence_v1_delete_relationship]]"
---
# Confluence v1 - Delete relationship

**Delete relationship** — `DELETE /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}/{targetKey}`

- Run by the tool [[confluence_v1_delete_relationship]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/relation/{{param:relationName}}/from/{{param:sourceType}}/{{param:sourceKey}}/to/{{param:targetType}}/{{param:targetKey}}?sourceStatus={{param:sourceStatus}}&targetStatus={{param:targetStatus}}&sourceVersion={{param:sourceVersion}}&targetVersion={{param:targetVersion}}
Authorization: {{service.auth_token}}
```

## Parameters

- `relationName` (path, string, required) — The name of the relationship.
- `sourceType` (path, string, required) — The source entity type of the relationship. This must be 'user', if the relationName is 'favourite'.
- `sourceKey` (path, string, required) — - The identifier for the source entity: - If sourceType is user, then specify either current (logged-in user), the user key of the user, or the account ID of the user.
- `targetType` (path, string, required) — The target entity type of the relationship. This must be 'space' or 'content', if the relationName is 'favourite'.
- `targetKey` (path, string, required) — - The identifier for the target entity: - If targetType is user, then specify either current (logged-in user), the user key of the user, or the account ID of the user.
- `sourceStatus` (query, string, optional) — The status of the source. This parameter is only used when the sourceType is 'content'.
- `targetStatus` (query, string, optional) — The status of the target. This parameter is only used when the targetType is 'content'.
- `sourceVersion` (query, string, optional) — The version of the source. This parameter is only used when the sourceType is 'content' and the sourceStatus is 'historical'.
- `targetVersion` (query, string, optional) — The version of the target. This parameter is only used when the targetType is 'content' and the targetStatus is 'historical'.

## Original description

Deletes a relationship between two entities (user, space, content).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
For favourite relationships, the current user can only delete their own
favourite relationships. A space administrator can delete favourite
relationships for any user.
