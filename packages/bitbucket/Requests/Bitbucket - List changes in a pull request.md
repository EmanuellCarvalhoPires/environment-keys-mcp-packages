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
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_list_changes_in_a_pull_request]]"
---
# Bitbucket - List changes in a pull request

**List changes in a pull request** — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff`

- Run by the tool [[bitbucket_list_changes_in_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/diff
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.

## Original description

Redirects to the [repository diff](/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-diff-spec-get)
with the revspec that corresponds to the pull request.
