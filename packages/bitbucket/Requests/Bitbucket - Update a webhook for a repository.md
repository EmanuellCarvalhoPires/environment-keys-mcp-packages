---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/hooks/{uid}"
category: "Repositories"
writes_data: true
tool_note: "[[bitbucket_update_a_webhook_for_a_repository]]"
---
# Bitbucket - Update a webhook for a repository

**Update a webhook for a repository** — `PUT /repositories/{workspace}/{repo_slug}/hooks/{uid}`

- Run by the tool [[bitbucket_update_a_webhook_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/hooks/{{param:uid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `uid` (path, string, required) — Value of uid in the path.

## Original description

Updates the specified webhook subscription.

The following properties can be mutated:

* `description`
* `url`
* `secret`
* `active`
* `events`

The hook's secret is used as a key to generate the HMAC hex digest sent in the
`X-Hub-Signature` header at delivery time. This signature is only generated
when the hook has a secret.

Set the hook's secret by passing the new value in the `secret` field. Passing a
`null` value in the `secret` field will remove the secret from the hook. The
hook's secret can be left unchanged by not passing the `secret` field in the
request.
