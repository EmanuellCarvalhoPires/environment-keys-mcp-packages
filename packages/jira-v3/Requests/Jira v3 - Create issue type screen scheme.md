---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-screen-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issuetypescreenscheme"
category: "Issue type screen schemes"
writes_data: true
tool_note: "[[jira_create_issue_type_screen_scheme]]"
---
# Jira v3 - Create issue type screen scheme

**Create issue type screen scheme** — `POST /rest/api/3/issuetypescreenscheme`

- Run by the tool [[jira_create_issue_type_screen_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issuetypescreenscheme
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issueTypeMappings": [
    {
      "issueTypeId": "default",
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
  ],
  "name": "Scrum issue type screen scheme"
}
```

## Original description

Creates an issue type screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
