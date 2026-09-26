---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}"
category: "Project versions"
writes_data: true
tool_note: "[[jira_delete_related_work]]"
---
# Jira v3 - Delete related work

**Delete related work** — `DELETE /rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}`

- Run by the tool [[jira_delete_related_work]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/version/{{param:versionId}}/relatedwork/{{param:relatedWorkId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `versionId` (path, string, required) — The ID of the version that the target related work belongs to.
- `relatedWorkId` (path, string, required) — The ID of the related work to delete.

## Original description

Deletes the given related work for the given version.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Resolve issues:* and *Edit issues* [Managing project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) for the project that contains the version.
