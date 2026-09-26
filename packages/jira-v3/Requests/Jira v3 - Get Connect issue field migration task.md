---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/migration-of-connect-modules-to-forge
  - api/operation/list
  - api/effect/read
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task"
category: "Migration of Connect modules to Forge"
writes_data: false
---
# Jira v3 - Get Connect issue field migration task

**Get Connect issue field migration task** — `GET /rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Get Connect issue field migration task"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/atlassian-connect/1/migration/{{param:connectKey}}/{{param:jiraIssueFieldsKey}}/task
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `connectKey` (path, string, required) — The key of the Connect app that contains the Jira issue field being migrated.
- `jiraIssueFieldsKey` (path, string, required) — The module key of the Connect issue field being migrated.

## Original description

Returns the details of a Connect issue field's migration to Forge.

When migrating a Connect app to Forge, [Issue Field](https://developer.atlassian.com/cloud/jira/software/modules/issue-field/) modules
must be converted to [Custom field](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/). When the
Forge version of the app is installed, Forge creates a
[background task](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-group-tasks) to track the
migration of field data across. This endpoint returns the status and other details of that background task.

For more details, see
[Jira modules > Jira Custom Fields](https://developer.atlassian.com/platform/adopting-forge-from-connect/migrate-jira-custom-fields/).

**[Permissions](#permissions) required:** Only Connect and Forge apps can make this request.
