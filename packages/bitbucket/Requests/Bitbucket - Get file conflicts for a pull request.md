---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/conflicts"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_get_file_conflicts_for_a_pull_request]]"
---
# Bitbucket - Get file conflicts for a pull request

**Get file conflicts for a pull request** — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/conflicts`

- Run by the tool [[bitbucket_get_file_conflicts_for_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/conflicts
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.

## Original description

Redirects to the [repository file conflicts](/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-file-conflicts-spec-get)
with the revspec that corresponds to the pull request.
