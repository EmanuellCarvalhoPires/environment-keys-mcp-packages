---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/ui-modifications-apps
  - api/operation/delete
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/uiModifications/{uiModificationId}"
category: "UI modifications (apps)"
writes_data: true
---
# Jira v3 - Delete UI modification

**Delete UI modification** — `DELETE /rest/api/3/uiModifications/{uiModificationId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Delete UI modification"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/uiModifications/{{param:uiModificationId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `uiModificationId` (path, string, required) — The ID of the UI modification.

## Original description

Deletes a UI modification. All the contexts that belong to the UI modification are deleted too. UI modification can only be deleted by Forge apps.

**[Permissions](#permissions) required:** None.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
