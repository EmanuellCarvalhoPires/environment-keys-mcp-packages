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
path: "/rest/api/3/issuetypescreenscheme/project"
category: "Issue type screen schemes"
writes_data: true
tool_note: "[[jira_assign_issue_type_screen_scheme_to_project]]"
---
# Jira v3 - Assign issue type screen scheme to project

**Assign issue type screen scheme to project** — `PUT /rest/api/3/issuetypescreenscheme/project`

- Run by the tool [[jira_assign_issue_type_screen_scheme_to_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuetypescreenscheme/project
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issueTypeScreenSchemeId": "10001",
  "projectId": "10002"
}
```

## Original description

Assigns an issue type screen scheme to a project.

Issue type screen schemes can only be assigned to classic projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
