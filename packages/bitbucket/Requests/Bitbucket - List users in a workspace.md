---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/members"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_list_users_in_a_workspace]]"
---
# Bitbucket - List users in a workspace

**List users in a workspace** — `GET /workspaces/{workspace}/members`

- Run by the tool [[bitbucket_list_users_in_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/members
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all members of the requested workspace.

This endpoint additionally supports [filtering](/cloud/bitbucket/rest/intro/#filtering) by
email address, if called by a workspace administrator, integration or workspace access
token. This is done by adding the following query string parameter:

* `q=user.email IN ("user1@org.com","user2@org.com")`

When filtering by email, you can query up to 90 addresses at a time.
Note that the query parameter values need to be URL escaped, so the final query string
should be:

* `q=user.email%20IN%20(%22user1@org.com%22,%22user2@org.com%22)`

Email addresses that you filter by (and only these email addresses) can be included in the
response using the `fields` query parameter:

* `&fields=+values.user.email` - add the `email` field to the default `user` response object
* `&fields=values.user.email,values.user.account_id` - only return user email addresses and
account IDs

Once again, all query parameter values must be URL escaped.
