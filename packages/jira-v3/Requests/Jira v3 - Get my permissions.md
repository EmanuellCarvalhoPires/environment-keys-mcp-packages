---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/permissions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/mypermissions"
category: "Permissions"
writes_data: false
tool_note: "[[jira_get_my_permissions]]"
---
# Jira v3 - Get my permissions

**Get my permissions** — `GET /rest/api/3/mypermissions`

- Run by the tool [[jira_get_my_permissions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/mypermissions?projectKey={{param:projectKey}}&projectId={{param:projectId}}&issueKey={{param:issueKey}}&issueId={{param:issueId}}&permissions={{param:permissions}}&projectUuid={{param:projectUuid}}&projectConfigurationUuid={{param:projectConfigurationUuid}}&commentId={{param:commentId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectKey` (query, string, optional) — The key of project. Ignored if projectId is provided.
- `projectId` (query, string, optional) — The ID of project.
- `issueKey` (query, string, optional) — The key of the issue. Ignored if issueId is provided.
- `issueId` (query, string, optional) — The ID of the issue.
- `permissions` (query, string, optional) — A list of permission keys. (Required) This parameter accepts a comma-separated list. To get the list of available permissions, use Get all permissions.
- `projectUuid` (query, string, optional) — Query parameter projectUuid.
- `projectConfigurationUuid` (query, string, optional) — Query parameter projectConfigurationUuid.
- `commentId` (query, string, optional) — The ID of the comment.

## Original description

Returns a list of permissions indicating which permissions the user has. Details of the user's permissions can be obtained in a global, project, issue or comment context.

The user is reported as having a project permission:

 *  in the global context, if the user has the project permission in any project.
 *  for a project, where the project permission is determined using issue data, if the user meets the permission's criteria for any issue in the project. Otherwise, if the user has the project permission in the project.
 *  for an issue, where a project permission is determined using issue data, if the user has the permission in the issue. Otherwise, if the user has the project permission in the project containing the issue.
 *  for a comment, where the user has both the permission to browse the comment and the project permission for the comment's parent issue. Only the BROWSE\_PROJECTS permission is supported. If a `commentId` is provided whose `permissions` does not equal BROWSE\_PROJECTS, a 400 error will be returned.

This means that users may be shown as having an issue permission (such as EDIT\_ISSUES) in the global context or a project context but may not have the permission for any or all issues. For example, if Reporters have the EDIT\_ISSUES permission a user would be shown as having this permission in the global context or the context of a project, because any user can be a reporter. However, if they are not the user who reported the issue queried they would not have EDIT\_ISSUES permission for that issue.

For [Jira Service Management project permissions](https://support.atlassian.com/jira-cloud-administration/docs/customize-jira-service-management-permissions/), this will be evaluated similarly to a user in the customer portal. For example, if the BROWSE\_PROJECTS permission is granted to Service Project Customer - Portal Access, any users with access to the customer portal will have the BROWSE\_PROJECTS permission.

Global permissions are unaffected by context.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
