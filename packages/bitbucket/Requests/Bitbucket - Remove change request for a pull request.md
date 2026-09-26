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
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes"
category: "Pullrequests"
writes_data: true
tool_note: "[[bitbucket_remove_change_request_for_a_pull_request]]"
---
# Bitbucket - Remove change request for a pull request

**Remove change request for a pull request** — `DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes`

- Run by the tool [[bitbucket_remove_change_request_for_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/request-changes
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.

