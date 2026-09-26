---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/workspaces/{workspace}/hooks"
category: "Workspaces"
writes_data: true
tool_note: "[[bitbucket_create_a_webhook_for_a_workspace]]"
---
# Bitbucket - Create a webhook for a workspace

**Create a webhook for a workspace** — `POST /workspaces/{workspace}/hooks`

- Run by the tool [[bitbucket_create_a_webhook_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/workspaces/{{service.workspace}}/hooks
Authorization: {{service.auth_token}}
```

## Original description

Creates a new webhook on the specified workspace.

Workspace webhooks are fired for events from all repositories contained
by that workspace.

Example:

```
$ curl -X POST -u credentials -H 'Content-Type: application/json'
  https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks
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

This call requires the webhook scope, as well as any scope
that applies to the events that the webhook subscribes to. In the
example above that means: `webhook`, `repository` and `issue`.

The `url` must properly resolve and cannot be an internal, non-routed address.

Only workspace owners can install webhooks on workspaces.
