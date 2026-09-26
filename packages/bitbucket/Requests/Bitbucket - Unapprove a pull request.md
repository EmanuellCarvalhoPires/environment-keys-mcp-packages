---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve"
category: "Pullrequests"
writes_data: true
tool_note: "[[bitbucket_unapprove_a_pull_request]]"
---
# Bitbucket - Unapprove a pull request

**Unapprove a pull request** — `DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve`

- Run by the tool [[bitbucket_unapprove_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/approve
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.

## Original description

Redact the authenticated user's approval of the specified pull
request.
