---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/version/{id}/mergeto/{moveIssuesTo}"
category: "Project versions"
writes_data: true
tool_note: "[[jira_merge_versions]]"
---
# Jira v3 - Merge versions

**Merge versions** — `PUT /rest/api/3/version/{id}/mergeto/{moveIssuesTo}`

- Run by the tool [[jira_merge_versions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/version/{{param:id}}/mergeto/{{param:moveIssuesTo}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the version to delete.
- `moveIssuesTo` (path, string, required) — The ID of the version to merge into.

## Original description

Merges two project versions. The merge is completed by deleting the version specified in `id` and replacing any occurrences of its ID in `fixVersion` with the version ID specified in `moveIssuesTo`.

Consider using [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) instead. This resource supports swapping version values in `fixVersion`, `affectedVersion`, and custom fields.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.
