---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-screen-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping"
category: "Issue type screen schemes"
writes_data: true
tool_note: "[[jira_append_mappings_to_issue_type_screen_scheme]]"
---
# Jira v3 - Append mappings to issue type screen scheme

**Append mappings to issue type screen scheme** — `PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping`

- Run by the tool [[jira_append_mappings_to_issue_type_screen_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuetypescreenscheme/{{param:issueTypeScreenSchemeId}}/mapping
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
  "issueTypeMappings": [
    {
      "issueTypeId": "10000",
      "screenSchemeId": "10001"
    },
    {
      "issueTypeId": "10001",
      "screenSchemeId": "10002"
    },
    {
      "issueTypeId": "10002",
      "screenSchemeId": "10002"
    }
  ]
}
```

## Original description

Appends issue type to screen scheme mappings to an issue type screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
