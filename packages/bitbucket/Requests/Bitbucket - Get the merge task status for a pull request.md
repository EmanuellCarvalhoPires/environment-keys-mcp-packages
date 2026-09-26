---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_get_the_merge_task_status_for_a_pull_request]]"
---
# Bitbucket - Get the merge task status for a pull request

**Get the merge task status for a pull request** — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}`

- Run by the tool [[bitbucket_get_the_merge_task_status_for_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/merge/task-status/{{param:task_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.
- `task_id` (path, string, required) — Value of taskid in the path.

## Original description

When merging a pull request takes too long, the client receives a
task ID along with a 202 status code. The task ID can be used in a call
to this endpoint to check the status of a merge task.

```
curl -X GET https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-status/
```

If the merge task is not yet finished, a PENDING status will be returned.

```
HTTP/2 200
{
    "task_status": "PENDING",
    "links": {
        "self": {
            "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-status/"
        }
    }
}
```

If the merge was successful, a SUCCESS status will be returned.

```
HTTP/2 200
{
    "task_status": "SUCCESS",
    "links": {
        "self": {
            "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-status/"
        }
    },
    "merge_result": 
}
```

If the merge task failed, an error will be returned.

```
{
    "type": "error",
    "error": {
        "message": ""
    }
}
```
