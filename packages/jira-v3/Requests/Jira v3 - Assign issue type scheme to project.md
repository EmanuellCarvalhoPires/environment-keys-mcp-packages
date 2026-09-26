---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issuetypescheme/project"
category: "Issue type schemes"
writes_data: true
tool_note: "[[jira_assign_issue_type_scheme_to_project]]"
---
# Jira v3 - Assign issue type scheme to project

**Assign issue type scheme to project** — `PUT /rest/api/3/issuetypescheme/project`

- Run by the tool [[jira_assign_issue_type_scheme_to_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuetypescheme/project
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issueTypeSchemeId": "10000",
  "projectId": "10000"
}
```

## Original description

Assigns an issue type scheme to a project.

If any issues in the project are assigned issue types not present in the new scheme, the operation will fail. To complete the assignment those issues must be updated to use issue types in the new scheme.

Issue type schemes can only be assigned to classic projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
