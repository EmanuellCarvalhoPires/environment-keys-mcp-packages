---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-values-apps
  - api/operation/action
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/app/field/value"
category: "Issue custom field values (apps)"
writes_data: true
---
# Jira v3 - Update custom fields

**Update custom fields** — `POST /rest/api/3/app/field/value`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Update custom fields"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/app/field/value?generateChangelog={{param:generateChangelog}}&generateAppEvents={{param:generateAppEvents}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `generateChangelog` (query, string, optional) — Whether to generate a changelog for this update.
- `generateAppEvents` (query, string, optional) — Whether to generate app events for this update. Suppresses Forge, Connect, OAuth 2.0, and admin-configured webhooks (registered via the Jira admin UI).
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "updates": [
    {
      "customField": "customfield_10010",
      "issueIds": [
        10010,
        10011
      ],
      "value": "new value"
    },
    {
      "customField": "customfield_10011",
      "issueIds": [
        10010
      ],
      "value": 1000
    }
  ]
}
```

## Original description

Updates the value of one or more custom fields on one or more issues. Combinations of custom field and issue should be unique within the request.

Apps can only perform this operation on [custom fields](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/) and [custom field types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) declared in their own manifests.

**[Permissions](#permissions) required:** Only the app that owns the custom field or custom field type can update its values with this operation.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
