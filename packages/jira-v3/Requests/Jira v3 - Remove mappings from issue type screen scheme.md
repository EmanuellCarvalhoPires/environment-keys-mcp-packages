---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-screen-schemes
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove"
category: "Issue type screen schemes"
writes_data: true
tool_note: "[[jira_remove_mappings_from_issue_type_screen_scheme]]"
---
# Jira v3 - Remove mappings from issue type screen scheme

**Remove mappings from issue type screen scheme** — `POST /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove`

- Run by the tool [[jira_remove_mappings_from_issue_type_screen_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issuetypescreenscheme/{{param:issueTypeScreenSchemeId}}/mapping/remove
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueTypeScreenSchemeId` (path, string, required) — The ID of the issue type screen scheme.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issueTypeIds": [
    "10000",
    "10001",
    "10004"
  ]
}
```

## Original description

Removes issue type to screen scheme mappings from an issue type screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
