---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issuetypescheme/{issueTypeSchemeId}"
category: "Issue type schemes"
writes_data: true
tool_note: "[[jira_delete_issue_type_scheme]]"
---
# Jira v3 - Delete issue type scheme

**Delete issue type scheme** — `DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}`

- Run by the tool [[jira_delete_issue_type_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issuetypescheme/{{param:issueTypeSchemeId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueTypeSchemeId` (path, string, required) — The ID of the issue type scheme.

## Original description

Deletes an issue type scheme.

Only issue type schemes used in classic projects can be deleted. Only issue type schemes not associated with a project can be deleted

A validation error will be returned if the specified scheme is associated with one or more projects. Use [Get issue type scheme API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-get) (with the projects expand, and id query parameter) to get a list of projects. Then, use [Assign issue type scheme to project API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-project-put) to associate all projects to another scheme before deleting.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
