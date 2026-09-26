---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/hooks"
category: "Repositories"
writes_data: true
tool_note: "[[bitbucket_create_a_webhook_for_a_repository]]"
---
# Bitbucket - Create a webhook for a repository

**Create a webhook for a repository** — `POST /repositories/{workspace}/{repo_slug}/hooks`

- Run by the tool [[bitbucket_create_a_webhook_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/hooks
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Creates a new webhook on the specified repository.

Example:

```
$ curl -X POST -u credentials -H 'Content-Type: application/json'
  https://api.bitbucket.org/2.0/repositories/my-workspace/my-repo-slug/hooks
  -d '
    {
      "description": "Webhook Description",
      "url": "https://example.com/",
      "active": true,
      "secret": "this is a really bad secret",
      "events": [
        "repo:push",
        "issue:created",
        "issue:updated"
      ]
    }'
```

When the `secret` is provided it will be used as the key to generate a HMAC
digest value sent in the `X-Hub-Signature` header at delivery time. Passing
a `null` or empty `secret` or not passing a `secret` will leave the webhook's
secret unset. Bitbucket only generates the `X-Hub-Signature` when the webhook's
secret is set.

Note that this call requires the webhook scope, as well as any scope
that applies to the events that the webhook subscribes to. In the
example above that means: `webhook`, `repository` and `issue`.

Also note that the `url` must properly resolve and cannot be an
internal, non-routed address.
