---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/pullrequests"
category: "Pullrequests"
writes_data: true
tool_note: "[[bitbucket_create_a_pull_request]]"
---
# Bitbucket - Create a pull request

**Create a pull request** — `POST /repositories/{workspace}/{repo_slug}/pullrequests`

- Run by the tool [[bitbucket_create_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new pull request where the destination repository is
this repository and the author is the authenticated user.

The minimum required fields to create a pull request are `title` and
`source`, specified by a branch name.

```
curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-repository/pullrequests \
    -u my-username:my-password \
    --request POST \
    --header 'Content-Type: application/json' \
    --data '{
        "title": "My Title",
        "source": {
            "branch": {
                "name": "staging"
            }
        }
    }'
```

If the pull request's `destination` is not specified, it will default
to the `repository.mainbranch`. To open a pull request to a
different branch, say from a feature branch to a staging branch,
specify a `destination` (same format as the `source`):

```
{
    "title": "My Title",
    "source": {
        "branch": {
            "name": "my-feature-branch"
        }
    },
    "destination": {
        "branch": {
            "name": "staging"
        }
    }
}
```

Reviewers can be specified by adding an array of user objects as the
`reviewers` property.

```
{
    "title": "My Title",
    "source": {
        "branch": {
            "name": "my-feature-branch"
        }
    },
    "reviewers": [
        {
            "uuid": "{504c3b62-8120-4f0c-a7bc-87800b9d6f70}"
        }
    ]
}
```

Other fields:

* `description` - a string
* `close_source_branch` - boolean that specifies if the source branch should be closed upon merging
* `draft` - boolean that specifies whether the pull request is a draft
