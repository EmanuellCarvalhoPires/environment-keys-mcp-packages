---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/pipelines"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_run_a_pipeline]]"
---
# Bitbucket - Run a pipeline

**Run a pipeline** — `POST /repositories/{workspace}/{repo_slug}/pipelines`

- Run by the tool [[bitbucket_run_a_pipeline]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines?merge_defaults={{param:merge_defaults}}&target_branch_to_create={{param:target_branch_to_create}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `merge_defaults` (query, string, optional) — Whether to merge repository-level defaults into the supplied YAML. Defaults to false.
- `target_branch_to_create` (query, string, optional) — Optional branch name to create from the requested branch or commit target.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Endpoint to create and initiate a pipeline.
There are a number of different options to initiate a pipeline, where the payload of the request will determine which type of pipeline will be instantiated.

## Trigger a pipeline for a branch

One way to trigger pipelines is by specifying the branch for which you want to trigger a pipeline.
The specified branch will be used to determine which pipeline definition from the `bitbucket-pipelines.yml` file will be applied to initiate the pipeline. The pipeline will then do a clone of the repository and checkout the latest revision of the specified branch.

### Example

```
$ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
      -H 'Content-Type: application/json' \
      https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
      -d '
      {
        "target": {
          "ref_type": "branch",
          "type": "pipeline_ref_target",
          "ref_name": "master"
        }
      }'
```

## Trigger a pipeline for a commit on a branch or tag

You can initiate a pipeline for a specific commit and in the context of a specified reference (e.g. a branch, tag or bookmark).
The specified reference will be used to determine which pipeline definition from the bitbucket-pipelines.yml file will be applied to initiate the pipeline. The pipeline will clone the repository and then do a checkout the specified reference.

The following reference types are supported:

* `branch`
* `named_branch`
* `bookmark`
 * `tag`

### Example

```
$ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
      -H 'Content-Type: application/json' \
      https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
      -d '
      {
        "target": {
          "commit": {
            "type": "commit",
            "hash": "ce5b7431602f7cbba007062eeb55225c6e18e956"
          },
          "ref_type": "branch",
          "type": "pipeline_ref_target",
          "ref_name": "master"
        }
      }'
```

## Trigger a specific pipeline definition for a commit

You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a specific commit.
In addition to the commit revision, you specify the type and pattern of the selector that identifies the pipeline definition. The resulting pipeline will then clone the repository and checkout the specified revision.

### Example

```
$ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
      -H 'Content-Type: application/json' \
      https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
      -d '
      {
        "target": {
          "commit": {
            "hash":"a3c4e02c9a3755eccdc3764e6ea13facdf30f923",
            "type":"commit"
          },
          "selector": {
            "type":"custom",
            "pattern":"Deploy to production"
          },
          "type":"pipeline_commit_target"
        }
      }'
```

## Trigger a specific pipeline definition for a commit on a branch or tag

You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a specific commit in the context of a specified reference.
In addition to the commit revision, you specify the type and pattern of the selector that identifies the pipeline definition, as well as the reference information. The resulting pipeline will then clone the repository a checkout the specified reference.

### Example

```
$ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
      -H 'Content-Type: application/json' \
      https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
      -d '
      {
        "target": {
          "commit": {
            "hash":"a3c4e02c9a3755eccdc3764e6ea13facdf30f923",
            "type":"commit"
          },
          "selector": {
            "type": "custom",
            "pattern": "Deploy to production"
          },
          "type": "pipeline_ref_target",
          "ref_name": "master",
          "ref_type": "branch"
        }
      }'
```

## Trigger a custom pipeline with variables

In addition to triggering a custom pipeline that is defined in your `bitbucket-pipelines.yml` file as shown in the examples above, you can specify variables that will be available for your build. In the request, provide a list of variables, specifying the following for each variable: key, value, and whether it should be secured or not (this field is optional and defaults to not secured).

### Example

```
$ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
      -H 'Content-Type: application/json' \
      https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
      -d '
      {
        "target": {
          "type": "pipeline_ref_target",
          "ref_type": "branch",
          "ref_name": "master",
          "selector": {
            "type": "custom",
            "pattern": "Deploy to production"
          }
        },
        "variables": [
          {
            "key": "var1key",
            "value": "var1value",
            "secured": true
          },
          {
            "key": "var2key",
            "value": "var2value"
          }
        ]
      }'
```

## Trigger a pull request pipeline

You can also initiate a pipeline for a specific pull request.

### Example

```
$ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
      -H 'Content-Type: application/json' \
      https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
      -d '
      {
        "target": {
          "type": "pipeline_pullrequest_target",
          "source": "pull-request-branch",
          "destination": "master",
          "destination_commit": {
            "hash": "9f848b7"
          },
          "commit": {
            "hash": "1a372fc"
          },
          "pullrequest": {
            "id": "3"
          },
          "selector": {
            "type": "pull-requests",
            "pattern": "**"
          }
        }
      }'
```

# On-demand pipeline

By default, pipelines run using the YAML in the repository’s `bitbucket-pipelines.yml` configuration file.
With an _on-demand_ pipeline, you include the pipeline’s YAML in the request body. That YAML applies only
to that run and overrides the YAML in `bitbucket-pipelines.yml`.

Just like with regular pipelines, there is a number of different options to initiate an on-demand pipeline.
However, since the payload contains YAML configuration in this case, _query parameters_ are used to supply
the necessary metadata to determine which type of pipeline will be instantiated. These query parameters
are derived from the JSON equivalent by turning each property into a key-value pair with the JSON path
of the property as the new key.

## Optional on-demand query parameters

Use `merge_defaults=true` to merge repository-level defaults into the supplied YAML. Pipelines merges
`image`, `options`, `clone`, `export`, `labels`, and definitions. The supplied YAML still controls
pipeline steps.

Use `target_branch_to_create` to create a branch from the requested branch or commit target before the
run starts. Pipelines then uses the new branch as the on-demand pipeline target.

## Trigger on-demand pipeline for a branch

You can initiate an on-demand pipeline for a specific branch. This branch will be used to determine
which pipeline definition from the supplied YAML configuration will be applied to initiate the pipeline.
The pipeline will then do a clone of the repository and check out the latest revision of the specified branch.

To trigger an on-demand pipeline for a _branch_ the requesting user must have **write permission** for
that branch (which can be limited by [branch restrictions](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/)).

### Example

```
$ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
      -H 'Content-Type: application/yaml' \
      https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipeline_ref_target&target.ref_type=branch&target.ref_name=master \
      -d '
pipelines:
  default:
    - step:
        script:
          - echo This is an on-demand pipeline'
```

## Trigger on-demand pipeline for a commit on a branch or tag

You can initiate an on-demand pipeline for a specific commit and in the context of a specified reference
(branch or tag). The specified reference will be used to determine which pipeline definition from the supplied
YAML configuration will be applied to initiate the pipeline. The pipeline will clone the repository and
check out the specified reference.

To trigger an on-demand pipeline for a _branch_ the requesting user must have **write permission** for
that branch (which can be limited by [branch restrictions](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/)).

### Example

```
$ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
      -H 'Content-Type: application/yaml' \
      https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipeline_ref_target&target.ref_type=branch&target.ref_name=master&target.commit.hash=ce5b7431602f7cbba007062eeb55225c6e18e956 \
      -d '
pipelines:
  default:
    - step:
        script:
          - echo This is an on-demand pipeline'
```

## Trigger a specific on-demand pipeline definition for a commit

You can trigger a specific pipeline that is defined in the supplied YAML configuration for a specific commit.
In addition to the commit revision, you specify the type and pattern of the selector that identifies
the pipeline definition. The resulting pipeline will then clone the repository and checkout the specified revision.

### Example

```
$ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
      -H 'Content-Type: application/yaml' \
      https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipeline_commit_target&target.commit.hash=a3c4e02c9a3755eccdc3764e6ea13facdf30f923&target.selector.type=custom&target.selector.pattern=security-scan \
      -d '
pipelines:
  custom:
    security-scan:
      - step:
          script:
            - echo Run on-demand security scan
```

## Trigger a custom on-demand pipeline with variables

In addition to triggering a custom on-demand pipeline that is defined in the supplied YAML configuration
as shown in the examples above, you can specify variables that will be available for your build.
In the request, provide each variable as an indexed set of query parameters representing its key, value,
and whether it should be secured or not (this field is optional and defaults to not secured).

### Example

```
$ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
      -H 'Content-Type: application/yaml' \
      https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipeline_ref_target&target.ref_type=branch&target.ref_name=master&target.selector.type=custom&target.selector.pattern=security-scan&variables[0].key=var1key&variables[0].value=var1value&variables[0].secured=true&variables[1].key=var2key&variables[1].value=var2value \
      -d '
pipelines:
  custom:
    security-scan:
      - variables:
          - name: var1key
          - name: var2key
      - step:
          script:
            - echo Run on-demand security scan'
```

## Trigger a pull request pipeline

You can also initiate an on-demand pipeline for a specific pull request.

### Example

```
$ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
      -H 'Content-Type: application/yaml' \
      https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipeline_pullrequest_target&target.source=pull-request-branch&target.destination=destination&target.destination_commit.hash=9f848b7&target.commit.hash=1a372fc&target.pullrequest.id=3&target.selector.type=pull-requests&target.selector.pattern=** \
      -d '
pipelines:
  pull-requests:
    "**":
      - step:
          script:
            - echo This is an on-demand pipeline'
```
