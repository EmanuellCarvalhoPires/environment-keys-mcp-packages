---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/workspaces/{workspace}/projects/{project_key}"
category: "Projects"
writes_data: true
tool_note: "[[bitbucket_update_a_project_for_a_workspace]]"
---
# Bitbucket - Update a project for a workspace

**Update a project for a workspace** — `PUT /workspaces/{workspace}/projects/{project_key}`

- Run by the tool [[bitbucket_update_a_project_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Since this endpoint can be used to both update and to create a
project, the request body depends on the intent.

#### Creation

See the POST documentation for the project collection for an
example of the request body.

Note: The `key` should not be specified in the body of request
(since it is already present in the URL). The `name` is required,
everything else is optional.

#### Update

See the POST documentation for the project collection for an
example of the request body.

Note: The key is not required in the body (since it is already in
the URL). The key may be specified in the body, if the intent is
to change the key itself. In such a scenario, the location of the
project is changed and is returned in the `Location` header of the
response.
