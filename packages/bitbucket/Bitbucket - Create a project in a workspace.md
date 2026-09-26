---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/workspaces/{workspace}/projects"
category: "Projects"
writes_data: true
tool_note: "[[bitbucket_create_a_project_in_a_workspace]]"
---
# Bitbucket - Create a project in a workspace

**Create a project in a workspace** — `POST /workspaces/{workspace}/projects`

- Run by the tool [[bitbucket_create_a_project_in_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/workspaces/{{service.workspace}}/projects
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new project.

Note that the avatar has to be embedded as either a data-url
or a URL to an external image as shown in the examples below:

```
$ body=$(cat << EOF
{
    "name": "Mars Project",
    "key": "MARS",
    "description": "Software for colonizing mars.",
    "links": {
        "avatar": {
            "href": "data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/..."
        }
    },
    "is_private": false
}
EOF
)
$ curl -H "Content-Type: application/json" \
       -X POST \
       -d "$body" \
       https://api.bitbucket.org/2.0/workspaces/teams-in-space/projects/ | jq .
{
  // Serialized project document
}
```

or even:

```
$ body=$(cat << EOF
{
    "name": "Mars Project",
    "key": "MARS",
    "description": "Software for colonizing mars.",
    "links": {
        "avatar": {
            "href": "http://i.imgur.com/72tRx4w.gif"
        }
    },
    "is_private": false
}
EOF
)
$ curl -H "Content-Type: application/json" \
       -X POST \
       -d "$body" \
       https://api.bitbucket.org/2.0/workspaces/teams-in-space/projects/ | jq .
{
  // Serialized project document
}
```
