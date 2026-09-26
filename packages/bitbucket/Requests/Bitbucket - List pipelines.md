---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pipelines"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_list_pipelines]]"
---
# Bitbucket - List pipelines

**List pipelines** — `GET /repositories/{workspace}/{repo_slug}/pipelines`

- Run by the tool [[bitbucket_list_pipelines]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines?creator.uuid={{param:creator_uuid}}&target.ref_type={{param:target_ref_type}}&target.ref_name={{param:target_ref_name}}&target.branch={{param:target_branch}}&target.commit.hash={{param:target_commit_hash}}&target.selector.pattern={{param:target_selector_pattern}}&target.selector.type={{param:target_selector_type}}&created_on={{param:created_on}}&trigger_type={{param:trigger_type}}&status={{param:status}}&sort={{param:sort}}&page={{param:page}}&pagelen={{param:pagelen}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `creator_uuid` (query, string, optional) — The UUID of the creator of the pipeline to filter by.
- `target_ref_type` (query, string, optional) — The type of the reference to filter by.
- `target_ref_name` (query, string, optional) — The reference name to filter by.
- `target_branch` (query, string, optional) — The name of the branch to filter by.
- `target_commit_hash` (query, string, optional) — The revision to filter by.
- `target_selector_pattern` (query, string, optional) — The pipeline pattern to filter by.
- `target_selector_type` (query, string, optional) — The type of pipeline to filter by.
- `created_on` (query, string, optional) — The creation date to filter by.
- `trigger_type` (query, string, optional) — The trigger type to filter by.
- `status` (query, string, optional) — The pipeline status to filter by.
- `sort` (query, string, optional) — The attribute name to sort on.
- `page` (query, string, optional) — The page number of elements to retrieve.
- `pagelen` (query, string, optional) — The maximum number of results to return.

## Original description

Find pipelines in a repository.

Note that unlike other endpoints in the Bitbucket API, this endpoint utilizes query parameters to allow filtering
and sorting of returned results. See [query parameters](#api-repositories-workspace-repo-slug-pipelines-get-request-Query%20parameters)
for specific details.
