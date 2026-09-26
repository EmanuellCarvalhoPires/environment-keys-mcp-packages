---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/workspaces/{workspace}/projects/{project_key}"
category: "Projects"
writes_data: true
tool_note: "[[bitbucket_delete_a_project_for_a_workspace]]"
---
# Bitbucket - Delete a project for a workspace

**Delete a project for a workspace** — `DELETE /workspaces/{workspace}/projects/{project_key}`

- Run by the tool [[bitbucket_delete_a_project_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}
Authorization: {{service.auth_token}}
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.

## Original description

Deletes this project. This is an irreversible operation.

You cannot delete a project that still contains repositories.
To delete the project, [delete](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-delete)
or transfer the repositories first.

Example:
```
$ curl -X DELETE https://api.bitbucket.org/2.0/workspaces/bbworkspace1/projects/PROJ
```
