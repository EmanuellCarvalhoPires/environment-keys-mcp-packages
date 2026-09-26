---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-configuration-apps
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/app/field/context/configuration/list"
category: "Issue custom field configuration (apps)"
writes_data: false
---
# Jira v3 - Bulk get custom field configurations

**Bulk get custom field configurations** — `POST /rest/api/3/app/field/context/configuration/list`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Bulk get custom field configurations"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/app/field/context/configuration/list?id={{param:id}}&fieldContextId={{param:fieldContextId}}&issueId={{param:issueId}}&projectKeyOrId={{param:projectKeyOrId}}&issueTypeId={{param:issueTypeId}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (query, string, optional) — The list of configuration IDs. To include multiple configurations, separate IDs with an ampersand: id=10000&id=10001. Can't be provided with fieldContextId, issueId, projectKeyOrId, or issueTypeId.
- `fieldContextId` (query, string, optional) — The list of field context IDs. To include multiple field contexts, separate IDs with an ampersand: fieldContextId=10000&fieldContextId=10001.
- `issueId` (query, string, optional) — The ID of the issue to filter results by. If the issue doesn't exist, an empty list is returned. Can't be provided with projectKeyOrId, or issueTypeId.
- `projectKeyOrId` (query, string, optional) — The ID or key of the project to filter results by. Must be provided with issueTypeId. Can't be provided with issueId.
- `issueTypeId` (query, string, optional) — The ID of the issue type to filter results by. Must be provided with projectKeyOrId. Can't be provided with issueId.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "fieldIdsOrKeys": [
    "customfield_10035",
    "customfield_10036"
  ]
}
```

## Original description

Returns a [paginated](#pagination) list of configurations for list of custom fields of a [type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) created by a [Forge app](https://developer.atlassian.com/platform/forge/).

The result can be filtered by one of these criteria:

 *  `id`.
 *  `fieldContextId`.
 *  `issueId`.
 *  `projectKeyOrId` and `issueTypeId`.

Otherwise, all configurations for the provided list of custom fields are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that provided the custom field type.
