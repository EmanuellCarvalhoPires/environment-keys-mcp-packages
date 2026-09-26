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
path: "/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}"
category: "Issue type screen schemes"
writes_data: true
tool_note: "[[jira_update_issue_type_screen_scheme]]"
---
# Jira v3 - Update issue type screen scheme

**Update issue type screen scheme** — `PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}`

- Run by the tool [[jira_update_issue_type_screen_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuetypescreenscheme/{{param:issueTypeScreenSchemeId}}
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
  "description": "Screens for scrum issue types.",
  "name": "Scrum scheme"
}
```

## Original description

Updates an issue type screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
